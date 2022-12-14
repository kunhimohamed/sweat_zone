# Copyright (c) 2022, kunhimohamed6@gmail.com and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

def create_gym_trainer():
	if frappe.flags.test_events_created:
		return

	frappe.set_user("Administrator")
	doc = frappe.get_doc({
		"doctype": "Gym Trainer",
		"name1":"_Test Trainer 1",
		"phone": "36512",
		"email": "test@example.com"
	})
	row = doc.append("allowed_subscription_plans", {
		"trainer_subscription_plan": "Advanced Plan"
	})
	doc.insert()

	doc = frappe.get_doc({
		"doctype": "Gym Trainer",
		"name1":"_Test Trainer 2",
		"phone": "458967",
		"email": "test34ertd@example.com"
	})
	row = doc.append("allowed_subscription_plans", {
		"trainer_subscription_plan": "Beginer Plan"
	})
	doc.insert()

	frappe.flags.test_events_created = True


class TestGymTrainer(FrappeTestCase):
	def test_setUp(self):
		create_gym_trainer()
