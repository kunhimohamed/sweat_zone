// Copyright (c) 2022, kunhimohamed6@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Feedback', {
	refresh: function(frm) {
		frm.set_value("user", frappe.session.user);
		frm.refresh_field("user");
	}
});
