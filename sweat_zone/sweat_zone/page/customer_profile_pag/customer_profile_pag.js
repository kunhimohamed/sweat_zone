

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
   // frappe.call('erpnext.manufacturing.doctype.bom.bom.get_bom_diff', {
   //    bom1: name1,
   //    bom2: name2
   // }).then(r => {
   //    let diff = r.message;
   //    frappe.model.with_doctype('BOM', () => {
   //       this.render('BOM', name1, name2, diff);
   //    });
   // });
   $(frappe.render_template("customer_profile_pag", {"test":"temp"})).appendTo(this.page.main);
}
})