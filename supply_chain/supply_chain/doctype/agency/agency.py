# Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Agency(Document):
	
	def validate(self):
		if self.get("__islocal") and len(self.items) > 0 and not self.is_active:
			frappe.throw("Agency needs to be active to link items")
			
		if not self.get("__islocal"):
			old_status = self.get_doc_before_save().is_active
			frappe.log_error("Old Status", str(old_status))
			if old_status == 0 and not self.is_active and len(self.items) > 0:
				frappe.throw(f"Cannot add items to inactive agency <b>{self.agency_name}</b>")

		if self.name and not self.is_active and len(self.items) > 0:
			frappe.log_error("Doc",self.as_dict())
			frappe.throw(f"Cannot deactivate {self.agency_name} as this agency has linked items")
	
	@frappe.whitelist()
	def create_supplier(self):
		existing_supplier = frappe.db.exists("Supplier", {"name" : self.agency_name})
		if existing_supplier:
			return{
				"status" : 'Exists',
				"message" : existing_supplier
			}
		supplier = frappe.get_doc({
			"doctype":"Supplier",
			"supplier_name": self.agency_name,
		}).insert()
		contact = create_contact(supplier.name,self.email_id,self.phone)
		frappe.db.set_value("Supplier", supplier.name, "supplier_primary_contact", contact)
		self.supplier = supplier.name
		self.save()
		return {
			"status" : "Success",
			"message" : supplier.name
		}

def create_contact(supplier_name, email, phone):
	contact = frappe.get_doc({
		"doctype": "Contact",
		"first_name" : supplier_name,
		"email_ids":[{
			"email_id": email,
			"is_primary": 1
		}],
		"phone_nos":[{
			"phone": phone,
			"is_primary_phone": 1
		}],
		"links":[{
			"link_doctype": "Supplier",
			"link_name": supplier_name
		}],
		"is_primary_contact" : 1
	}).insert()
	return contact.name
