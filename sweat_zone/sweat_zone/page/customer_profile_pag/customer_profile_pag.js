

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
   $(frappe.render_template("customer_profile_pag", {"test":"temp"})).appendTo(this.page.main);
}
})