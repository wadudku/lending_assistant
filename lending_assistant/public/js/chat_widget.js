// Lending Assistant chat widget (M1 stub).
// Server text is only ever put on the page with textContent: never as markup.
// Markdown rendering and sanitising arrive in M5.
frappe.provide("lending_assistant");

(function () {
	"use strict";

	const ROLE = "Assistant User";
	const METHOD = "lending_assistant.api.chat.ask";

	let built = false;
	let conversation = null;
	let ui = {};

	function el(tag, className, text) {
		const node = document.createElement(tag);
		if (className) node.className = className;
		if (text !== undefined) node.textContent = text;
		return node;
	}

	function add_line(kind, text) {
		const line = el("div", "ast-line ast-" + kind, text);
		ui.log.appendChild(line);
		ui.log.scrollTop = ui.log.scrollHeight;
	}

	function set_busy(busy) {
		ui.send.disabled = busy;
		ui.input.disabled = busy;
	}

	function send() {
		const question = ui.input.value.trim();
		if (!question) return;

		add_line("user", question);
		ui.input.value = "";
		set_busy(true);

		const args = { question: question, route: frappe.get_route_str(), depth: "Both" };
		if (conversation) args.conversation = conversation;

		frappe.call({
			method: METHOD,
			type: "POST",
			args: args,
			callback: function (r) {
				set_busy(false);
				if (r && r.message) {
					conversation = r.message.conversation;
					add_line("assistant", r.message.answer);
				}
			},
			error: function () {
				set_busy(false);
				add_line("error", __("The assistant could not answer. See the message at the top of the page."));
			},
		});
		ui.input.focus();
	}

	function toggle(open) {
		const show = open === undefined ? ui.panel.hidden : open;
		ui.panel.hidden = !show;
		if (show) ui.input.focus();
	}

	function build() {
		ui.button = el("button", "ast-fab", __("Ask"));
		ui.button.type = "button";
		ui.button.title = __("Lending Assistant");
		ui.button.addEventListener("click", function () {
			toggle();
		});

		ui.panel = el("div", "ast-panel");
		ui.panel.hidden = true;

		const header = el("div", "ast-header");
		header.appendChild(el("span", "ast-title", __("Lending Assistant")));
		const close = el("button", "ast-close", "×");
		close.type = "button";
		close.addEventListener("click", function () {
			toggle(false);
		});
		header.appendChild(close);

		ui.log = el("div", "ast-log");
		const form = el("div", "ast-form");
		ui.input = el("textarea", "ast-input");
		ui.input.rows = 2;
		ui.input.maxLength = 4000;
		ui.input.placeholder = __("Ask a question");
		ui.input.addEventListener("keydown", function (e) {
			if (e.key === "Enter" && !e.shiftKey) {
				e.preventDefault();
				send();
			}
		});
		ui.send = el("button", "ast-send", __("Send"));
		ui.send.type = "button";
		ui.send.addEventListener("click", send);
		form.appendChild(ui.input);
		form.appendChild(ui.send);

		ui.panel.appendChild(header);
		ui.panel.appendChild(ui.log);
		ui.panel.appendChild(form);
		document.body.appendChild(ui.button);
		document.body.appendChild(ui.panel);
	}

	function init() {
		if (built) return;
		if (!frappe.user || !frappe.user.has_role(ROLE)) return;
		built = true;
		build();
	}

	$(document).on("startup", init);
})();
