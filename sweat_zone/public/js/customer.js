
frappe.ui.form.on("Customer", {
	setup: function (frm) {
		frm.set_query("locker", function (doc) {
			// let root_store_room = root_store_room
			return {
				query: "sweat_zone.events.customer.fetch_available_locker"
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