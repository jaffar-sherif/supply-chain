# Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return[
		{
			"label" : "Agency",
			"fieldname" : "agency",
			"fieldtype" : "Link",
			"options" : "Agency",
			"width" : 200
		},
		{
			"label" : "Item",
			"fieldname" : "item_code",
			"fieldtype" : "Link",
			"options" : "Item",
			"width" : 200
		},
		{
			"label" : "Min Order Qty",
			"fieldname" : "min_order_qty",
			"fieldtype" : "Int",
			"width" : 150
		},
		{
			"label" : "Lead Time (In Days)",
			"fieldname" : "lead_time",
			"fieldtype" : "Int",
			"width" : 150
		}
	]

def get_data(filters):
	conditions = ""
	filter_data = {}
	if filters.get("agency"):
		conditions += " AND ag.name = %(agency_name)s"
		filter_data["agency_name"] = filters.get("agency")
	
	if filters.get("item_code"):
		conditions += " AND agc.item_code = %(item_code)s"
		filter_data["item_code"] = filters.get("item_code")
	
	if filters.get("lead_time"):
		conditions += " AND agc.lead_time_days <= %(lead_time)s"
		filter_data['lead_time'] = filters.get("lead_time")
	
	qry = """
			SELECT ag.agency_name as agency, agc.item_code, agc.min_order_qty, agc.lead_time_days as lead_time
				FROM
					`tabAgency` ag
				INNER JOIN
					`tabAgency Item` agc
				ON
					ag.name = agc.parent
			WHERE
				1 = 1
		"""+ conditions
	frappe.log_error("Filter Data", str(filter_data))
	frappe.log_error("Qry", qry)
	data = frappe.db.sql(qry,filter_data ,as_dict = 1)
	return data