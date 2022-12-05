frappe.ui.form.on("Customer", {
	setup: function (frm) {

	  frm.set_query("trainer", function (doc) {
		return {
              filters: {
                value: row.item_code,
                apply_on: "Item Code",
              }
		};
	  });


	},
});