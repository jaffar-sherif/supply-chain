import frappe

def set_default_item_code(doc, method= None):
    if not doc.manufacturer_part_no:
        doc.manufacturer_part_no = doc.item_code

def validate_duplicate_manufacturer(doc, method = None):
    # Check duplicate manufacturer for the same item code and manufacturer
    # As core ERPNext does the restriction with combination of item code , manufacturer and manufacturer part no
    existing = frappe.get_all("Item Manufacturer", filters={
        "item_code": doc.item_code,
        "manufacturer": doc.manufacturer,
        "name": ["!=", doc.name]
    })
    if existing:
        frappe.throw("Duplicate entry against the item code {0} and manufacturer {1}".format(doc.item_code, doc.manufacturer))


def validate_blocked_manufacturer(doc, method  = None):
    is_blocked = frappe.db.get_value("Manufacturer", doc.manufacturer, "custom_is_blocked")
    if is_blocked:
        frappe.throw(f"Manufacturer {doc.manufacturer} is marked as blocked and cannot be linked to Item Manufacturer.")