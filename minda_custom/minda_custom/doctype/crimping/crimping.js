// Copyright (c) 2018, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Crimping",{
    employee_code:function(frm){
    frappe.call({
        method: 'frappe.client.get_value',
        args: {
            'doctype': 'Employee',
            'filters': {'employee_number': frm.doc.employee_code},
            'fieldname': [
                'employee_name','date_of_joining','line'
          ]
        },
        callback: function(r) {
        if (!r.exc) {
            frm.set_value("data_1",r.message.employee_name)
            frm.set_value("date_of_joining",r.message.date_of_joining)
            frm.set_value("line_name",r.message.line)
    
                // code snippet
            }
    
        }
    
    })
},
    after_save:function(frm){
        frm.trigger("onload_post_render");
    },
   'onload_post_render': function(frm) {
        $(cur_frm.fields_dict.ok.input).addClass('chb');
        $(cur_frm.fields_dict.partially_ok.input).addClass('chb');
        $(cur_frm.fields_dict.not_ok.input).addClass('chb');
        $(".chb").change(function() {
        $(".chb").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_1.input).addClass('chb1');
        $(cur_frm.fields_dict.partially_ok1.input).addClass('chb1');
        $(cur_frm.fields_dict.not_ok1.input).addClass('chb1');
        $(".chb1").change(function() {
        $(".chb1").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_2.input).addClass('chb2');
        $(cur_frm.fields_dict.partially_ok2.input).addClass('chb2');
        $(cur_frm.fields_dict.not_ok2.input).addClass('chb2');
        $(".chb2").change(function() {
        $(".chb2").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_3.input).addClass('chb3');
        $(cur_frm.fields_dict.partially_ok3.input).addClass('chb3');
        $(cur_frm.fields_dict.not_ok3.input).addClass('chb3');
        $(".chb3").change(function() {
        $(".chb3").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_4.input).addClass('chb4');
        $(cur_frm.fields_dict.partially_ok4.input).addClass('chb4');
        $(cur_frm.fields_dict.not_ok4.input).addClass('chb4');
        $(".chb4").change(function() {
        $(".chb4").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_5.input).addClass('chb5');
        $(cur_frm.fields_dict.partially_ok5.input).addClass('chb5');
        $(cur_frm.fields_dict.not_ok5.input).addClass('chb5');
        $(".chb5").change(function() {
        $(".chb5").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok6.input).addClass('chb6');
        $(cur_frm.fields_dict.partially_ok6.input).addClass('chb6');
        $(cur_frm.fields_dict.not_ok6.input).addClass('chb6');
        $(".chb6").change(function() {
        $(".chb6").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_14.input).addClass('chb7');
        $(cur_frm.fields_dict.partially_ok_14.input).addClass('chb7');
        $(cur_frm.fields_dict.not_ok_14.input).addClass('chb7');
        $(".chb7").change(function() {
        $(".chb7").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_15.input).addClass('chb8');
        $(cur_frm.fields_dict.partially_ok_15.input).addClass('chb8');
        $(cur_frm.fields_dict.not_ok_15.input).addClass('chb8');
        $(".chb8").change(function() {
        $(".chb8").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_16.input).addClass('chb9');
        $(cur_frm.fields_dict.partially_ok_16.input).addClass('chb9');
        $(cur_frm.fields_dict.not_ok_16.input).addClass('chb9');
        $(".chb9").change(function() {
        $(".chb9").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_17.input).addClass('chb10');
        $(cur_frm.fields_dict.partially_ok_17.input).addClass('chb10');
        $(cur_frm.fields_dict.not_ok_17.input).addClass('chb10');
        $(".chb10").change(function() {
        $(".chb10").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_18.input).addClass('chb11');
        $(cur_frm.fields_dict.partially_ok_118.input).addClass('chb11');
        $(cur_frm.fields_dict.not_ok_18.input).addClass('chb11');
        $(".chb11").change(function() {
        $(".chb11").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_19.input).addClass('chb12');
        $(cur_frm.fields_dict.partially_ok_19.input).addClass('chb12');
        $(cur_frm.fields_dict.not_ok_19.input).addClass('chb12');
        $(".chb12").change(function() {
        $(".chb12").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_20.input).addClass('chb13');
        $(cur_frm.fields_dict.partially_ok_20.input).addClass('chb13');
        $(cur_frm.fields_dict.not_ok_20.input).addClass('chb13');
        $(".chb13").change(function() {
        $(".chb13").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_21.input).addClass('chb14');
        $(cur_frm.fields_dict.partially_ok_21.input).addClass('chb14');
        $(cur_frm.fields_dict.not_ok_21.input).addClass('chb14');
        $(".chb14").change(function() {
        $(".chb14").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_22.input).addClass('chb15');
        $(cur_frm.fields_dict.partially_ok_22.input).addClass('chb15');
        $(cur_frm.fields_dict.not_ok_22.input).addClass('chb15');
        $(".chb15").change(function() {
        $(".chb15").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_23.input).addClass('chb16');
        $(cur_frm.fields_dict.partially_ok_23.input).addClass('chb16');
        $(cur_frm.fields_dict.not_ok_23.input).addClass('chb16');
        $(".chb16").change(function() {
        $(".chb16").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_24.input).addClass('chb17');
        $(cur_frm.fields_dict.partially_ok_24.input).addClass('chb17');
        $(cur_frm.fields_dict.not_ok_24.input).addClass('chb17');
        $(".chb17").change(function() {
        $(".chb17").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_25.input).addClass('chb18');
        $(cur_frm.fields_dict.partially_ok_25.input).addClass('chb18');
        $(cur_frm.fields_dict.not_ok_25.input).addClass('chb18');
        $(".chb18").change(function() {
        $(".chb18").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_26.input).addClass('chb19');
        $(cur_frm.fields_dict.partially_ok_26.input).addClass('chb19');
        $(cur_frm.fields_dict.not_ok_26.input).addClass('chb19');
        $(".chb19").change(function() {
        $(".chb19").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_27.input).addClass('chb20');
        $(cur_frm.fields_dict.partially_ok_27.input).addClass('chb20');
        $(cur_frm.fields_dict.not_ok_27.input).addClass('chb20');
        $(".chb20").change(function() {
        $(".chb20").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_28.input).addClass('chb21');
        $(cur_frm.fields_dict.partially_ok_28.input).addClass('chb21');
        $(cur_frm.fields_dict.not_ok_28.input).addClass('chb21');
        $(".chb21").change(function() {
        $(".chb21").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_29.input).addClass('chb22');
        $(cur_frm.fields_dict.partially_ok_29.input).addClass('chb22');
        $(cur_frm.fields_dict.not_ok_29.input).addClass('chb22');
        $(".chb22").change(function() {
        $(".chb22").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_30.input).addClass('chb23');
        $(cur_frm.fields_dict.partially_ok_30.input).addClass('chb23');
        $(cur_frm.fields_dict.not_ok_30.input).addClass('chb23');
        $(".chb23").change(function() {
        $(".chb23").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_31.input).addClass('chb24');
        $(cur_frm.fields_dict.partially_ok_31.input).addClass('chb24');
        $(cur_frm.fields_dict.not_ok_31.input).addClass('chb24');
        $(".chb24").change(function() {
        $(".chb24").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_32.input).addClass('chb25');
        $(cur_frm.fields_dict.partially_ok_32.input).addClass('chb25');
        $(cur_frm.fields_dict.not_ok_32.input).addClass('chb25');
        $(".chb25").change(function() {
        $(".chb25").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_33.input).addClass('chb26');
        $(cur_frm.fields_dict.partially_ok_33.input).addClass('chb26');
        $(cur_frm.fields_dict.not_ok_33.input).addClass('chb26');
        $(".chb26").change(function() {
        $(".chb26").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_34.input).addClass('chb27');
        $(cur_frm.fields_dict.partially_ok_34.input).addClass('chb27');
        $(cur_frm.fields_dict.not_ok_34.input).addClass('chb27');
        $(".chb27").change(function() {
        $(".chb27").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_7.input).addClass('chb28');
        $(cur_frm.fields_dict.partially_ok_7.input).addClass('chb28');
        $(cur_frm.fields_dict.not_ok7.input).addClass('chb28');
        $(".chb28").change(function() {
        $(".chb28").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_8.input).addClass('chb29');
        $(cur_frm.fields_dict.partially_ok_8.input).addClass('chb29');
        $(cur_frm.fields_dict.not_ok_8.input).addClass('chb29');
        $(".chb29").change(function() {
        $(".chb29").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_9.input).addClass('chb30');
        $(cur_frm.fields_dict.partially_ok_9.input).addClass('chb30');
        $(cur_frm.fields_dict.not_ok_9.input).addClass('chb30');
        $(".chb30").change(function() {
        $(".chb30").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_10.input).addClass('chb31');
        $(cur_frm.fields_dict.partially_ok_10.input).addClass('chb31');
        $(cur_frm.fields_dict.not_ok_10.input).addClass('chb31');
        $(".chb31").change(function() {
        $(".chb31").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_11.input).addClass('chb32');
        $(cur_frm.fields_dict.partially_ok_11.input).addClass('chb32');
        $(cur_frm.fields_dict.not_ok_11.input).addClass('chb32');
        $(".chb32").change(function() {
        $(".chb32").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_12.input).addClass('chb33');
        $(cur_frm.fields_dict.partially_ok_12.input).addClass('chb33');
        $(cur_frm.fields_dict.not_ok_12.input).addClass('chb33');
        $(".chb33").change(function() {
        $(".chb33").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_13.input).addClass('chb34');
        $(cur_frm.fields_dict.partially_ok_13.input).addClass('chb34');
        $(cur_frm.fields_dict.not_ok_13.input).addClass('chb34');
        $(".chb34").change(function() {
        $(".chb34").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_35.input).addClass('chb35');
        $(cur_frm.fields_dict.partially_ok_35.input).addClass('chb35');
        $(cur_frm.fields_dict.not_ok_35.input).addClass('chb35');
        $(".chb35").change(function() {
        $(".chb35").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_36.input).addClass('chb36');
        $(cur_frm.fields_dict.partially_ok_36.input).addClass('chb36');
        $(cur_frm.fields_dict.not_ok_36.input).addClass('chb36');
        $(".chb36").change(function() {
        $(".chb36").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_37.input).addClass('chb37');
        $(cur_frm.fields_dict.partially_ok_37.input).addClass('chb37');
        $(cur_frm.fields_dict.not_ok_37.input).addClass('chb37');
        $(".chb37").change(function() {
        $(".chb37").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_38.input).addClass('chb38');
        $(cur_frm.fields_dict.partially_ok_38.input).addClass('chb38');
        $(cur_frm.fields_dict.not_ok_38.input).addClass('chb38');
        $(".chb38").change(function() {
        $(".chb38").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_39.input).addClass('chb39');
        $(cur_frm.fields_dict.partially_ok_39.input).addClass('chb39');
        $(cur_frm.fields_dict.not_ok_39.input).addClass('chb39');
        $(".chb39").change(function() {
        $(".chb39").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_40.input).addClass('chb40');
        $(cur_frm.fields_dict.partially_ok_40.input).addClass('chb40');
        $(cur_frm.fields_dict.not_ok_40.input).addClass('chb40');
        $(".chb40").change(function() {
        $(".chb40").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_41.input).addClass('chb41');
        $(cur_frm.fields_dict.partially_ok_41.input).addClass('chb41');
        $(cur_frm.fields_dict.not_ok_41.input).addClass('chb41');
        $(".chb41").change(function() {
        $(".chb41").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_42.input).addClass('chb42');
        $(cur_frm.fields_dict.partially_ok_42.input).addClass('chb42');
        $(cur_frm.fields_dict.not_ok_42.input).addClass('chb42');
        $(".chb42").change(function() {
        $(".chb42").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_43.input).addClass('chb43');
        $(cur_frm.fields_dict.partially_ok_43.input).addClass('chb43');
        $(cur_frm.fields_dict.not_ok_43.input).addClass('chb43');
        $(".chb43").change(function() {
        $(".chb43").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_44.input).addClass('chb44');
        $(cur_frm.fields_dict.partially_check_44.input).addClass('chb44');
        $(cur_frm.fields_dict.not_ok_44.input).addClass('chb44');
        $(".chb44").change(function() {
        $(".chb44").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_45.input).addClass('chb45');
        $(cur_frm.fields_dict.partially_ok_45.input).addClass('chb45');
        $(cur_frm.fields_dict.not_ok_45.input).addClass('chb45');
        $(".chb45").change(function() {
        $(".chb45").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_46.input).addClass('chb46');
        $(cur_frm.fields_dict.partially_ok_46.input).addClass('chb46');
        $(cur_frm.fields_dict.not_ok_46.input).addClass('chb46');
        $(".chb46").change(function() {
        $(".chb46").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_47.input).addClass('chb47');
        $(cur_frm.fields_dict.partially_ok_47.input).addClass('chb47');
        $(cur_frm.fields_dict.not_ok_47.input).addClass('chb47');
        $(".chb47").change(function() {
        $(".chb47").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_48.input).addClass('chb48');
        $(cur_frm.fields_dict.partially_ok_48.input).addClass('chb48');
        $(cur_frm.fields_dict.not_ok_48.input).addClass('chb48');
        $(".chb48").change(function() {
        $(".chb48").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_49.input).addClass('chb49');
        $(cur_frm.fields_dict.partially_ok_49.input).addClass('chb49');
        $(cur_frm.fields_dict.not_ok_49.input).addClass('chb49');
        $(".chb49").change(function() {
        $(".chb49").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_50.input).addClass('chb50');
        $(cur_frm.fields_dict.partially_ok_50.input).addClass('chb50');
        $(cur_frm.fields_dict.not_ok_50.input).addClass('chb50');
        $(".chb50").change(function() {
        $(".chb50").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_51.input).addClass('chb51');
        $(cur_frm.fields_dict.partially_ok_51.input).addClass('chb51');
        $(cur_frm.fields_dict.not_ok_51.input).addClass('chb51');
        $(".chb51").change(function() {
        $(".chb51").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_52.input).addClass('chb52');
        $(cur_frm.fields_dict.partially_ok_52.input).addClass('chb52');
        $(cur_frm.fields_dict.not_ok_52.input).addClass('chb52');
        $(".chb52").change(function() {
        $(".chb52").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_53.input).addClass('chb53');
        $(cur_frm.fields_dict.partially_ok_53.input).addClass('chb53');
        $(cur_frm.fields_dict.not_ok_53.input).addClass('chb53');
        $(".chb53").change(function() {
        $(".chb53").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_54.input).addClass('chb54');
        $(cur_frm.fields_dict.partially_ok_54.input).addClass('chb54');
        $(cur_frm.fields_dict.not_ok_54.input).addClass('chb54');
        $(".chb54").change(function() {
        $(".chb54").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_55.input).addClass('chb55');
        $(cur_frm.fields_dict.partially_ok_55.input).addClass('chb55');
        $(cur_frm.fields_dict.not_ok_55.input).addClass('chb55');
        $(".chb55").change(function() {
        $(".chb55").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_56.input).addClass('chb56');
        $(cur_frm.fields_dict.partially_ok_56.input).addClass('chb56');
        $(cur_frm.fields_dict.not_ok_56.input).addClass('chb56');
        $(".chb56").change(function() {
        $(".chb56").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_57.input).addClass('chb57');
        $(cur_frm.fields_dict.partially_ok_57.input).addClass('chb57');
        $(cur_frm.fields_dict.not_ok_57.input).addClass('chb57');
        $(".chb57").change(function() {
        $(".chb57").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_58.input).addClass('chb58');
        $(cur_frm.fields_dict.partially_ok_58.input).addClass('chb58');
        $(cur_frm.fields_dict.not_ok_58.input).addClass('chb58');
        $(".chb58").change(function() {
        $(".chb58").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_59.input).addClass('chb59');
        $(cur_frm.fields_dict.partially_ok_59.input).addClass('chb59');
        $(cur_frm.fields_dict.not_ok_59.input).addClass('chb59');
        $(".chb59").change(function() {
        $(".chb59").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_60.input).addClass('chb60');
        $(cur_frm.fields_dict.partially_ok_60.input).addClass('chb60');
        $(cur_frm.fields_dict.not_ok_60.input).addClass('chb60');
        $(".chb60").change(function() {
        $(".chb60").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_61.input).addClass('chb61');
        $(cur_frm.fields_dict.partially_ok_61.input).addClass('chb61');
        $(cur_frm.fields_dict.not_ok_61.input).addClass('chb61');
        $(".chb61").change(function() {
        $(".chb61").prop('checked', false);
        $(this).prop('checked', true);
        })
    },
   
    'ok': function(frm) {
        if(frm.doc.ok){
            frm.set_value("iws","1");
        }
        else{
            frm.set_value("iws","");
        }
    },
    'partially_ok': function(frm) {
        if(frm.doc.partially_ok){
            frm.set_value("iws","0.5");
        }
        else{
            frm.set_value("iws","");
        }
    },
    'not_ok': function(frm) {
        if(frm.doc.not_ok){
            frm.set_value("iws","0");
        }
        else{
            frm.set_value("iws","");
        }
    },

    'ok_1': function(frm) {
        if(frm.doc.ok_1){
            frm.set_value("wslm","1");
        }
        else{
            frm.set_value("wslm","");
        }
    },
    'partially_ok1': function(frm) {
        if(frm.doc.partially_ok1){
            frm.set_value("wslm","0.5");
        }
        else{
            frm.set_value("wslm","");
        }
    },
    'not_ok1': function(frm) {
        if(frm.doc.not_ok1){
            frm.set_value("wslm","0");
        }
        else{
            frm.set_value("wslm","");
        }
    },
    'ok_2': function(frm) {
        if(frm.doc.ok_2){
            frm.set_value("tcsch","1");
        }
        else{
            frm.set_value("tcsch","");
        }
    },
    'partially_ok2': function(frm) {
        if(frm.doc.partially_ok2){
            frm.set_value("tcsch","0.5");
        }
        else{
            frm.set_value("tcsch","");
        }
    },
    'not_ok2': function(frm) {
        if(frm.doc.not_ok2){
            frm.set_value("tcsch","0");
        }
        else{
            frm.set_value("tcsch","");
        }
    },

    'ok_3': function(frm) {
        if(frm.doc.ok_3){
            frm.set_value("chslc","1");
        }
        else{
            frm.set_value("chslc","");
        }
    },
    'partially_ok3': function(frm) {
        if(frm.doc.partially_ok3){
            frm.set_value("chslc","0.5");
        }
        else{
            frm.set_value("chslc","");
        }
    },
    'not_ok3': function(frm) {
        if(frm.doc.not_ok3){
            frm.set_value("chslc","0");
        }
        else{
            frm.set_value("chslc","");
        }
    },
    'ok_4': function(frm) {
        if(frm.doc.ok_4){
            frm.set_value("iwc","1");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'partially_ok4': function(frm) {
        if(frm.doc.partially_ok4){
            frm.set_value("iwc","0.5");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'not_ok4': function(frm) {
        if(frm.doc.not_ok4){
            frm.set_value("iwc","0");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'ok_4': function(frm) {
        if(frm.doc.ok_4){
            frm.set_value("iwc","1");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'partially_ok4': function(frm) {
        if(frm.doc.partially_ok4){
            frm.set_value("iwc","0.5");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'not_ok4': function(frm) {
        if(frm.doc.not_ok4){
            frm.set_value("iwc","0");
        }
        else{
            frm.set_value("iwc","");
        }
    },
    'ok_5': function(frm) {
        if(frm.doc.ok_5){
            frm.set_value("mi","1");
        }
        else{
            frm.set_value("mi","");
        }
    },
    'partially_ok5': function(frm) {
        if(frm.doc.partially_ok5){
            frm.set_value("mi","0.5");
        }
        else{
            frm.set_value("mi","");
        }
    },
    'not_ok5': function(frm) {
        if(frm.doc.not_ok5){
            frm.set_value("mi","0");
        }
        else{
            frm.set_value("mi","");
        }
    },
    'ok6': function(frm) {
        if(frm.doc.ok6){
            frm.set_value("si","1");
        }
        else{
            frm.set_value("si","");
        }
    },
    'partially_ok6': function(frm) {
        if(frm.doc.partially_ok6){
            frm.set_value("si","0.5");
        }
        else{
            frm.set_value("si","");
        }
    },
    'not_ok6': function(frm) {
        if(frm.doc.not_ok6){
            frm.set_value("si","0");
        }
        else{
            frm.set_value("si","");
        }
    },
    iws:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws));
    },
    wslm:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm));
    },
    tcsch:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch));
    },
    chslc:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch)+flt(frm.doc.chslc));
    },
    iwc:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch)+flt(frm.doc.chslc)+flt(frm.doc.iwc));
    },
    mi:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch)+flt(frm.doc.chslc)+flt(frm.doc.iwc)+flt(frm.doc.mi));
    },
    si:function(frm){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch)+flt(frm.doc.chslc)+flt(frm.doc.iwc)+flt(frm.doc.mi)+flt(frm.doc.si));
    },
});
