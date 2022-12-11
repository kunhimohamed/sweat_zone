# Copyright (c) 2022, kunhimohamed6@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import get_date_str
import datetime

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	chart = get_chart_data(filters, data)
	message = "Workout on date"
	return columns, data, message, chart

def get_columns(filters):
	
	columns = [
		{
			"fieldname": "date",
			"label": _("Date"),
			"fieldtype": "date",
			"hidden": 0
		},
		{
			"fieldname": "calories_intake",
			"label": _("Calories Intake"),
			"fieldtype": "calories_intake",
			"hidden": 0
		},
		{
			"fieldname": "workout_hours",
			"label": _("Workout Hours"),
			"fieldtype": "workout_hours",
			"hidden": 0
		}
	]

	return columns

def get_data(filters):
	data = frappe.get_all("Track Customer Fitness", fields=["calories_intake", "workout_hours", "date"] , filters={"parent":filters.user})
	return data

def get_chart_data(filters, data):
	data_set = []
	for each in data:
		data_set.append({"name":get_date_str(each.date), "values":[each.workout_hours]})
	chart = {"data": {"labels": ["Work Out"], "datasets": data_set}}
	chart["type"] = "bar"
	return chart