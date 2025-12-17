import frappe

@frappe.whitelist()
def get_manufacturers_by_item(item_code):    
    try:
        if not item_code:
            return {'status' : 'Error', 'message' : 'Item Code is required.'}
        data = {'item_code' : item_code, 'manufacturers' : []}
        if not frappe.db.exists("Item", item_code):
            return {'status' : 'Error', 'message' : f'Item {item_code} does not exist.'}
        manufacturers = frappe.get_all(
            "Item Manufacturer",
            filters = {"item_code" : item_code},
            fields = ['manufacturer', 'manufacturer_part_no','custom_gtin']
        )
        for m in manufacturers:
            data['manufacturers'].append(m)
        data['status'] = 'Success'
        return data
    except Exception as e:
        frappe.log_error("Get Manufacturers by Item API",frappe.get_traceback())
        return {'status' : 'Error', 'message' : frappe.get_traceback()}
