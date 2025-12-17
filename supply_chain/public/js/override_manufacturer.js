frappe.ui.form.on("Item Manufacturer", {
    refresh(frm){
        frm.set_query("manufacturer", function(){
            return{
                "filters" : {
                    "custom_is_blocked" : 0
                }
            }
        })
    }
})