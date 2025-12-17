// Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
// For license information, please see license.txt

frappe.query_reports["Agency Lead Times"] = {
	"filters": [
		{
			"fieldname" : "agency",
			"label" : __("Agency"),
			"fieldtype": "Link",
			"options": "Agency",
			"width": "250"
		},
		{
			"fieldname" : "item_code",
			"label" : __("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
			"width": "250"
		},
		{
			"fieldname" : 'lead_time',
			"label" : __('Lead Time (Days) <='),
			"fieldtype": 'Int',
			"width": "150"
		}
	]
};
