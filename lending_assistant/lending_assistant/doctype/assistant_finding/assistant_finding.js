// Assistant Finding form. Only static text and escaped ids are shown (no server text as markup).
frappe.ui.form.on("Assistant Finding", {
	refresh(frm) {
		const reasons = (frm.doc.__onload && frm.doc.__onload.stale_reasons) || [];
		if (reasons.length) {
			const text = __("Check again: the analysis this finding relied on has changed.") + " " + reasons.map((r) => frappe.utils.escape_html(r)).join("; ");
			frm.dashboard.set_headline_alert(text, "orange");
		}
		const name = frm.doc.source_message;
		if (name && /^[A-Za-z0-9_-]+$/.test(name)) {
			const link = document.createElement("a");
			link.href = frappe.utils.get_form_link("Assistant Message", name);
			link.textContent = name;
			link.target = "_blank";
			link.rel = "noopener noreferrer";
			const area = frm.fields_dict.source_message.$wrapper.find(".control-value, .like-disabled-input").first();
			if (area.length) area[0].replaceChildren(link);
		}
	},
});
