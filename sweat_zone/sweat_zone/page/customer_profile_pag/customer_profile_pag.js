

frappe.pages['customer-profile-pag'].on_page_load = function(wrapper) {
	new profile_pag(wrapper);
}

profile_pag = Class.extend({
init: function(wrapper) {
   this.page = frappe.ui.make_app_page({
	   parent: wrapper,
	   title: 'Profile Page',
	   single_column: true
   });
   this.make();
},
make: function() {
   frappe.call('sweat_zone.events.customer.fetch_customer_subscription_details').then(r => {
      if (r.message){
         console.log(r.message);
         $(frappe.render_template("customer_profile_pag", {"test":r.message, "array_length":r.message.length})).appendTo(this.page.main);
      }
      else{
         $(frappe.render_template("customer_profile_pag", {"test":[], "array_length":r.message.length})).appendTo(this.page.main);
      }
   });
   
}
})