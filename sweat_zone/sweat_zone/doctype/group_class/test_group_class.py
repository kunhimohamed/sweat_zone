# Copyright (c) 2022, kunhimohamed6@gmail.com and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

def create_group_class():
	if frappe.flags.test_events_created:
		return

	frappe.set_user("Administrator")
	doc = frappe.get_doc({
		"doctype": "Group Class",
		"class_name":"Test Class 1",
		"description": "Test Class 1 description"
	}).insert()

	doc = frappe.get_doc({
		"doctype": "Group Class",
		"class_name":"Test Class 2",
		"description": "Test Class 2 description"
	}).insert()

	frappe.flags.test_events_created = True

class TestGroupClass(FrappeTestCase):
	def setUp(self):
		create_group_class()
