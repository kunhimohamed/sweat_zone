# Copyright (c) 2022, kunhimohamed6@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = get_column(filters)
	data = get_data(filters)
	return columns, data

def get_column(filters):
	return	[
		{
			"fieldname": "group_class",
			"label": _("Group Class"),
			"fieldtype": "Link",
			"options": "Group Class"
		},
		{
			"fieldname": "count_group_class",
			"label": _("Count Group Class"),
			"fieldtype": "Data"
		}
	]

def get_data(filters):
	return frappe.db.sql("""
		select 
			tgcbd.group_class, count(tgcbd.group_class) as count_group_class
		from 
			`tabGroup Class Book Detail` tgcbd
		group by 
			tgcbd.group_class;
	""", as_dict=1)