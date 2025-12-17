// Copyright (c) 2025, with validations, reports, and APIs.Jaffar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agency", {
	refresh(frm) {
        if(!frm.doc._islocal && frm.doc.is_active && !frm.doc.supplier){
            frm.add_custom_button(("Create Supplier"),function(){
                frappe.call({
                    doc:frm.doc,
                    method:"create_supplier",
                    freeze:true,
                    async:false,
                    freeze_message:__("Creating Supplier..."),
                    callback(r){
                        if(r.message && r.message.status == "Success"){
                            frappe.msgprint(__("Supplier {0} created successfully.",[r.message.message]))
                        }
                        else if(r.message && r.message.status == "Exists"){
                            frappe.msgprint(__("Supplier {0} already exists.",[r.message.message]))
                        }
                    }
                })
            })
        }
	},
});
