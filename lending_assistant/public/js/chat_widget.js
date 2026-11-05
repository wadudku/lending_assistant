// Lending Assistant chat panel (M5).
// Server text reaches the page in exactly one way as markup: render_answer() below (Frappe's markdown sanitiser,
// then our stricter pass). Everything else the user or the server wrote (questions, titles, errors, comments) goes
// in with textContent. A Python test (test_chat_widget_source) enforces both.
frappe.provide("lending_assistant");

(function () {
	"use strict";

	const ROLE = "Assistant User";
	const ASK = "lending_assistant.api.chat.ask";
	const FEEDBACK = "lending_assistant.api.chat.feedback";
	const LIST = "frappe.client.get_list";
	const CONVERSATION = "Assistant Conversation";
	const MESSAGE = "Assistant Message";
	const KB_IMG = "/assets/lending_assistant/kb_img/";
	const PREFS_KEY = "lending_assistant.prefs";
	const CLIENT_TIMEOUT_MS = 130000; // server budget is 90 s (100 s Deep), see orchestrator.BUDGET
	const HISTORY_CAP = 30;
	const MESSAGE_CAP = 50;
	const MAX_COMMENT = 1000;
	// Must equal prompts.SOURCE_LABELS (a Python test compares them).
	const LABELS = ["[Analysis]", "[Team finding]", "[Live site]", "[Code]", "[General knowledge]", "[Web]"];
	const DEPTHS = ["Business", "Technical", "Both"];
	const ALLOWED_TAGS = new Set(["p", "br", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "blockquote", "pre", "code", "em", "strong", "del", "b", "i", "a", "img", "table", "thead", "tbody", "tr", "th", "td"]);

	let built = false;
	let conversation = null;
	let ui = {};
	let busy = false;
	let request_id = 0;
	let chip_text = "";
	let chip_cleared = false;
	let prefs = { depth: "Both", deep: 0 };

	function el(tag, className, text) {
		const node = document.createElement(tag);
		if (className) node.className = className;
		if (text !== undefined) node.textContent = text;
		return node;
	}

	// ---- preferences (per browser; storage may be blocked) --------------------------------------------------------

	function read_prefs() {
		try {
			const saved = JSON.parse(window.localStorage.getItem(PREFS_KEY) || "{}");
			if (DEPTHS.indexOf(saved.depth) >= 0) prefs.depth = saved.depth;
			if (saved.deep === 1 || saved.deep === 0) prefs.deep = saved.deep;
		} catch (e) {
			/* work without storage */
		}
	}

	function write_prefs() {
		try {
			window.localStorage.setItem(PREFS_KEY, JSON.stringify(prefs));
		} catch (e) {
			/* work without storage */
		}
	}

	// ---- rendering: the only place model text becomes markup -------------------------------------------------------

	// http(s) links, or a same-origin path that starts with ONE slash. Everything else is not a link.
	function safe_href(href) {
		if (typeof href !== "string" || /[\s\u0000-\u001f\\]/.test(href)) return null;
		if (href.startsWith("/")) return href.startsWith("//") ? null : href;
		try {
			const url = new URL(href);
			return url.protocol === "https:" || url.protocol === "http:" ? href : null;
		} catch (e) {
			return null;
		}
	}

	function safe_img(src) {
		return (
			typeof src === "string" &&
			src.startsWith(KB_IMG) &&
			!/\.\.|\\|\/\/|%2e|%2f|%5c|[\s\u0000-\u001f]/i.test(src.slice(KB_IMG.length - 1))
		);
	}

	function harden(root) {
		for (const node of Array.from(root.children)) {
			harden(node);
			const tag = node.tagName.toLowerCase();
			if (tag === "img") {
				const src = node.getAttribute("src");
				if (!safe_img(src)) {
					node.replaceWith(document.createTextNode(node.getAttribute("alt") || ""));
					continue;
				}
			} else if (tag === "a") {
				const href = safe_href(node.getAttribute("href"));
				if (!href) {
					node.replaceWith(...node.childNodes);
					continue;
				}
			} else if (!ALLOWED_TAGS.has(tag)) {
				node.replaceWith(...node.childNodes);
				continue;
			}
			const keep = { title: true, alt: tag === "img", src: tag === "img", href: tag === "a" };
			if ((tag === "code" || tag === "pre") && /^language-[\w-]+$/.test(node.getAttribute("class") || "")) {
				keep["class"] = true;
			}
			for (const attr of Array.from(node.attributes)) {
				if (!keep[attr.name.toLowerCase()]) node.removeAttribute(attr.name);
			}
			if (tag === "a") {
				node.setAttribute("href", safe_href(node.getAttribute("href")));
				node.setAttribute("target", "_blank");
				node.setAttribute("rel", "noopener noreferrer");
			} else if (tag === "img") {
				node.setAttribute("loading", "lazy");
			}
		}
	}

	function label_slug(label) {
		return label.slice(1, -1).toLowerCase().replace(/ /g, "-");
	}

	function badge_labels(root) {
		const pattern = new RegExp(LABELS.map((l) => l.replace(/[[\]]/g, "\\$&")).join("|"), "g");
		const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
		const texts = [];
		while (walker.nextNode()) {
			if (!walker.currentNode.parentElement.closest("code, pre, a")) texts.push(walker.currentNode);
		}
		for (const text of texts) {
			const value = text.nodeValue;
			pattern.lastIndex = 0;
			if (!pattern.test(value)) continue;
			pattern.lastIndex = 0;
			const parts = document.createDocumentFragment();
			let last = 0;
			let m;
			while ((m = pattern.exec(value)) !== null) {
				if (m.index > last) parts.appendChild(document.createTextNode(value.slice(last, m.index)));
				parts.appendChild(el("span", "ast-badge ast-badge-" + label_slug(m[0]), m[0]));
				last = m.index + m[0].length;
			}
			if (last < value.length) parts.appendChild(document.createTextNode(value.slice(last)));
			text.replaceWith(parts);
		}
	}

	function mark_callouts(root) {
		for (const node of root.querySelectorAll("p, li")) {
			if (/^\s*⚠/.test(node.textContent)) node.classList.add("ast-callout");
		}
	}

	// THE render function. Frappe's markdown (showdown + its whitelist sanitiser), then harden(), badges, callouts.
	function render_answer(container, markdown) {
		const parsed = new DOMParser().parseFromString(frappe.markdown(String(markdown || "")), "text/html");
		harden(parsed.body);
		badge_labels(parsed.body);
		mark_callouts(parsed.body);
		container.replaceChildren(...parsed.body.childNodes);
	}

	// ---- log lines -------------------------------------------------------------------------------------------------

	function scroll_down() {
		ui.log.scrollTop = ui.log.scrollHeight;
	}

	function add_line(kind, text) {
		const line = el("div", "ast-line ast-" + kind, text);
		ui.log.appendChild(line);
		scroll_down();
		return line;
	}

	function add_answer(msg) {
		const wrap = el("div", "ast-line ast-assistant ast-status-" + (msg.status === "ok" ? "ok" : msg.status === "limited" ? "limited" : "error"));
		if (msg.status === "limited") {
			wrap.appendChild(el("div", "ast-note", __("Partial answer: a limit was reached before it was finished.")));
		}
		const body = el("div", "ast-md");
		render_answer(body, msg.answer);
		wrap.appendChild(body);
		if (msg.message) wrap.appendChild(feedback_row(msg));
		ui.log.appendChild(wrap);
		scroll_down();
	}

	// ---- feedback --------------------------------------------------------------------------------------------------

	function feedback_row(msg) {
		const row = el("div", "ast-feedback");
		let value = msg.feedback || "";
		let sending = false;
		let saved_comment = msg.feedback_comment || "";
		const state = el("span", "ast-fb-state", "");
		const up = el("button", "ast-fb ast-fb-up", "👍");
		const down = el("button", "ast-fb ast-fb-down", "👎");
		const more = el("button", "ast-fb-link", __("Comment"));
		const box = el("div", "ast-fb-box");
		const text = el("textarea", "ast-fb-text");
		const save = el("button", "ast-fb-save", __("Send comment"));
		for (const b of [up, down, more, save]) b.type = "button";
		up.setAttribute("aria-label", __("Helpful"));
		down.setAttribute("aria-label", __("Not helpful"));
		text.maxLength = MAX_COMMENT;
		text.rows = 2;
		text.value = msg.feedback_comment || "";
		box.hidden = true;
		box.appendChild(text);
		box.appendChild(save);

		function refresh() {
			up.setAttribute("aria-pressed", String(value === "up"));
			down.setAttribute("aria-pressed", String(value === "down"));
			up.classList.toggle("ast-fb-on", value === "up");
			down.classList.toggle("ast-fb-on", value === "down");
			state.textContent = value ? __("Feedback saved: {0}", [value === "up" ? __("helpful") : __("not helpful")]) : "";
		}

		function send(new_value, comment) {
			if (sending) return;
			sending = true;
			frappe.call({
				method: FEEDBACK,
				type: "POST",
				args: { message: msg.message, value: new_value, comment: comment },
				callback: function (r) {
					sending = false;
					if (r && r.message) {
						value = r.message.feedback;
						saved_comment = comment;
						refresh();
					}
				},
				error: function (xhr) {
					sending = false;
					state.textContent = server_message(xhr) || __("Feedback could not be saved.");
				},
			});
		}

		// The same value is not sent twice (the comment can still be added with "Send comment").
		function thumb(v) {
			if (v !== value) send(v, text.value);
		}

		up.addEventListener("click", () => thumb("up"));
		down.addEventListener("click", () => thumb("down"));
		more.addEventListener("click", () => {
			box.hidden = !box.hidden;
		});
		save.addEventListener("click", () => {
			if (!value) {
				state.textContent = __("Choose helpful or not helpful first.");
			} else if (text.value !== saved_comment) {
				send(value, text.value);
			}
		});
		row.append(up, down, more, state, box);
		if (msg.feedback_comment) box.hidden = false;
		refresh();
		return row;
	}

	// ---- errors from the server ------------------------------------------------------------------------------------

	function server_message(xhr) {
		try {
			const data = xhr && xhr.responseJSON;
			if (data && data._server_messages) {
				const list = JSON.parse(data._server_messages).map((m) => JSON.parse(m).message);
				const doc = new DOMParser().parseFromString(list.join(" "), "text/html");
				return doc.body.textContent.trim();
			}
		} catch (e) {
			/* fall through */
		}
		return "";
	}

	// ---- context chip ----------------------------------------------------------------------------------------------

	function route_label(route) {
		const parts = (route || []).filter(Boolean);
		if (!parts.length) return "";
		const kind = String(parts[0]).toLowerCase();
		if (kind === "form" && parts.length >= 3) return parts[1] + " " + parts.slice(2).join("/");
		if ((kind === "list" || kind === "report" || kind === "query-report") && parts.length >= 2) return parts[1] + " " + __("list");
		return parts.join("/");
	}

	function current_route() {
		return chip_cleared ? "" : frappe.get_route_str() || "";
	}

	function update_chip(reset) {
		if (reset) chip_cleared = false;
		chip_text = chip_cleared ? "" : route_label(frappe.get_route());
		ui.chip.hidden = !chip_text;
		ui.chip_text.textContent = chip_text;
	}

	// ---- sending ---------------------------------------------------------------------------------------------------

	function set_busy(on) {
		busy = on;
		ui.send.disabled = on;
		ui.input.disabled = on;
		ui.busy.hidden = !on;
		if (!on && ui.timer) {
			clearInterval(ui.timer);
			ui.timer = null;
		}
	}

	function start_clock() {
		const t0 = Date.now();
		const tick = () => {
			const s = Math.floor((Date.now() - t0) / 1000);
			ui.busy.textContent = __("Working... {0} s", [s]) + (s >= 30 ? " " + __("(Deep answers can take about 100 s)") : "");
		};
		tick();
		ui.timer = setInterval(tick, 1000);
	}

	function send() {
		const question = ui.input.value.trim();
		if (!question || busy) return;
		const my_request = ++request_id;

		add_line("user", question);
		ui.input.value = "";
		set_busy(true);
		start_clock();

		const args = { question: question, route: current_route(), depth: prefs.depth, deep: prefs.deep };
		if (conversation) args.conversation = conversation;

		let finished = false;
		const finish = () => {
			finished = true;
			clearTimeout(timer);
			set_busy(false);
			ui.input.focus();
		};
		let xhr = null;
		const timer = setTimeout(function () {
			if (finished) return;
			request_id++; // a late answer is ignored
			if (xhr && xhr.abort) xhr.abort();
			finish();
			add_line("error", __("The advisor took too long. The answer may still have been saved: open History."));
		}, CLIENT_TIMEOUT_MS);

		xhr = frappe.call({
			method: ASK,
			type: "POST",
			args: args,
			callback: function (r) {
				if (finished || my_request !== request_id) return;
				finish();
				if (r && r.message) {
					conversation = r.message.conversation;
					add_answer(r.message);
				}
			},
			error: function (xhr_err) {
				if (finished || my_request !== request_id) return;
				finish();
				add_line("error", server_message(xhr_err) || __("The assistant could not answer."));
			},
		});
	}

	// ---- conversations ---------------------------------------------------------------------------------------------

	function new_conversation() {
		conversation = null;
		ui.log.replaceChildren();
		show_view("chat");
		ui.input.focus();
	}

	function show_view(view) {
		ui.history.hidden = view !== "history";
		ui.log.hidden = view !== "chat";
	}

	function load_history() {
		show_view("history");
		ui.history.replaceChildren(el("div", "ast-note", __("Loading...")));
		frappe.call({
			method: LIST,
			type: "GET",
			args: {
				doctype: CONVERSATION,
				filters: { user: frappe.session.user },
				fields: ["name", "title", "last_activity", "message_count"],
				order_by: "last_activity desc",
				limit_page_length: HISTORY_CAP,
			},
			callback: function (r) {
				const rows = (r && r.message) || [];
				ui.history.replaceChildren();
				if (!rows.length) ui.history.appendChild(el("div", "ast-note", __("No conversations yet.")));
				for (const row of rows) {
					const item = el("button", "ast-history-item");
					item.type = "button";
					item.appendChild(el("span", "ast-history-title", row.title || row.name));
					item.appendChild(el("span", "ast-history-meta", (row.message_count || 0) + " " + __("messages") + " · " + (row.last_activity || "")));
					item.addEventListener("click", () => open_conversation(row.name));
					ui.history.appendChild(item);
				}
				if (rows.length >= HISTORY_CAP) ui.history.appendChild(el("div", "ast-note", __("Showing the latest {0}.", [HISTORY_CAP])));
			},
			error: function (xhr) {
				ui.history.replaceChildren(el("div", "ast-line ast-error", server_message(xhr) || __("History could not be loaded.")));
			},
		});
	}

	function open_conversation(name) {
		frappe.call({
			method: LIST,
			type: "GET",
			args: {
				doctype: MESSAGE,
				filters: { conversation: name, user: frappe.session.user },
				fields: ["name", "question", "answer", "status", "depth", "deep", "feedback", "feedback_comment", "route", "creation"],
				order_by: "creation desc",
				limit_page_length: MESSAGE_CAP,
			},
			callback: function (r) {
				const rows = ((r && r.message) || []).slice().reverse();
				conversation = name;
				ui.log.replaceChildren();
				show_view("chat");
				if (rows.length >= MESSAGE_CAP) add_line("note", __("Older messages are not shown."));
				for (const row of rows) {
					add_line("user", row.question || "");
					add_answer({ message: row.name, answer: row.answer || "", status: row.status, feedback: row.feedback, feedback_comment: row.feedback_comment });
				}
			},
			error: function (xhr) {
				add_line("error", server_message(xhr) || __("The conversation could not be opened."));
			},
		});
	}

	// ---- panel -----------------------------------------------------------------------------------------------------

	function toggle(open) {
		const show = open === undefined ? ui.panel.hidden : open;
		ui.panel.hidden = !show;
		if (show) {
			update_chip(false);
			ui.input.focus();
		}
	}

	function build() {
		read_prefs();
		ui.button = el("button", "ast-fab", __("Ask"));
		ui.button.type = "button";
		ui.button.title = __("Lending Assistant");
		ui.button.addEventListener("click", () => toggle());

		ui.panel = el("div", "ast-panel");
		ui.panel.hidden = true;
		ui.panel.addEventListener("keydown", function (e) {
			if (e.key === "Escape") {
				e.stopPropagation();
				toggle(false);
				ui.button.focus();
			}
		});

		const header = el("div", "ast-header");
		header.appendChild(el("span", "ast-title", __("Lending Assistant")));
		const tools = el("span", "ast-tools");
		const history = el("button", "ast-tool", __("History"));
		const fresh = el("button", "ast-tool", __("New conversation"));
		const close = el("button", "ast-close", "×");
		close.setAttribute("aria-label", __("Close"));
		for (const b of [history, fresh, close]) {
			b.type = "button";
			tools.appendChild(b);
		}
		history.addEventListener("click", () => (ui.history.hidden ? load_history() : show_view("chat")));
		fresh.addEventListener("click", new_conversation);
		close.addEventListener("click", () => toggle(false));
		header.appendChild(tools);

		ui.chip = el("div", "ast-chip");
		ui.chip.hidden = true;
		ui.chip_text = el("span", "ast-chip-text", "");
		const clear = el("button", "ast-chip-clear", "×");
		clear.type = "button";
		clear.title = __("Ask without this context");
		clear.setAttribute("aria-label", __("Clear context"));
		clear.addEventListener("click", () => {
			chip_cleared = true;
			update_chip(false);
		});
		ui.chip.append(ui.chip_text, clear);

		ui.log = el("div", "ast-log");
		ui.history = el("div", "ast-historylist");
		ui.history.hidden = true;
		ui.busy = el("div", "ast-busy", "");
		ui.busy.hidden = true;

		const options = el("div", "ast-options");
		ui.depth = el("select", "ast-depth");
		ui.depth.setAttribute("aria-label", __("Depth"));
		for (const d of DEPTHS) {
			const o = el("option", "", __(d));
			o.value = d;
			ui.depth.appendChild(o);
		}
		ui.depth.value = prefs.depth;
		ui.depth.addEventListener("change", () => {
			prefs.depth = ui.depth.value;
			write_prefs();
		});
		const deep_label = el("label", "ast-deep");
		ui.deep = el("input");
		ui.deep.type = "checkbox";
		ui.deep.checked = prefs.deep === 1;
		ui.deep.addEventListener("change", () => {
			prefs.deep = ui.deep.checked ? 1 : 0;
			write_prefs();
		});
		deep_label.append(ui.deep, document.createTextNode(" " + __("Deep analysis (slower, larger model)")));
		options.append(ui.depth, deep_label);

		const form = el("div", "ast-form");
		ui.input = el("textarea", "ast-input");
		ui.input.rows = 2;
		ui.input.maxLength = 4000;
		ui.input.placeholder = __("Ask a question");
		ui.input.addEventListener("keydown", function (e) {
			if (e.key === "Enter" && !e.shiftKey && !e.isComposing) {
				e.preventDefault();
				send();
			}
		});
		ui.send = el("button", "ast-send", __("Send"));
		ui.send.type = "button";
		ui.send.addEventListener("click", send);
		form.append(ui.input, ui.send);

		ui.panel.append(header, ui.chip, ui.log, ui.history, ui.busy, options, form);
		document.body.append(ui.button, ui.panel);

		frappe.router.on("change", () => update_chip(true));
		update_chip(true);
	}

	function init() {
		if (built) return;
		if (!frappe.user || !frappe.user.has_role(ROLE)) return;
		built = true;
		build();
	}

	$(document).on("startup", init);
})();
