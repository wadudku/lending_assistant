// Assistant Finding list: status indicator and "Export to Markdown" (selected rows, or the current filter, at most 200).
// Reads go through frappe.client.get_list, so the user's permissions apply; no new server method.
(function () {
	const FIELDS = ["name", "title", "status", "owner", "creation", "br_ids", "doctypes", "sources", "cards_used", "cards_basis", "lending_version", "author_name", "confirmed_by", "confirmed_on", "question", "summary"];
	const CAP = 200;

	function one_line(text) {
		return String(text || "").replace(/\s+/g, " ").trim();
	}

	function listing(text) {
		return String(text || "").split("\n").map(one_line).filter(Boolean).join(", ");
	}

	function parse(text) {
		try {
			const v = JSON.parse(text || "[]");
			return Array.isArray(v) ? v : [];
		} catch (e) {
			return [];
		}
	}

	function who(row) {
		return row.author_name || frappe.user.full_name(row.owner) || "";
	}

	function block(row) {
		const cards = parse(row.cards_used).map((c) => one_line(c.id) + " v" + one_line(c.version)).join(", ");
		const confirmed = row.status === "Confirmed" ? " (by " + one_line(frappe.user.full_name(row.confirmed_by) || row.confirmed_by) + " on " + one_line(row.confirmed_on) + ")" : "";
		return [
			"## " + row.name + ": " + one_line(row.title),
			"",
			"- Status: " + row.status + confirmed,
			"- Author: " + one_line(who(row)) + "   Date: " + String(row.creation || "").slice(0, 10) + "   Lending version: " + one_line(row.lending_version),
			"- BR ids: " + listing(row.br_ids),
			"- Doctypes: " + listing(row.doctypes),
			"- Sources: " + parse(row.sources).map(one_line).join(", "),
			"- Cards: " + cards + (row.cards_basis ? " (" + one_line(row.cards_basis) + ")" : ""),
			"- Question: " + one_line(row.question),
			"",
			String(row.summary || "").split("\n").map((line) => "> " + line).join("\n"),
			"",
		].join("\n");
	}

	function download(text) {
		const blob = new Blob([text], { type: "text/markdown;charset=utf-8" });
		const link = document.createElement("a");
		link.href = URL.createObjectURL(blob);
		link.download = "assistant-findings-" + frappe.datetime.get_today() + ".md";
		document.body.appendChild(link);
		link.click();
		link.remove();
		setTimeout(() => URL.revokeObjectURL(link.href), 1000);
	}

	function export_markdown(listview) {
		const names = listview.get_checked_items(true);
		const filters = names.length ? [["name", "in", names]] : listview.get_filters_for_args();
		frappe.call({
			method: "frappe.client.get_list",
			type: "GET",
			args: { doctype: "Assistant Finding", filters: filters, fields: FIELDS, order_by: "creation desc", limit_page_length: CAP },
			callback: function (r) {
				const rows = (r && r.message) || [];
				if (!rows.length) {
					frappe.show_alert({ message: __("Nothing to export."), indicator: "orange" });
					return;
				}
				const head = "# Assistant findings\n\nExported " + frappe.datetime.get_today() + ". " + rows.length + " finding(s)." + (rows.length >= CAP ? " Only the first " + CAP + " are included." : "") + "\n\n";
				download(head + rows.map(block).join("\n"));
			},
		});
	}

	frappe.listview_settings["Assistant Finding"] = {
		add_fields: ["status"],
		get_indicator: (doc) => [__(doc.status), doc.status === "Confirmed" ? "green" : "gray", "status,=," + doc.status],
		onload: function (listview) {
			// the inner button is hidden on narrow screens, so the same action is also in the Menu
			listview.page.add_inner_button(__("Export to Markdown"), () => export_markdown(listview));
			listview.page.add_menu_item(__("Export to Markdown"), () => export_markdown(listview), true);
		},
	};
})();
