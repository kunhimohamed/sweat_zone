
import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def fetch_specified_trainer(doctype, txt, searchfield, start, page_len, filters):
	
	selected_plan = filters.get("selected_plan")
	if selected_plan:
		return frappe.get_all(
			"Trainer Subscription Plans",
			filters={"trainer_subscription_plan": selected_plan, "parenttype": "Gym Trainer"},
			fields=["parent"],
			as_list=1,
		)