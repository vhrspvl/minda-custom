// Copyright (c) 2018, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Contractor Invoice', {
	contractor: function(frm) {
			frappe.call({
				method:"minda_custom.minda_custom.doctype.contractor_invoice.contractor_invoice.get_mandays",
				args:{
					"start_date":frm.doc.start_date,
					"contractor":frm.doc.contractor
				},
				freeze: true,
				freeze_message: __("Fetching"),
				callback:function(r) {
                        // console.log(r)
                        frm.set_value("total_manheads",r.message[0])
						frm.set_value("total_mandays",r.message[1][15])
						frm.set_value("basic",r.message[1][0])
						frm.set_value("da",r.message[1][1])
						frm.set_value("basic_da",r.message[1][3])
						frm.set_value("other_allowance",r.message[1][2])
                        frm.set_value("esic",r.message[1][4])
						frm.set_value("pf",r.message[1][5])
						frm.set_value("service_charge",r.message[1][7])
                        frm.set_value("ot_wages",r.message[1][8])
                        frm.set_value("ot_esic",r.message[1][9])
                        frm.set_value("ot_service_charge",r.message[1][10])
                        frm.set_value("gross",r.message[1][6])
                        frm.set_value("total",r.message[1][11])
                        frm.set_value("sgst",r.message[1][12])
                        frm.set_value("cgst",r.message[1][13])
                        // frm.set_df_property('cgst','read_only',1)
                        frm.set_value("sub_total",r.message[1][14])
                        frm.set_value("canteen",r.message[1][16])
                        frm.set_value("line_leader",r.message[1][18])
                        frm.set_value("gross_pay",r.message[1][17])

				}
				
			})

	}
});
