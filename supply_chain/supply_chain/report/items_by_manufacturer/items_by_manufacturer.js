// Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
// For license information, please see license.txt

frappe.query_reports["Items by Manufacturer"] = {
	"filters": [
		{
			"fieldname" : "manufacturer",
			"label" : __("Manufacturer"),
			"fieldtype": "Link",
			"options": "Manufacturer",
			"width": "250"
		},
		{
			"fieldname" : "item_code",
			"label" : __("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
			"width": "250"
		}
	]
};
