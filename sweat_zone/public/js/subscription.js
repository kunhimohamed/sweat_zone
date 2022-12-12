
frappe.ui.form.on("Subscription", {	
	refresh: function(frm) {
        frappe.db.get_value('Gym Subscription Settings', 'Gym Subscription Settings', ['follow_calendar_months'])
            .then(gym_settings_record => {
                frm.set_value("follow_calendar_months", gym_settings_record.message.follow_calendar_months);
                frm.set_value("generate_new_invoices_past_due_date", gym_settings_record.message.generate_new_invoices_past_due_date);
                frm.set_value("cancel_at_period_end", gym_settings_record.message.cancel_at_end_of_period);
                frm.set_value("generate_invoice_at_period_start", gym_settings_record.message.generate_invoice_at_beginning_of_period);
                frm.refresh_field("follow_calendar_months");
        });
	}
});