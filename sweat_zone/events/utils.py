
import frappe
from erpnext.portal.utils import party_exists, get_debtors_account
from frappe.utils.nestedset import get_root_of
from erpnext.e_commerce.doctype.e_commerce_settings.e_commerce_settings import (
	get_shopping_cart_settings,
)


def custom_create_customer_or_supplier():
	"""Based on the default Role (Customer, Supplier), create a Customer / Supplier.
	Called on_session_creation hook.
	"""
	user = frappe.session.user

	user_roles = frappe.get_roles()

	if (frappe.db.get_value("User", user, "user_type") != "Website User") and ("Gym Member" not in user_roles):
		return

	
	portal_settings = frappe.get_single("Portal Settings")
	default_role = portal_settings.default_role

	if default_role not in ["Customer", "Supplier"]:
		return

	# create customer / supplier if the user has that role
	if portal_settings.default_role and portal_settings.default_role in user_roles:
		doctype = portal_settings.default_role
	else:
		doctype = None

	if not doctype:
		return

	if party_exists(doctype, user):
		return

	party = frappe.new_doc(doctype)
	fullname = frappe.utils.get_fullname(user)

	if doctype == "Customer":
		cart_settings = get_shopping_cart_settings()

		if cart_settings.enable_checkout:
			debtors_account = get_debtors_account(cart_settings)
		else:
			debtors_account = ""

		party.update(
			{
				"customer_name": fullname,
				"customer_type": "Individual",
				"customer_group": cart_settings.default_customer_group,
				"territory": get_root_of("Territory"),
			}
		)

		if debtors_account:
			party.update({"accounts": [{"company": cart_settings.company, "account": debtors_account}]})
	else:
		party.update(
			{
				"supplier_name": fullname,
				"supplier_group": "All Supplier Groups",
				"supplier_type": "Individual",
			}
		)

	party.flags.ignore_mandatory = True
	party.insert(ignore_permissions=True)

	alternate_doctype = "Customer" if doctype == "Supplier" else "Supplier"

	if party_exists(alternate_doctype, user):
		# if user is both customer and supplier, alter fullname to avoid contact name duplication
		fullname += "-" + doctype

	create_party_contact(doctype, fullname, user, party.name)

	return party


def create_party_contact(doctype, fullname, user, party_name):
	contact = frappe.new_doc("Contact")
	contact.update({"first_name": fullname, "email_id": user})
	contact.append("links", dict(link_doctype=doctype, link_name=party_name))
	contact.append("email_ids", dict(email_id=user, is_primary=1))
	contact.flags.ignore_mandatory = True
	contact.insert(ignore_permissions=True)