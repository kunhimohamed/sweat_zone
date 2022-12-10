
import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def fetch_available_locker(doctype, txt, searchfield, start, page_len, filters):
	"""
	Select locker which is not reserved by any customer
	"""
	root_locker = frappe.db.get_value("Gym Subscription Settings", "Gym Subscription Settings", "root_store_room")
	if root_locker:
		return frappe.get_all(
			"Locker",
			filters={"customer": "", "is_group": 0, "name": ["!=", root_locker]},
			fields=["name"],
			as_list=1,
		)

def check_and_book_locker(doc, handler=None):
	"""
	check then book the locker for the customer
	"""
	if frappe.db.exists("Locker", {"customer": doc.name}):
		if not doc.disabled:
			frappe.throw("You already have a locker!")
		else:
			doc.locker = None
			lockers = frappe.get_list("Locker", fields=["name"], filters={"customer": doc.name})
			if lockers:
				for locker in lockers:
					frappe.db.set_value("Locker", locker.name, "Customer", "")
					frappe.db.commit()
	else:		
		if not doc.disabled:
			if doc.locker:
				frappe.db.set_value("Locker", doc.locker, "customer", doc.name)
				frappe.db.commit()
		else:
			doc.locker = None

@frappe.whitelist()
def fetch_customer_subscription_details(user=None):
	"""
	fetch customer subscription details for display in page
	"""
	if not user:
		user = frappe.session.user
		customer = party_exists_then_return(user)
		if customer:
			subscription_detail = frappe.db.sql("""
					select 
						ts.name, ts.start_date, ts.end_date, tspd.plan, tspd.gym_trainer  from tabSubscription ts 
					join 
						`tabSubscription Plan Detail` tspd on tspd.parent = ts.name
					where 
						ts.party = "{customer}";
			""".format(customer = customer), as_dict=1);
			return subscription_detail

def party_exists_then_return(user):
	# check if contact exists against party and if it is linked to the doctype
	contact_name = frappe.db.get_value("Contact", {"email_id": user})
	if contact_name:
		contact = frappe.get_doc("Contact", contact_name)
		for contact_link in contact.links:
			if contact_link.link_doctype == "Customer":
				return contact_link.link_name