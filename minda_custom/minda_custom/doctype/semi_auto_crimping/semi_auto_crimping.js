// Copyright (c) 2019, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Semi Auto Crimping', {
    choose_question: function(frm){
        
        
    },
    ok: function(frm) {
        if(frm.doc.ok){
            frm.trigger("onload");
            frm.set_value("iws","1");
        }
        else{
            frm.set_value("iws","");
        }
    },
    partially_ok: function(frm) {
        if(frm.doc.partially_ok){
            frm.trigger("onload");
            frm.set_value("iws","0.5");
        }
        else{
            frm.set_value("iws","");
        }
    },
    not_ok: function(frm) {
        if(frm.doc.not_ok){
            frm.trigger("onload");
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
    'ok_14': function(frm) {
        if(frm.doc.ok_14){
            frm.set_value("d_1","1");
        }
        else{
            frm.set_value("d_1","");
        }
    },
    'partially_ok_14': function(frm) {
        if(frm.doc.partially_ok_14){
            frm.set_value("d_1","0.5");
        }
        else{
            frm.set_value("d_1","");
        }
    },
    'not_ok_14': function(frm) {
        if(frm.doc.not_ok_14){
            frm.set_value("d_1","0");
        }
        else{
            frm.set_value("d_1","");
        }
    },

    'ok_15': function(frm) {
        if(frm.doc.ok_15){
            frm.set_value("d_2","1");
        }
        else{
            frm.set_value("d_2","");
        }
    },
    'partially_ok_15': function(frm) {
        if(frm.doc.partially_ok_15){
            frm.set_value("d_2","0.5");
        }
        else{
            frm.set_value("d_2","");
        }
    },
    'not_ok_15': function(frm) {
        if(frm.doc.not_ok_15){
            frm.set_value("d_2","0");
        }
        else{
            frm.set_value("d_2","");
        }
    },
    'ok_16': function(frm) {
        if(frm.doc.ok_16){
            frm.set_value("d_3","1");
        }
        else{
            frm.set_value("d_3","");
        }
    },
    'partially_ok_16': function(frm) {
        if(frm.doc.partially_ok_16){
            frm.set_value("d_3","0.5");
        }
        else{
            frm.set_value("d_3","");
        }
    },
    'not_ok_16': function(frm) {
        if(frm.doc.not_ok_16){
            frm.set_value("d_3","0");
        }
        else{
            frm.set_value("d_3","");
        }
    },

    'ok_17': function(frm) {
        if(frm.doc.ok_17){
            frm.set_value("d_4","1");
        }
        else{
            frm.set_value("d_4","");
        }
    },
    'partially_ok_17': function(frm) {
        if(frm.doc.partially_ok_17){
            frm.set_value("d_4","0.5");
        }
        else{
            frm.set_value("d_4","");
        }
    },
    'not_ok_17': function(frm) {
        if(frm.doc.not_ok_17){
            frm.set_value("d_4","0");
        }
        else{
            frm.set_value("d_4","");
        }
    },
    'ok_18': function(frm) {
        if(frm.doc.ok_18){
            frm.set_value("d_5","1");
        }
        else{
            frm.set_value("d_5","");
        }
    },
    'partially_ok_118': function(frm) {
        if(frm.doc.partially_ok_118){
            frm.set_value("d_5","0.5");
        }
        else{
            frm.set_value("d_5","");
        }
    },
    'not_ok_18': function(frm) {
        if(frm.doc.not_ok_18){
            frm.set_value("d_5","0");
        }
        else{
            frm.set_value("d_5","");
        }
    },
    'ok_19': function(frm) {
        if(frm.doc.ok_19){
            frm.set_value("d_6","1");
        }
        else{
            frm.set_value("d_6","");
        }
    },
    'partially_ok_19': function(frm) {
        if(frm.doc.partially_ok_19){
            frm.set_value("d_6","0.5");
        }
        else{
            frm.set_value("d_6","");
        }
    },
    'not_ok_19': function(frm) {
        if(frm.doc.not_ok_19){
            frm.set_value("d_6","0");
        }
        else{
            frm.set_value("d_6","");
        }
    },
    'ok_20': function(frm) {
        if(frm.doc.ok_20){
            frm.set_value("d_7","1");
        }
        else{
            frm.set_value("d_7","");
        }
    },
    'partially_ok_20': function(frm) {
        if(frm.doc.partially_ok_20){
            frm.set_value("d_7","0.5");
        }
        else{
            frm.set_value("d_7","");
        }
    },
    'not_ok_20': function(frm) {
        if(frm.doc.not_ok_20){
            frm.set_value("d_7","0");
        }
        else{
            frm.set_value("d_7","");
        }
    },
    'ok_21': function(frm) {
        if(frm.doc.ok_21){
            frm.set_value("d_8","1");
        }
        else{
            frm.set_value("d_8","");
        }
    },
    'partially_ok_21': function(frm) {
        if(frm.doc.partially_ok_21){
            frm.set_value("d_8","0.5");
        }
        else{
            frm.set_value("d_8","");
        }
    },
    'not_ok_21': function(frm) {
        if(frm.doc.not_ok_21){
            frm.set_value("d_8","0");
        }
        else{
            frm.set_value("d_8","");
        }
    },
    'ok_22': function(frm) {
        if(frm.doc.ok_22){
            frm.set_value("d_9","1");
        }
        else{
            frm.set_value("d_9","");
        }
    },
    'partially_ok_22': function(frm) {
        if(frm.doc.partially_ok_22){
            frm.set_value("d_9","0.5");
        }
        else{
            frm.set_value("d_9","");
        }
    },
    'not_ok_22': function(frm) {
        if(frm.doc.not_ok_22){
            frm.set_value("d_9","0");
        }
        else{
            frm.set_value("d_9","");
        }
    },
    'ok_23': function(frm) {
        if(frm.doc.ok_23){
            frm.set_value("d_10","1");
        }
        else{
            frm.set_value("d_10","");
        }
    },
    'partially_ok_23': function(frm) {
        if(frm.doc.partially_ok_23){
            frm.set_value("d_10","0.5");
        }
        else{
            frm.set_value("d_10","");
        }
    },
    'not_ok_23': function(frm) {
        if(frm.doc.not_ok_23){
            frm.set_value("d_10","0");
        }
        else{
            frm.set_value("d_10","");
        }
    },
    'ok_24': function(frm) {
        if(frm.doc.ok_24){
            frm.set_value("d_11","1");
        }
        else{
            frm.set_value("d_11","");
        }
    },
    'partially_ok_24': function(frm) {
        if(frm.doc.partially_ok_24){
            frm.set_value("d_11","0.5");
        }
        else{
            frm.set_value("d_11","");
        }
    },
    'not_ok_24': function(frm) {
        if(frm.doc.not_ok_24){
            frm.set_value("d_11","0");
        }
        else{
            frm.set_value("d_11","");
        }
    },
    'ok_25': function(frm) {
        if(frm.doc.ok_25){
            frm.set_value("d_12","1");
        }
        else{
            frm.set_value("d_12","");
        }
    },
    'partially_ok_25': function(frm) {
        if(frm.doc.partially_ok_25){
            frm.set_value("d_12","0.5");
        }
        else{
            frm.set_value("d_12","");
        }
    },
    'not_ok_25': function(frm) {
        if(frm.doc.not_ok_25){
            frm.set_value("d_12","0");
        }
        else{
            frm.set_value("d_12","");
        }
    },
    'ok_26': function(frm) {
        if(frm.doc.ok_26){
            frm.set_value("d_13","1");
        }
        else{
            frm.set_value("d_13","");
        }
    },
    'partially_ok_26': function(frm) {
        if(frm.doc.partially_ok_26){
            frm.set_value("d_13","0.5");
        }
        else{
            frm.set_value("d_13","");
        }
    },
    'not_ok_26': function(frm) {
        if(frm.doc.not_ok_26){
            frm.set_value("d_13","0");
        }
        else{
            frm.set_value("d_13","");
        }
    },
    'ok_27': function(frm) {
        if(frm.doc.ok_27){
            frm.set_value("d_14","1");
        }
        else{
            frm.set_value("d_14","");
        }
    },
    'partially_ok_27': function(frm) {
        if(frm.doc.partially_ok_27){
            frm.set_value("d_14","0.5");
        }
        else{
            frm.set_value("d_14","");
        }
    },
    'not_ok_27': function(frm) {
        if(frm.doc.not_ok_27){
            frm.set_value("d_14","0");
        }
        else{
            frm.set_value("d_14","");
        }
    },
    'ok_28': function(frm) {
        if(frm.doc.ok_28){
            frm.set_value("d_15","1");
        }
        else{
            frm.set_value("d_15","");
        }
    },
    'partially_ok_28': function(frm) {
        if(frm.doc.partially_ok_28){
            frm.set_value("d_15","0.5");
        }
        else{
            frm.set_value("d_15","");
        }
    },
    'not_ok_28': function(frm) {
        if(frm.doc.not_ok_28){
            frm.set_value("d_15","0");
        }
        else{
            frm.set_value("d_15","");
        }
    },
    'ok_29': function(frm) {
        if(frm.doc.ok_29){
            frm.set_value("d_16","1");
        }
        else{
            frm.set_value("d_16","");
        }
    },
    'partially_ok_29': function(frm) {
        if(frm.doc.partially_ok_29){
            frm.set_value("d_16","0.5");
        }
        else{
            frm.set_value("d_16","");
        }
    },
    'not_ok_29': function(frm) {
        if(frm.doc.not_ok_29){
            frm.set_value("d_16","0");
        }
        else{
            frm.set_value("d_16","");
        }
    },
    'ok_30': function(frm) {
        if(frm.doc.ok_30){
            frm.set_value("d_17","1");
        }
        else{
            frm.set_value("d_17","");
        }
    },
    'partially_ok_30': function(frm) {
        if(frm.doc.partially_ok_30){
            frm.set_value("d_17","0.5");
        }
        else{
            frm.set_value("d_17","");
        }
    },
    'not_ok_30': function(frm) {
        if(frm.doc.not_ok_30){
            frm.set_value("d_17","0");
        }
        else{
            frm.set_value("d_17","");
        }
    },
    'ok_31': function(frm) {
        if(frm.doc.ok_31){
            frm.set_value("d_18","1");
        }
        else{
            frm.set_value("d_18","");
        }
    },
    'partially_ok_31': function(frm) {
        if(frm.doc.partially_ok_31){
            frm.set_value("d_18","0.5");
        }
        else{
            frm.set_value("d_18","");
        }
    },
    'not_ok_31': function(frm) {
        if(frm.doc.not_ok_31){
            frm.set_value("d_18","0");
        }
        else{
            frm.set_value("d_18","");
        }
    },
    'ok_32': function(frm) {
        if(frm.doc.ok_32){
            frm.set_value("d_19","1");
        }
        else{
            frm.set_value("d_19","");
        }
    },
    'partially_ok_32': function(frm) {
        if(frm.doc.partially_ok_32){
            frm.set_value("d_19","0.5");
        }
        else{
            frm.set_value("d_19","");
        }
    },
    'not_ok_32': function(frm) {
        if(frm.doc.not_ok_32){
            frm.set_value("d_19","0");
        }
        else{
            frm.set_value("d_19","");
        }
    },
    'ok_33': function(frm) {
        if(frm.doc.ok_33){
            frm.set_value("d_20","1");
        }
        else{
            frm.set_value("d_20","");
        }
    },
    'partially_ok_33': function(frm) {
        if(frm.doc.partially_ok_33){
            frm.set_value("d_20","0.5");
        }
        else{
            frm.set_value("d_20","");
        }
    },
    'not_ok_33': function(frm) {
        if(frm.doc.not_ok_33){
            frm.set_value("d_20","0");
        }
        else{
            frm.set_value("d_20","");
        }
    },
    'ok_34': function(frm) {
        if(frm.doc.ok_34){
            frm.set_value("d_21","1");
        }
        else{
            frm.set_value("d_21","");
        }
    },
    'partially_ok_34': function(frm) {
        if(frm.doc.partially_ok_34){
            frm.set_value("d_21","0.5");
        }
        else{
            frm.set_value("d_21","");
        }
    },
    'not_ok_34': function(frm) {
        if(frm.doc.not_ok_34){
            frm.set_value("d_21","0");
        }
        else{
            frm.set_value("d_21","");
        }
    },
    'ok_7': function(frm) {
        if(frm.doc.ok_7){
            frm.set_value("clit_1","1");
        }
        else{
            frm.set_value("clit_1","");
        }
    },
    'partially_ok_7': function(frm) {
        if(frm.doc.partially_ok_7){
            frm.set_value("clit_1","0.5");
        }
        else{
            frm.set_value("clit_1","");
        }
    },
    'not_ok7': function(frm) {
        if(frm.doc.not_ok7){
            frm.set_value("clit_1","0");
        }
        else{
            frm.set_value("clit_1","");
        }
    },

    'ok_8': function(frm) {
        if(frm.doc.ok_8){
            frm.set_value("clit_2","1");
        }
        else{
            frm.set_value("clit_2","");
        }
    },
    'partially_ok_8': function(frm) {
        if(frm.doc.partially_ok_8){
            frm.set_value("clit_2","0.5");
        }
        else{
            frm.set_value("clit_2","");
        }
    },
    'not_ok_8': function(frm) {
        if(frm.doc.not_ok_8){
            frm.set_value("clit_2","0");
        }
        else{
            frm.set_value("clit_2","");
        }
    },
    'ok_9': function(frm) {
        if(frm.doc.ok_9){
            frm.set_value("clit_3","1");
        }
        else{
            frm.set_value("clit_3","");
        }
    },
    'partially_ok_9': function(frm) {
        if(frm.doc.partially_ok_9){
            frm.set_value("clit_3","0.5");
        }
        else{
            frm.set_value("clit_3","");
        }
    },
    'not_ok_9': function(frm) {
        if(frm.doc.not_ok_9){
            frm.set_value("clit_3","0");
        }
        else{
            frm.set_value("clit_3","");
        }
    },

    'ok_10': function(frm) {
        if(frm.doc.ok_10){
            frm.set_value("clit_4","1");
        }
        else{
            frm.set_value("clit_4","");
        }
    },
    'partially_ok_10': function(frm) {
        if(frm.doc.partially_ok_10){
            frm.set_value("clit_4","0.5");
        }
        else{
            frm.set_value("clit_4","");
        }
    },
    'not_ok_10': function(frm) {
        if(frm.doc.not_ok_10){
            frm.set_value("clit_4","0");
        }
        else{
            frm.set_value("clit_4","");
        }
    },
    'ok_11': function(frm) {
        if(frm.doc.ok_11){
            frm.set_value("clit_6","1");
        }
        else{
            frm.set_value("clit_6","");
        }
    },
    'partially_ok_11': function(frm) {
        if(frm.doc.partially_ok_11){
            frm.set_value("clit_6","0.5");
        }
        else{
            frm.set_value("clit_6","");
        }
    },
    'not_ok_11': function(frm) {
        if(frm.doc.not_ok_11){
            frm.set_value("clit_6","0");
        }
        else{
            frm.set_value("clit_6","");
        }
    },
    'ok_12': function(frm) {
        if(frm.doc.ok_12){
            frm.set_value("clit_5","1");
        }
        else{
            frm.set_value("clit_5","");
        }
    },
    'partially_ok_12': function(frm) {
        if(frm.doc.partially_ok_12){
            frm.set_value("clit_5","0.5");
        }
        else{
            frm.set_value("clit_5","");
        }
    },
    'not_ok_12': function(frm) {
        if(frm.doc.not_ok_12){
            frm.set_value("clit_5","0");
        }
        else{
            frm.set_value("clit_5","");
        }
    },
    'ok_13': function(frm) {
        if(frm.doc.ok_13){
            frm.set_value("clit_7","1");
        }
        else{
            frm.set_value("clit_7","");
        }
    },
    'partially_ok_13': function(frm) {
        if(frm.doc.partially_ok_13){
            frm.set_value("clit_7","0.5");
        }
        else{
            frm.set_value("clit_7","");
        }
    },
    'not_ok_13': function(frm) {
        if(frm.doc.not_ok_13){
            frm.set_value("clit_7","0");
        }
        else{
            frm.set_value("clit_7","");
        }
    },
    'ok_35': function(frm) {
        if(frm.doc.ok_35){
            frm.set_value("safe_1","1");
        }
        else{
            frm.set_value("safe_1","");
        }
    },
    'partially_ok_35': function(frm) {
        if(frm.doc.partially_ok_35){
            frm.set_value("safe_1","0.5");
        }
        else{
            frm.set_value("safe_1","");
        }
    },
    'not_ok_35': function(frm) {
        if(frm.doc.not_ok_35){
            frm.set_value("safe_1","0");
        }
        else{
            frm.set_value("safe_1","");
        }
    },

    'ok_36': function(frm) {
        if(frm.doc.ok_36){
            frm.set_value("safe_2","1");
        }
        else{
            frm.set_value("safe_2","");
        }
    },
    'partially_ok_36': function(frm) {
        if(frm.doc.partially_ok_36){
            frm.set_value("safe_2","0.5");
        }
        else{
            frm.set_value("safe_2","");
        }
    },
    'not_ok_36': function(frm) {
        if(frm.doc.not_ok_36){
            frm.set_value("safe_2","0");
        }
        else{
            frm.set_value("safe_2","");
        }
    },
    'ok_37': function(frm) {
        if(frm.doc.ok_37){
            frm.set_value("safe_3","1");
        }
        else{
            frm.set_value("safe_3","");
        }
    },
    'partially_ok_37': function(frm) {
        if(frm.doc.partially_ok_37){
            frm.set_value("safe_3","0.5");
        }
        else{
            frm.set_value("safe_3","");
        }
    },
    'not_ok_37': function(frm) {
        if(frm.doc.not_ok_37){
            frm.set_value("safe_3","0");
        }
        else{
            frm.set_value("safe_3","");
        }
    },

    'ok_38': function(frm) {
        if(frm.doc.ok_38){
            frm.set_value("safe_4","1");
        }
        else{
            frm.set_value("safe_4","");
        }
    },
    'partially_ok_38': function(frm) {
        if(frm.doc.partially_ok_38){
            frm.set_value("safe_4","0.5");
        }
        else{
            frm.set_value("safe_4","");
        }
    },
    'not_ok_38': function(frm) {
        if(frm.doc.not_ok_38){
            frm.set_value("safe_4","0");
        }
        else{
            frm.set_value("safe_4","");
        }
    },
    'ok_39': function(frm) {
        if(frm.doc.ok_39){
            frm.set_value("safe_5","1");
        }
        else{
            frm.set_value("safe_5","");
        }
    },
    'partially_ok_39': function(frm) {
        if(frm.doc.partially_ok_39){
            frm.set_value("safe_5","0.5");
        }
        else{
            frm.set_value("safe_5","");
        }
    },
    'not_ok_39': function(frm) {
        if(frm.doc.not_ok_39){
            frm.set_value("safe_5","0");
        }
        else{
            frm.set_value("safe_5","");
        }
    },
    'ok_40': function(frm) {
        if(frm.doc.ok_40){
            frm.set_value("safe_6","1");
        }
        else{
            frm.set_value("safe_6","");
        }
    },
    'partially_ok_40': function(frm) {
        if(frm.doc.partially_ok_40){
            frm.set_value("safe_6","0.5");
        }
        else{
            frm.set_value("safe_6","");
        }
    },
    'not_ok_40': function(frm) {
        if(frm.doc.not_ok_40){
            frm.set_value("safe_6","0");
        }
        else{
            frm.set_value("safe_6","");
        }
    },
    'ok_41': function(frm) {
        if(frm.doc.ok_41){
            frm.set_value("safe_7","1");
        }
        else{
            frm.set_value("safe_7","");
        }
    },
    'partially_ok_41': function(frm) {
        if(frm.doc.partially_ok_41){
            frm.set_value("safe_7","0.5");
        }
        else{
            frm.set_value("safe_7","");
        }
    },
    'not_ok_41': function(frm) {
        if(frm.doc.not_ok_41){
            frm.set_value("safe_7","0");
        }
        else{
            frm.set_value("safe_7","");
        }
    },
    'ok_42': function(frm) {
        if(frm.doc.ok_42){
            frm.set_value("work_1","1");
        }
        else{
            frm.set_value("work_1","");
        }
    },
    'partially_ok_42': function(frm) {
        if(frm.doc.partially_ok_42){
            frm.set_value("work_1","0.5");
        }
        else{
            frm.set_value("work_1","");
        }
    },
    'not_ok_42': function(frm) {
        if(frm.doc.not_ok_42){
            frm.set_value("work_1","0");
        }
        else{
            frm.set_value("work_1","");
        }
    },

    'ok_43': function(frm) {
        if(frm.doc.ok_43){
            frm.set_value("work_2","1");
        }
        else{
            frm.set_value("work_2","");
        }
    },
    'partially_ok_43': function(frm) {
        if(frm.doc.partially_ok_43){
            frm.set_value("work_2","0.5");
        }
        else{
            frm.set_value("work_2","");
        }
    },
    'not_ok_43': function(frm) {
        if(frm.doc.not_ok_43){
            frm.set_value("work_2","0");
        }
        else{
            frm.set_value("work_2","");
        }
    },
    'ok_44': function(frm) {
        if(frm.doc.ok_44){
            frm.set_value("work_3","1");
        }
        else{
            frm.set_value("work_3","");
        }
    },
    'partially_ok_44': function(frm) {
        if(frm.doc.partially_ok_44){
            frm.set_value("work_3","0.5");
        }
        else{
            frm.set_value("work_3","");
        }
    },
    'not_ok_44': function(frm) {
        if(frm.doc.not_ok_44){
            frm.set_value("work_3","0");
        }
        else{
            frm.set_value("work_3","");
        }
    },

    'ok_45': function(frm) {
        if(frm.doc.ok_45){
            frm.set_value("work_4","1");
        }
        else{
            frm.set_value("work_4","");
        }
    },
    'partially_ok_45': function(frm) {
        if(frm.doc.partially_ok_45){
            frm.set_value("work_4","0.5");
        }
        else{
            frm.set_value("work_4","");
        }
    },
    'not_ok_45': function(frm) {
        if(frm.doc.not_ok_45){
            frm.set_value("work_4","0");
        }
        else{
            frm.set_value("work_4","");
        }
    },
    'ok_46': function(frm) {
        if(frm.doc.ok_46){
            frm.set_value("wotk_5","1");
        }
        else{
            frm.set_value("wotk_5","");
        }
    },
    'partially_ok_46': function(frm) {
        if(frm.doc.partially_ok_46){
            frm.set_value("wotk_5","0.5");
        }
        else{
            frm.set_value("wotk_5","");
        }
    },
    'not_ok_46': function(frm) {
        if(frm.doc.not_ok_46){
            frm.set_value("wotk_5","0");
        }
        else{
            frm.set_value("wotk_5","");
        }
    },
    'ok_47': function(frm) {
        if(frm.doc.ok_47){
            frm.set_value("work_6","1");
        }
        else{
            frm.set_value("work_6","");
        }
    },
    'partially_ok_47': function(frm) {
        if(frm.doc.partially_ok_47){
            frm.set_value("work_6","0.5");
        }
        else{
            frm.set_value("work_6","");
        }
    },
    'not_ok_47': function(frm) {
        if(frm.doc.not_ok_47){
            frm.set_value("work_6","0");
        }
        else{
            frm.set_value("work_6","");
        }
    },
    'ok_48': function(frm) {
        if(frm.doc.ok_48){
            frm.set_value("work_7","1");
        }
        else{
            frm.set_value("work_7","");
        }
    },
    'partially_ok_48': function(frm) {
        if(frm.doc.partially_ok_48){
            frm.set_value("work_7","0.5");
        }
        else{
            frm.set_value("work_7","");
        }
    },
    'not_ok_48': function(frm) {
        if(frm.doc.not_ok_48){
            frm.set_value("work_7","0");
        }
        else{
            frm.set_value("work_7","");
        }
    },
    'ok_49': function(frm) {
        if(frm.doc.ok_49){
            frm.set_value("f1","1");
        }
        else{
            frm.set_value("f1","");
        }
    },
    'partially_ok_49': function(frm) {
        if(frm.doc.partially_ok_49){
            frm.set_value("f1","0.5");
        }
        else{
            frm.set_value("f1","");
        }
    },
    'not_ok_49': function(frm) {
        if(frm.doc.not_ok_49){
            frm.set_value("f1","0");
        }
        else{
            frm.set_value("f1","");
        }
    },

    'ok_50': function(frm) {
        if(frm.doc.ok_50){
            frm.set_value("f2","1");
        }
        else{
            frm.set_value("f2","");
        }
    },
    'partially_ok_50': function(frm) {
        if(frm.doc.partially_ok_50){
            frm.set_value("f2","0.5");
        }
        else{
            frm.set_value("f2","");
        }
    },
    'not_ok_50': function(frm) {
        if(frm.doc.not_ok_50){
            frm.set_value("f2","0");
        }
        else{
            frm.set_value("f2","");
        }
    },
    'ok_51': function(frm) {
        if(frm.doc.ok_51){
            frm.set_value("f3","1");
        }
        else{
            frm.set_value("f3","");
        }
    },
    'partially_ok_51': function(frm) {
        if(frm.doc.partially_ok_51){
            frm.set_value("f3","0.5");
        }
        else{
            frm.set_value("f3","");
        }
    },
    'not_ok_51': function(frm) {
        if(frm.doc.not_ok_51){
            frm.set_value("f3","0");
        }
        else{
            frm.set_value("f3","");
        }
    },

    'ok_56': function(frm) {
        if(frm.doc.ok_56){
            frm.set_value("s1","1");
        }
        else{
            frm.set_value("s1","");
        }
    },
    'partially_ok_56': function(frm) {
        if(frm.doc.partially_ok_56){
            frm.set_value("s1","0.5");
        }
        else{
            frm.set_value("s1","");
        }
    },
    'not_ok_56': function(frm) {
        if(frm.doc.not_ok_56){
            frm.set_value("s1","0");
        }
        else{
            frm.set_value("s1","");
        }
    },
    'ok_57': function(frm) {
        if(frm.doc.ok_57){
            frm.set_value("s2","1");
        }
        else{
            frm.set_value("s2","");
        }
    },
    'partially_ok_57': function(frm) {
        if(frm.doc.partially_ok_57){
            frm.set_value("s2","0.5");
        }
        else{
            frm.set_value("s2","");
        }
    },
    'not_ok_57': function(frm) {
        if(frm.doc.not_ok_57){
            frm.set_value("s2","0");
        }
        else{
            frm.set_value("s2","");
        }
    },

    'ok_58': function(frm) {
        if(frm.doc.ok_58){
            frm.set_value("s3","1");
        }
        else{
            frm.set_value("s3","");
        }
    },
    'partially_ok_58': function(frm) {
        if(frm.doc.partially_ok_58){
            frm.set_value("s3","0.5");
        }
        else{
            frm.set_value("s3","");
        }
    },
    'not_ok_58': function(frm) {
        if(frm.doc.not_ok_58){
            frm.set_value("s3","0");
        }
        else{
            frm.set_value("s3","");
        }
    },
    'ok_59': function(frm) {
        if(frm.doc.ok_59){
            frm.set_value("zs","1");
        }
        else{
            frm.set_value("zs","");
        }
    },
    'partially_ok_59': function(frm) {
        if(frm.doc.partially_ok_59){
            frm.set_value("zs","0.5");
        }
        else{
            frm.set_value("zs","");
        }
    },
    'not_ok_59': function(frm) {
        if(frm.doc.not_ok_59){
            frm.set_value("zs","0");
        }
        else{
            frm.set_value("zs","");
        }
    },
    'ok_60': function(frm) {
        if(frm.doc.ok_60){
            frm.set_value("rh","1");
        }
        else{
            frm.set_value("rh","");
        }
    },
    'partially_ok_60': function(frm) {
        if(frm.doc.partially_ok_60){
            frm.set_value("rh","0.5");
        }
        else{
            frm.set_value("rh","");
        }
    },
    'not_ok_60': function(frm) {
        if(frm.doc.not_ok_60){
            frm.set_value("rh","0");
        }
        else{
            frm.set_value("rh","");
        }
    },
    'ok_61': function(frm) {
        if(frm.doc.ok_61){
            frm.set_value("cch","1");
        }
        else{
            frm.set_value("cch","");
        }
    },
    'partially_ok_61': function(frm) {
        if(frm.doc.partially_ok_61){
            frm.set_value("cch","0.5");
        }
        else{
            frm.set_value("cch","");
        }
    },
    'not_ok_61': function(frm) {
        if(frm.doc.not_ok_61){
            frm.set_value("cch","0");
        }
        else{
            frm.set_value("cch","");
        }
    },
    'ok_62': function(frm) {
        if(frm.doc.ok_62){
            frm.set_value("b_1","1");
        }
        else{
            frm.set_value("b_1","");
        }
    },
    'partially_ok_62': function(frm) {
        if(frm.doc.partially_ok_62){
            frm.set_value("b_1","0.5");
        }
        else{
            frm.set_value("b_1","");
        }
    },
    'not_ok_62': function(frm) {
        if(frm.doc.not_ok_62){
            frm.set_value("b_1","0");
        }
        else{
            frm.set_value("b_1","");
        }
    },
    'ok_63': function(frm) {
        if(frm.doc.ok_63){
            frm.set_value("b_2","1");
        }
        else{
            frm.set_value("b_2","");
        }
    },
    'partially_ok_63': function(frm) {
        if(frm.doc.partially_ok_63){
            frm.set_value("b_2","0.5");
        }
        else{
            frm.set_value("b_2","");
        }
    },
    'not_ok_63': function(frm) {
        if(frm.doc.not_ok_63){
            frm.set_value("b_2","0");
        }
        else{
            frm.set_value("b_2","");
        }
    },
    'ok_64': function(frm) {
        if(frm.doc.ok_64){
            frm.set_value("b_3","1");
        }
        else{
            frm.set_value("b_3","");
        }
    },
    'partially_ok_64': function(frm) {
        if(frm.doc.partially_ok_64){
            frm.set_value("b_3","0.5");
        }
        else{
            frm.set_value("b_3","");
        }
    },
    'not_ok_64': function(frm) {
        if(frm.doc.not_ok_64){
            frm.set_value("b_3","0");
        }
        else{
            frm.set_value("b_3","");
        }
    },
    'ok_65': function(frm) {
        if(frm.doc.ok_65){
            frm.set_value("b_4","1");
        }
        else{
            frm.set_value("b_4","");
        }
    },
    'partially_ok_65': function(frm) {
        if(frm.doc.partially_ok_65){
            frm.set_value("b_4","0.5");
        }
        else{
            frm.set_value("b_4","");
        }
    },
    'not_ok_65': function(frm) {
        if(frm.doc.not_ok_65){
            frm.set_value("b_4","0");
        }
        else{
            frm.set_value("b_4","");
        }
    },
    'ok_66': function(frm) {
        if(frm.doc.ok_66){
            frm.set_value("b_5","1");
        }
        else{
            frm.set_value("b_5","");
        }
    },
    'partially_ok_66': function(frm) {
        if(frm.doc.partially_ok_66){
            frm.set_value("b_5","0.5");
        }
        else{
            frm.set_value("b_5","");
        }
    },
    'not_ok_66': function(frm) {
        if(frm.doc.not_ok_66){
            frm.set_value("b_5","0");
        }
        else{
            frm.set_value("b_5","");
        }
    },
    ok_67: function(frm) {
        if(frm.doc.ok_67){
            frm.set_value("b_6","1");
        }
        else{
            frm.set_value("b_6","");
        }
    },
    partially_ok_67: function(frm) {
        if(frm.doc.partially_ok_67){
            frm.set_value("b_6","0.5");
        }
        else{
            frm.set_value("b_6","");
        }
    },
    not_ok_67: function(frm) {
        if(frm.doc.not_ok_67){
            frm.set_value("b_6","0");
        }
        else{
            frm.set_value("b_6","");
        }
    },
    after_save:function(frm){
        frm.trigger("onload");
    },
   onload: function(frm) {
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
        $(cur_frm.fields_dict.partially_ok_44.input).addClass('chb44');
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
        $(cur_frm.fields_dict.ok_62.input).addClass('chb62');
        $(cur_frm.fields_dict.partially_ok_62.input).addClass('chb62');
        $(cur_frm.fields_dict.not_ok_62.input).addClass('chb62');
        $(".chb62").change(function() {
        $(".chb62").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_63.input).addClass('chb63');
        $(cur_frm.fields_dict.partially_ok_63.input).addClass('chb63');
        $(cur_frm.fields_dict.not_ok_63.input).addClass('chb63');
        $(".chb63").change(function() {
        $(".chb63").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_64.input).addClass('chb64');
        $(cur_frm.fields_dict.partially_ok_64.input).addClass('chb64');
        $(cur_frm.fields_dict.not_ok_64.input).addClass('chb64');
        $(".chb64").change(function() {
        $(".chb64").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_65.input).addClass('chb65');
        $(cur_frm.fields_dict.partially_ok_65.
        ).addClass('chb65');
        $(cur_frm.fields_dict.not_ok_65.input).addClass('chb65');
        $(".chb65").change(function() {
        $(".chb65").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_66.input).addClass('chb66');
        $(cur_frm.fields_dict.partially_ok_66.input).addClass('chb66');
        $(cur_frm.fields_dict.not_ok_66.input).addClass('chb66');
        $(".chb66").change(function() {
        $(".chb66").prop('checked', false);
        $(this).prop('checked', true);
        })
        $(cur_frm.fields_dict.ok_67.input).addClass('chb67');
        $(cur_frm.fields_dict.partially_ok_67.input).addClass('chb67');
        $(cur_frm.fields_dict.not_ok_67.input).addClass('chb67');
        $(".chb67").change(function() {
        $(".chb67").prop('checked', false);
        $(this).prop('checked', true);
        })
    },
   
    validate:function(frm){
        if(!frm.doc.choose_question_filter){
            frappe.call({
                "method":"minda_custom.minda_custom.doctype.semi_auto_crimping.semi_auto_crimping.update_choose_question",
                args:{
                "choose_question": frm.doc.choose_question
                },
                callback: function(r){
                    if(frm.doc.choose_question){
                        frm.set_value("choose_question_filter", frm.doc.choose_question)
                        frm.save()
                    }
                }
                })
        }
        frm.trigger("onload");
        if((frm.doc.iws) || (frm.doc.wslm)|| (frm.doc.tcsch)|| (frm.doc.chslc)|| (frm.doc.iwc)|| (frm.doc.mi) || (frm.doc.si)){
        frm.set_value("mark_obtained_a", flt(frm.doc.iws)+flt(frm.doc.wslm)+flt(frm.doc.tcsch)+flt(frm.doc.chslc)+flt(frm.doc.iwc)+flt(frm.doc.mi)+flt(frm.doc.si));
    }
        if((frm.doc.d_1) || (frm.doc.d_2)|| (frm.doc.d_3)|| (frm.doc.d_4)|| (frm.doc.d_5)|| (frm.doc.d_6) || (frm.doc.d_7) || 
        (frm.doc.d_8) || (frm.doc.d_9)|| (frm.doc.d_10)|| (frm.doc.d_11)|| (frm.doc.d_12)|| (frm.doc.d_13) || (frm.doc.d_14)||
        (frm.doc.d_15) || (frm.doc.d_16)|| (frm.doc.d_17)|| (frm.doc.d_18)|| (frm.doc.d_19)|| (frm.doc.d_20) || (frm.doc.d_21)){
        frm.set_value("mark_obtained_b", flt(frm.doc.d_1)+flt(frm.doc.d_2)+flt(frm.doc.d_3)+flt(frm.doc.d_4)+flt(frm.doc.d_5)+flt(frm.doc.d_6)+flt(frm.doc.d_7)+flt(frm.doc.d_8)+flt(frm.doc.d_9)+flt(frm.doc.d_10)+
        flt(frm.doc.d_11)+flt(frm.doc.d_12)+flt(frm.doc.d_13)+flt(frm.doc.d_14)+flt(frm.doc.d_15)+flt(frm.doc.d_16)+flt(frm.doc.d_17)+flt(frm.doc.d_18)+flt(frm.doc.d_19)+flt(frm.doc.d_20)+flt(frm.doc.d_21));
    }
        if((frm.doc.clit_1) || (frm.doc.clit_2)|| (frm.doc.clit_3)|| (frm.doc.clit_4)|| (frm.doc.clit_5)|| (frm.doc.clit_6) || (frm.doc.clit_7)){
        frm.set_value("mark_obtained_c", flt(frm.doc.clit_1)+flt(frm.doc.clit_2)+flt(frm.doc.clit_3)+flt(frm.doc.clit_4)+flt(frm.doc.clit_5)+flt(frm.doc.clit_6)+flt(frm.doc.clit_7));
    }
        if((frm.doc.safe_1) || (frm.doc.safe_2)|| (frm.doc.safe_3)|| (frm.doc.safe_4)|| (frm.doc.safe_5)|| (frm.doc.safe_6) || (frm.doc.safe_7)){
        frm.set_value("mark_obtained_d", flt(frm.doc.safe_1)+flt(frm.doc.safe_2)+flt(frm.doc.safe_3)+flt(frm.doc.safe_4)+flt(frm.doc.safe_5)+flt(frm.doc.safe_6)+flt(frm.doc.safe_7));
    }
        if((frm.doc.work_1) || (frm.doc.work_2)|| (frm.doc.work_3)|| (frm.doc.work_4)|| (frm.doc.wotk_5)|| (frm.doc.work_6) || (frm.doc.work_7)){
        frm.set_value("mark_obtained_e", flt(frm.doc.work_1)+flt(frm.doc.work_2)+flt(frm.doc.work_3)+flt(frm.doc.work_4)+flt(frm.doc.wotk_5)+flt(frm.doc.work_6)+flt(frm.doc.work_7));
    }
        if((frm.doc.f1) || (frm.doc.f2)|| (frm.doc.f3)|| (frm.doc.f4)|| (frm.doc.f5)|| (frm.doc.f6) || (frm.doc.f7)){
        frm.set_value("mark_obtained_f", flt(frm.doc.f1)+flt(frm.doc.f2)+flt(frm.doc.f3)+flt(frm.doc.f4)+flt(frm.doc.f5)+flt(frm.doc.f6)+flt(frm.doc.f7));
    }
        if((frm.doc.s1) || (frm.doc.s2)|| (frm.doc.s3)){
        frm.set_value("mark_obtained_g", flt(frm.doc.s1)+flt(frm.doc.s2)+flt(frm.doc.s3));
    }
        if((frm.doc.zs) || (frm.doc.rh)|| (frm.doc.cch)){
        frm.set_value("mark_obtained_h", flt(frm.doc.zs)+flt(frm.doc.rh)+flt(frm.doc.cch));
    }
        if((frm.doc.productivity) || (frm.doc.work_quality)|| (frm.doc.discipline) || (frm.doc.attendance) ){
        frm.set_value("mark_obatained_i", flt(frm.doc.productivity)+flt(frm.doc.work_quality)+flt(frm.doc.discipline) +flt(frm.doc.attendance));
    }
        if((frm.doc.b_1) || (frm.doc.b_2)|| (frm.doc.b_3) || (frm.doc.b_4) || (frm.doc.b_5)|| (frm.doc.b_6)){ 
        frm.set_value("mark_obtained_j", flt(frm.doc.b_1)+flt(frm.doc.b_2)+flt(frm.doc.b_3)+flt(frm.doc.b_4) +flt(frm.doc.b_5) +flt(frm.doc.b_6));
    }
        if((frm.doc.mark_obtained_a) || (frm.doc.mark_obtained_b)|| (frm.doc.mark_obtained_c)|| (frm.doc.mark_obtained_d)|| (frm.doc.mark_obtained_e)|| (frm.doc.mark_obtained_f) || (frm.doc.mark_obtained_g) || (frm.doc.mark_obtained_h) || (frm.doc.mark_obatained_i) ||(frm.doc.mark_obtained_j) ){       
        frm.set_value("total_practical_mark_obtained", flt(frm.doc.mark_obtained_a)+flt(frm.doc.mark_obtained_b)+flt(frm.doc.mark_obtained_c)+flt(frm.doc.mark_obtained_d)+flt(frm.doc.mark_obtained_e)+flt(frm.doc.mark_obtained_f)+flt(frm.doc.mark_obtained_g)+flt(frm.doc.mark_obtained_h)+flt(frm.doc.mark_obatained_i)+flt(frm.doc.mark_obtained_j));
    }
   }

});
