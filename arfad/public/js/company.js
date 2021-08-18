frappe.ui.form.on("Company", {
	setup: function(frm) {
		frm.set_query("default_vat_tax_account_cf", function() {
			return { filters: { account_type: 'tax' ,company:frm.doc.name} };
		});
		frm.set_query("default_employee_petty_cash_payable_account_cf", function() {
			return { filters: { account_type: 'payable' ,company:frm.doc.name} };
		});		
	}
})