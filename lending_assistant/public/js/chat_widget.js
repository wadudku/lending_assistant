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
	const SAVE = "lending_assistant.api.findings.save";
	const LIST = "frappe.client.get_list";
	const CONVERSATION = "Assistant Conversation";
	const MESSAGE = "Assistant Message";
	const FINDING = "Assistant Finding";
	const KB_IMG = "/assets/lending_assistant/kb_img/";
	const FINDING_ROUTE = "/app/assistant-finding/";
	const FINDING_NAME = /^AF-\d{5,}$/;
	const MAX_TITLE = 140;
	const MAX_SUMMARY = 4000;
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

	// Links: http(s) to other sites; on THIS site only /app/... and /assets/lending_assistant/... (a GET API route such as
	// /api/method/logout must not become a link, M5-I1). Absolute URLs on this origin and dot-segment or encoded tricks go
	// through the same rule. Anything else is not a link: harden() keeps its text.
	function safe_href(href) {
		if (typeof href !== "string" || /[\s\u0000-\u001f\\]/.test(href)) return null;
		let url;
		try {
			url = new URL(href, window.location.origin);
		} catch (e) {
			return null;
		}
		if (url.protocol !== "https:" && url.protocol !== "http:") return null;
		// a trailing dot is the same host (lending_site. = lending_site), so it must not count as "another site" (M6-R6)
		const same_host = url.hostname.replace(/\.$/, "") === window.location.hostname.replace(/\.$/, "");
		if (!href.startsWith("/") && !same_host) return href;
		if (href.startsWith("//")) return null;
		const path = url.pathname;
		if (/\.\.|%2e|%2f|%5c|%25|\/\/|\/\.(\/|$)/i.test(path)) return null;
		return path === "/app" || path.startsWith("/app/") || path.startsWith("/assets/lending_assistant/") ? href : null;
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

	// showdown turns word_with_underscores into emphasis, and escaping with a backslash shows up literally where
	// showdown keeps backslashes verbatim. So: in plain text, escape every underscore of any token that contains one
	// ("__init__", "x__y__z", "howto.loan_repayment"; "_word_" emphasis is given up, the prompt uses "*"). Parts that
	// must stay verbatim are split out first: fences of 3+ backticks or tildes, inline code, indented code lines,
	// reference definitions, "](url)", <autolinks>, http(s) URLs and www. URLs.
	function protect_underscores(md) {
		const verbatim =
			/((?:`{3,}|~{3,})[\s\S]*?(?:`{3,}|~{3,})|`[^`\n]*`|^(?: {4}|\t).*$|^ {0,3}\[[^\]]+\]:.*$|\]\([^)\s]*\)|<[^<>\s]+>|https?:\/\/\S+|www\.\S+)/m;
		return md
			.split(new RegExp(verbatim.source, "gm"))
			.map((part, i) => (i % 2 ? part : part.replace(/[\w.]*_[\w.]*/g, (t) => t.replace(/_/g, "\\_"))))
			.join("");
	}

	// THE render function. Frappe's markdown (showdown + its whitelist sanitiser), then harden(), badges, callouts.
	function render_answer(container, markdown) {
		const parsed = new DOMParser().parseFromString(frappe.markdown(protect_underscores(String(markdown || ""))), "text/html");
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
		const finding = finding_row(msg);
		if (finding) wrap.appendChild(finding);
		ui.log.appendChild(wrap);
		scroll_down();
	}

	// ---- findings: Save as finding (a click is the only way a finding is made, G13) ----------------------------------

	function suggestion_of(msg) {
		let s = msg.suggestion;
		if (!s && msg.finding_suggestion) {
			try {
				s = JSON.parse(msg.finding_suggestion);
			} catch (e) {
				s = null;
			}
		}
		if (!s || typeof s.title !== "string" || typeof s.summary !== "string") return null;
		return {
			title: s.title,
			summary: s.summary,
			br_ids: Array.isArray(s.br_ids) ? s.br_ids.map(String) : [],
			doctypes: Array.isArray(s.doctypes) ? s.doctypes.map(String) : [],
		};
	}

	function saved_row(name) {
		const row = el("div", "ast-finding ast-finding-saved");
		row.appendChild(el("span", "", __("Saved as") + " "));
		if (typeof name === "string" && FINDING_NAME.test(name)) {
			const link = el("a", "", name);
			link.href = FINDING_ROUTE + encodeURIComponent(name);
			link.target = "_blank";
			link.rel = "noopener noreferrer";
			row.appendChild(link);
		} else {
			row.appendChild(el("span", "", __("a finding")));
		}
		return row;
	}

	function finding_row(msg) {
		if (!msg.message) return null;
		if (msg.finding) return saved_row(msg.finding);
		const suggestion = suggestion_of(msg);
		if (!suggestion) return null;
		const row = el("div", "ast-finding");
		const button = el("button", "ast-finding-save", __("Save as finding"));
		button.type = "button";
		button.addEventListener("click", () => open_save_dialog(msg, suggestion, row));
		row.appendChild(button);
		return row;
	}

	// The dialog title and every label are fixed translated strings (Frappe inserts a dialog title as HTML). The model's
	// title, summary and references only ever travel as field VALUES, which Frappe puts in inputs or escapes.
	function open_save_dialog(msg, suggestion, row) {
		let saving = false;
		const dialog = new frappe.ui.Dialog({
			title: __("Save as finding"),
			fields: [
				{ fieldname: "title", fieldtype: "Data", label: __("Title"), reqd: 1 },
				{ fieldname: "summary", fieldtype: "Text", label: __("Summary"), reqd: 1 },
				{ fieldname: "refs", fieldtype: "Small Text", label: __("BR ids and doctypes"), read_only: 1 },
			],
			primary_action_label: __("Save"),
			primary_action: function (values) {
				const title = String(values.title || "").trim();
				const summary = String(values.summary || "").trim();
				if (!title || title.length > MAX_TITLE) {
					add_line("error", __("The title is required and at most {0} characters.", [MAX_TITLE]));
					return;
				}
				if (!summary || summary.length > MAX_SUMMARY) {
					add_line("error", __("The summary is required and at most {0} characters.", [MAX_SUMMARY]));
					return;
				}
				if (saving) return;
				saving = true;
				post(SAVE, { message: msg.message, title: title, summary: summary })
					.then(function (res) {
						saving = false;
						if (res.ok && res.data.message && res.data.message.finding) {
							dialog.hide();
							row.replaceWith(saved_row(res.data.message.finding));
						} else {
							add_line("error", message_of(res.data) || __("The finding could not be saved."));
						}
					})
					.catch(function () {
						saving = false;
						add_line("error", __("The finding could not be saved."));
					});
			},
		});
		dialog.set_value("title", suggestion.title);
		dialog.set_value("summary", suggestion.summary);
		dialog.set_value("refs", suggestion.br_ids.concat(suggestion.doctypes).join("\n"));
		dialog.show();
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
			post(FEEDBACK, { message: msg.message, value: new_value, comment: comment })
				.then(function (res) {
					sending = false;
					if (res.ok && res.data.message) {
						value = res.data.message.feedback;
						saved_comment = comment;
						refresh();
					} else {
						state.textContent = message_of(res.data) || __("Feedback could not be saved.");
					}
				})
				.catch(function () {
					sending = false;
					state.textContent = __("Feedback could not be saved.");
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

	// ---- calls to ask / feedback and their errors ------------------------------------------------------------------
	// A plain POST rather than frappe.call: Frappe's own handler turns a 403/429 into a pop-up and hides the message
	// from the caller, and the panel has to show it. Same CSRF header, same endpoints, same cookies.

	function message_of(data) {
		try {
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

	function post(method, args, signal) {
		return fetch("/api/method/" + method, {
			method: "POST",
			credentials: "same-origin",
			signal: signal,
			headers: {
				"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
				Accept: "application/json",
				"X-Frappe-CSRF-Token": frappe.csrf_token,
			},
			body: new URLSearchParams(args).toString(),
		}).then(function (res) {
			return res.text().then(function (text) {
				let data = {};
				try {
					data = JSON.parse(text);
				} catch (e) {
					/* not JSON */
				}
				return { ok: res.ok, status: res.status, data: data };
			});
		});
	}

	function server_message(xhr) {
		try {
			return message_of(xhr && (xhr.responseJSON || JSON.parse(xhr.responseText)));
		} catch (e) {
			return "";
		}
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
		const abort = new AbortController();
		const finish = () => {
			finished = true;
			clearTimeout(timer);
			set_busy(false);
			ui.input.focus();
		};
		const timer = setTimeout(function () {
			if (finished) return;
			request_id++; // a late answer is ignored
			abort.abort();
			finish();
			add_line(
				"error",
				conversation
					? __("The advisor took too long. The answer may still have been saved: open History.")
					: __("The advisor took too long. The answer may still have been saved: open History. Your next question starts a new conversation.")
			);
		}, CLIENT_TIMEOUT_MS);

		post(ASK, args, abort.signal)
			.then(function (res) {
				if (finished || my_request !== request_id) return;
				finish();
				if (res.ok && res.data.message) {
					conversation = res.data.message.conversation;
					add_answer(res.data.message);
				} else {
					add_line("error", message_of(res.data) || __("The assistant could not answer."));
				}
			})
			.catch(function () {
				if (finished || my_request !== request_id) return;
				finish();
				add_line("error", __("The assistant could not be reached."));
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

	// "Saved as" only for a finding that still exists AND was saved from this very message (a deleted finding, or a reused name
	// that now belongs to another message, shows the button again, M6-R3). If the check fails the link is not trusted.
	function verify_findings(rows, done) {
		const linked = rows.filter((row) => row.finding);
		if (!linked.length) return done();
		frappe.call({
			method: LIST,
			type: "GET",
			args: {
				doctype: FINDING,
				filters: { name: ["in", linked.map((row) => row.finding)], source_message: ["in", linked.map((row) => row.name)] },
				fields: ["name", "source_message"],
				limit_page_length: linked.length,
			},
			callback: function (r) {
				const ok = new Set(((r && r.message) || []).map((f) => f.name + "|" + f.source_message));
				for (const row of linked) if (!ok.has(row.finding + "|" + row.name)) row.finding = "";
				done();
			},
			error: function () {
				for (const row of linked) row.finding = "";
				done();
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
				fields: ["name", "question", "answer", "status", "depth", "deep", "feedback", "feedback_comment", "route", "creation", "finding_suggestion", "finding"],
				order_by: "creation desc",
				limit_page_length: MESSAGE_CAP,
			},
			callback: function (r) {
				const rows = ((r && r.message) || []).slice().reverse();
				verify_findings(rows, () => {
					conversation = name;
					ui.log.replaceChildren();
					show_view("chat");
					if (rows.length >= MESSAGE_CAP) add_line("note", __("Older messages are not shown."));
					for (const row of rows) {
						add_line("user", row.question || "");
						add_answer({ message: row.name, answer: row.answer || "", status: row.status, feedback: row.feedback, feedback_comment: row.feedback_comment, finding_suggestion: row.finding_suggestion, finding: row.finding });
					}
				});
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
		if (ui.button) {
			ui.button.setAttribute("aria-expanded", show ? "true" : "false");
			ui.button.classList.toggle("ast-fab-open", !!show);
			// Swap the icons with the hidden attribute so only one is ever laid out, whatever stylesheet is loaded.
			if (ui.chat_svg) ui.chat_svg.toggleAttribute("hidden", !!show);
			if (ui.close_svg) ui.close_svg.toggleAttribute("hidden", !show);
		}
		if (show) {
			update_chip(false);
			ui.input.focus();
		}
	}

	// Icons are built with createElementNS and attribute calls only (no markup strings).
	function fab_icon(kind, className) {
		const NS = "http://www.w3.org/2000/svg";
		const svg = document.createElementNS(NS, "svg");
		const attrs = { viewBox: "0 0 24 24", width: "26", height: "26", fill: "none", stroke: "#fff", "stroke-width": "2", "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true", focusable: "false", class: className };
		for (const k of Object.keys(attrs)) svg.setAttribute(k, attrs[k]);
		const path = document.createElementNS(NS, "path");
		path.setAttribute("d", kind === "chat" ? "M21 11.5a8.4 8.4 0 0 1-8.5 8.3 8.7 8.7 0 0 1-3.6-.8L3 21l1.9-5.1A8.2 8.2 0 0 1 4 11.5 8.4 8.4 0 0 1 12.5 3.2 8.4 8.4 0 0 1 21 11.5z" : "M6 6l12 12M18 6L6 18");
		svg.appendChild(path);
		return svg;
	}

	function build() {
		read_prefs();
		ui.button = el("button", "ast-fab");
		ui.button.type = "button";
		ui.button.title = __("Ask the Lending Assistant");
		ui.button.setAttribute("aria-label", __("Ask the Lending Assistant"));
		ui.button.setAttribute("aria-expanded", "false");
		ui.chat_svg = fab_icon("chat", "ast-fab-chat");
		ui.close_svg = fab_icon("close", "ast-fab-x");
		ui.close_svg.setAttribute("hidden", "");
		ui.button.append(ui.chat_svg, ui.close_svg);
		ui.button.addEventListener("click", () => toggle());

		ui.panel = el("div", "ast-panel");
		ui.panel.hidden = true;
		// One document-level Esc handler: closes the open panel wherever focus is, but leaves Esc to an open Frappe dialog.
		document.addEventListener("keydown", function (e) {
			if (e.key !== "Escape" || ui.panel.hidden || document.querySelector(".modal.show")) return;
			toggle(false);
			ui.button.focus();
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
