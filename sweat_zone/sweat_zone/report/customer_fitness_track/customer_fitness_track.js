// Copyright (c) 2022, kunhimohamed6@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Customer Fitness Track"] = {
	"filters": [
		{
			"fieldname": "user",
			"label": __("User"),
			"fieldtype": "Link",
			"options": "User",
			"reqd": 1
		}
	]
};
