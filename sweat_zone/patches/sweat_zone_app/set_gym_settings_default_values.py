
import frappe

def execute():
	frappe.db.set_value("Gym Subscription Settings", "Gym Subscription Settings" ,{
		"follow_calendar_months":1,
		"generate_new_invoices_past_due_date":1,
		"cancel_at_end_of_period":1,
		"generate_invoice_at_beginning_of_period":1,
		"submit_invoice_automatically":1
	})
	frappe.db.commit()
