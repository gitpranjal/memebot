## story_make_po_correct_activity_entered_all_4_po_detail_types_changed_currency_change_denied_item_details_modified_in_multiple_goes
* make_po{"thing_to_make": "po", "raw_vendor_name": "A.V. EXPO FAB", "po_item_or_activity_entity": "Fabric"}
    - slot{"po_item_or_activity_entity": "Fabric"}
    - slot{"raw_vendor_name": "A.V. EXPO FAB"}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_validate_set_po_type
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* affirm
    - utter_ask_what_to_change
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST", "po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi", "po_vendor_attribute_value_code_to_change": "251"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi"}
    - slot{"po_vendor_attribute_value_code_to_change": "251"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST", "po_vendor_attribute_value_to_change": "New Bazar, Meerut, Uttar Pradesh", "po_vendor_attribute_value_code_to_change": "211"}
    - slot{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "New Bazar, Meerut, Uttar Pradesh"}
    - slot{"po_vendor_attribute_value_code_to_change": "211"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "PAY_TERMS_LIST", "po_vendor_attribute_value_to_change": "Within 10 days", "po_vendor_attribute_value_code_to_change": "1"}
    - slot{"po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "Within 10 days"}
    - slot{"po_vendor_attribute_value_code_to_change": "1"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST", "po_vendor_attribute_value_to_change": "By Courier", "po_vendor_attribute_value_code_to_change": "54"}
    - slot{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "By Courier"}
    - slot{"po_vendor_attribute_value_code_to_change": "54"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_validate_set_item_type_or_activity
    - remarks_form
    - form{"name": "remarks_form"}
    - form{"name": null}
    - utter_ask_for_currency_change
* deny
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "Category_30012018//ORD_30012018"}
    - slot{"po_detail_type_number_code": "3955"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3958"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3958"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "Category_30012018//ORD_30012018"}
    - slot{"po_detail_type_number_code": "3955"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3959"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3959"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012018", "po_detail_type_number_code": "3995"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012018"}
    - slot{"po_detail_type_number_code": "3995"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3958"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3958"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_save_po
    - action_restart
    
## stories_correct_po_item_or_activity_entity_entered_initial__1_po_detail_types_changed_currency_changed_item_details_modified_in_two_goes
* make_po{"thing_to_make": "po", "po_type": "PURCHASE ORDER", "raw_vendor_name": "A.V. EXPO FAB", "po_item_or_activity_entity": "Fabric"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_item_or_activity_entity": "Fabric"}
    - slot{"raw_vendor_name": "A.V. EXPO FAB"}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_validate_set_po_type
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* affirm
    - utter_ask_what_to_change
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST", "po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi", "po_vendor_attribute_value_code_to_change": "251"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi"}
    - slot{"po_vendor_attribute_value_code_to_change": "251"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_validate_set_item_type_or_activity
    - remarks_form
    - form{"name": "remarks_form"}
    - form{"name": null}
    - utter_ask_for_currency_change
* affirm
    - action_list_possible_currency_values
* inform{"po_vendor_currency": "USD", "po_vendor_currency_code": "1"}
    - slot{"po_vendor_currency": "USD"}
    - slot{"po_vendor_currency_code": "1"}
    - conversion_rate_form
    - form{"name": "conversion_rate_form"}
    - form{"name": null}
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"enter_manually": "no", "po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3959"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3959"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_save_po
    - action_restart
    
## story_make_po_correct_activity_entered_initial_po_details_not_changed_currency_change_denied_order_entered_item_details_modified_in_two_goes
* make_po{"thing_to_make": "po", "raw_vendor_name": "A.V. EXPO FAB", "po_item_or_activity_entity": "Fabric"}
    - slot{"info_type": "po"}
    - slot{"po_item_or_activity_entity": "Fabric"}
    - slot{"raw_vendor_name": "A.V. EXPO FAB"}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_validate_set_po_type
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* deny{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_validate_set_item_type_or_activity
    - remarks_form
    - form{"name": "remarks_form"}
    - form{"name": null}
    - utter_ask_for_currency_change
* deny
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3958"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3958"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_save_po
    - action_restart

## story_make_po_correct_activity_entered_initial_po_details_not_changed_currency_changed_item_details_modified_in_two_goes
* make_po{"thing_to_make": "po", "raw_vendor_name": "A.V. EXPO FAB", "po_item_or_activity_entity": "Fabric"}
    - slot{"po_item_or_activity_entity": "Fabric"}
    - slot{"raw_vendor_name": "A.V. EXPO FAB"}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_validate_set_po_type
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* deny{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_validate_set_item_type_or_activity
    - remarks_form
    - form{"name": "remarks_form"}
    - form{"name": null}
    - utter_ask_for_currency_change
* affirm
    - action_list_possible_currency_values
* inform{"po_vendor_currency": "USD", "po_vendor_currency_code": "1"}
    - slot{"po_vendor_currency": "USD"}
    - slot{"po_vendor_currency_code": "1"}
    - conversion_rate_form
    - form{"name": "conversion_rate_form"}
    - form{"name": null}
    - action_list_po_detail_type
* inform{"po_detail_type": "Order", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3958"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3958"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_save_po
    - action_restart
    
## story_make_po_incorrect_activity_type_entered_all_4_initial_po_details_changed_currency_change_denied_item_details_modified_in_multiple_goes
* make_po{"thing_to_make": "po", "po_type": "PURCHASE ORDER", "raw_vendor_name":"A.V. EXPO FAB", "po_item_or_activity_entity":"Fabric" }
    - slot{"po_item_or_activity_entity": "Fabric"}
    - slot{"raw_vendor_name": "A.V. EXPO FAB"}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_validate_set_po_type
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* affirm
    - utter_ask_what_to_change
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST", "po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi", "po_vendor_attribute_value_code_to_change": "251"}
    - slot{"po_vendor_attribute_to_change": "BILL_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "Okhla, Phase 1, New Delhi"}
    - slot{"po_vendor_attribute_value_code_to_change": "251"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST", "po_vendor_attribute_value_to_change": "New Bazar, Meerut, Uttar Pradesh", "po_vendor_attribute_value_code_to_change": "211"}
    - slot{"po_vendor_attribute_to_change": "SHIP_ADDRESS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "New Bazar, Meerut, Uttar Pradesh"}
    - slot{"po_vendor_attribute_value_code_to_change": "211"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "PAY_TERMS_LIST", "po_vendor_attribute_value_to_change": "Within 10 days", "po_vendor_attribute_value_code_to_change": "1"}
    - slot{"po_vendor_attribute_to_change": "PAY_TERMS_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "Within 10 days"}
    - slot{"po_vendor_attribute_value_code_to_change": "1"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "no", "po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - slot{"wish_to_continue": "no"}
    - slot{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - action_list_possible_values
* inform{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST", "po_vendor_attribute_value_to_change": "By Courier", "po_vendor_attribute_value_code_to_change": "54"}
    - slot{"po_vendor_attribute_to_change": "DISPATCH_MODE_LIST"}
    - slot{"po_vendor_attribute_value_to_change": "By Courier"}
    - slot{"po_vendor_attribute_value_code_to_change": "54"}
    - action_update_po_vendor_attribute_value
    - utter_ask_wanna_change_more_or_continue
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_validate_set_item_type_or_activity
    - slot{"show_correct_item_activity_button_list": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_or_activity_entity": "Fabric Purchase", "po_item_or_activity_entity_code": "20"}
    - slot{"po_item_or_activity_entity": "Fabric Purchase"}
    - slot{"po_item_or_activity_entity_code": "20"}
    - utter_ask_fg_code
    - remarks_form
    - form{"name": "remarks_form"}
    - form{"name": null}
    - utter_ask_for_currency_change
* deny
    - action_list_po_detail_type
* inform{"po_detail_type": "Order", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Order", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Order", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* affirm
    - action_list_po_detail_type
* inform{"po_detail_type": "Order", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_save_po
    - action_restart
    