
frappe.ui.form.on("Customer", {
	setup: function (frm) {
		frm.set_query("trainer", function (doc) {
			return {
				query: 'sweat_zone.events.customer.fetch_specified_trainer',
				filters: {
					selected_plan: frm.doc.subscription_plan
				}
			};
		});
	},
	subscription_plan: function(frm) {
		if(frm.doc.subscription_plan){
			frm.toggle_reqd(["trainer", "from_date", "to_date"], true);
		}
		else{
			frm.toggle_reqd(["trainer", "from_date", "to_date"], false);
		}
	},
	refresh: function(frm) {
		if(frm.doc.__islocal!=1){
			frm.toggle_display("subscriptions", true);
		}
		else{
			frm.toggle_display("subscriptions", false);
		}
	}
});