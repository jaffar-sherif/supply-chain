frappe.listview_settings["Agency"] = {
    get_indicator: function(doc) {
            if (!doc.is_active) {
                return [__('Inactive'), 'red', 'is_active,=,0'];
            }
            return [__('Active'), 'green', 'is_active,=,1'];
        },

        // Add this for row styling
    formatters: {
        // Style the agency_name column
        agency_name: function(value, df, doc) {
            let html = value;
            
            // If inactive, wrap in red styling
            if (doc.is_active === 0) {
                html = `<span style="color: white; background-color: #d32f2f; padding: 5px 10px; border-radius: 3px; font-weight: bold;">
                    ${value}
                </span>`;
            }
            
            return html;
        }
    },

}