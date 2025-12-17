# Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label" : "Manufacturer",
			"fieldname" : "manufacturer",
			"fieldtype" : "Link",
			"options" : "Manufacturer",
			"width" : 200
		},
		{
			"label" : "Item Code",
			"fieldname" : "item_code",
			"fieldtype" : "Link",
			"options" : "Item",
			"width" : 200
		},
		{
			"label" : "Manufacturer Part No",
			"fieldname" : "manufacturer_part_no",
			"fieldtype" : "Data",
			"width" : 200
		},
		{
			"label" : "Custom GTIN",
			"fieldname" : "custom_gtin",
			"fieldtype" : "Data",
			"width" : 150
		}
	]

def get_data(filters):
	conditions = ""
	filter_data = {}

	if filters.get("manufacturer"):
		conditions += " AND itm.manufacturer = %(manufacturer)s"
		filter_data['manufacturer'] = filters.get("manufacturer")
	
	if filters.get("item_code"):
		conditions += " AND itm.item_code = %(item_code)s"
		filter_data['item_code'] = filters.get("item_code")

	qry = """
		SELECT
			itm.manufacturer,
			itm.item_code,
			itm.manufacturer_part_no,
			itm.custom_gtin
		FROM
			`tabItem Manufacturer` itm
		WHERE 
			1 = 1
		""" + conditions
	data = frappe.db.sql(qry, filter_data, as_dict=1)
	return data