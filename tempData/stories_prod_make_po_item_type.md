## story_make_po_default_change_currency_change_item_type_no_select_from_top_three_save_on_search_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "no"}
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
* inform{"po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
    - slot{"po_detail_type_number_value": "Category_30012018//ORD_30012018"}
    - slot{"po_detail_type_number_code": "3955"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
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
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "ORD_30012017", "po_detail_type_number_code": "3956"}
    - slot{"po_detail_type_number_value": "ORD_30012017"}
    - slot{"po_detail_type_number_code": "3956"}
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
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "yes"}
* affirm
    - action_show_other_charges_popup_button
    - slot{"is_other_charges": "yes"}
* inform{"is_other_charges": "yes"}
    - slot{"is_other_charges": "yes"}
    - action_retrieve_other_charges
    - action_save_po
    - action_restart

## story_make_po_default_change_currency_change_item_type_select_from_top_three_and_save_on_some_top_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "Category_30012018", "po_detail_type_number_code": "3959"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "Category_30012018"}
    - slot{"po_detail_type_number_code": "3959"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "yes"}
* affirm
    - action_show_other_charges_popup_button
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_currency_change_item_type_select_from_top_three_and_save_on_search_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Indent No", "po_detail_type_code": "I"}
    - slot{"po_detail_type": "Indent No"}
    - slot{"po_detail_type_code": "I"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
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
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "yes"}
* deny
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_no_select_from_top_three_save_on_search_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
    - slot{"wish_to_continue": "no"}
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
* inform{"po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
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
* inform{"po_detail_type_number_value": "ORD_30012017", "po_detail_type_number_code": "3956"}
    - slot{"po_detail_type_number_value": "ORD_30012017"}
    - slot{"po_detail_type_number_code": "3956"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_select_from_top_three_save_on_search_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
    - slot{"po_detail_type_code": "O"}
    - action_list_top_three
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Job No", "po_detail_type_code": "J"}
    - slot{"po_detail_type": "Job No"}
    - slot{"po_detail_type_code": "J"}
    - action_list_top_three
* inform{"enter_manually": "yes"}
    - slot{"enter_manually": "yes"}
    - po_detail_type_raw_number_form
    - form{"name": "po_detail_type_raw_number_form"}
    - form{"name": null}
    - action_list_po_detail_type_number
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "ORD_30012017", "po_detail_type_number_code": "3956"}
    - slot{"po_detail_type_number_value": "ORD_30012017"}
    - slot{"po_detail_type_number_code": "3956"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_select_from_top_three_save_on_some_top_result_1
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
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
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_currency_change_item_type_select_from_top_three_save_on_search_result_2
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
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
* inform{"po_detail_type_number_value": "ORD_30012017", "po_detail_type_number_code": "3956"}
    - slot{"po_detail_type_number_value": "ORD_30012017"}
    - slot{"po_detail_type_number_code": "3956"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_select_from_top_result_save_on_some_top_result_2
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "no"}
    - action_list_po_detail_type
* inform{"po_detail_type": "Order No", "po_detail_type_code": "O"}
    - slot{"po_detail_type": "Order No"}
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
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_currency_change_item_type_no_top_three_select_3
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
    - slot{"wish_to_continue": "yes"}
* inform{"po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
    - slot{"po_detail_type_number_value": "Category_30012018//ORD_30012018"}
    - slot{"po_detail_type_number_code": "3955"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_3
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
* inform{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_currency_change_item_type_4
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_default_change_no_currency_change_item_type_4
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
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
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"po_detail_type_number_value": "Category_30012018//ORD_30012018", "po_detail_type_number_code": "3955"}
    - slot{"po_detail_type_number_value": "Category_30012018//ORD_30012018"}
    - slot{"po_detail_type_number_code": "3955"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_no_default_change_currency_change_item_type_5
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* deny{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart

## story_make_po_happy_path_item_type
* make_po{"thing_to_make": "po"}
    - action_ask_po_type
* inform{"po_type": "PURCHASE ORDER", "po_type_code": "M"}
    - slot{"po_type": "PURCHASE ORDER"}
    - slot{"po_type_code": "M"}
    - vendor_name_form
    - form{"name": "vendor_name_form"}
    - form{"name": null}
    - action_list_vendor_names
* inform{"po_vendor_name": "A.V. EXPO FAB", "po_vendor_name_code": "1499"}
    - slot{"po_vendor_name": "A.V. EXPO FAB"}
    - slot{"po_vendor_name_code": "1499"}
    - action_show_default_vendor_attribute_values
    - utter_ask_wanna_change_default
* deny{"wish_to_continue": "yes"}
    - slot{"wish_to_continue": "yes"}
    - action_list_item_type_or_activity
* inform{"po_item_type": "Fabric", "po_item_type_code": "1"}
    - slot{"po_item_type": "Fabric"}
    - slot{"po_item_type_code": "1"}
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
* inform{"enter_manually": "no", "po_detail_type_number_value": "ORD_30012020", "po_detail_type_number_code": "3978"}
    - slot{"enter_manually": "no"}
    - slot{"po_detail_type_number_value": "ORD_30012020"}
    - slot{"po_detail_type_number_code": "3978"}
    - action_get_item_details_popup_user
    - slot{"wish_to_continue": "yes"}
* inform
    - action_utter_ask_for_more_item_details
* deny
    - action_utter_ask_for_other_charges
    - slot{"is_other_charges": "no"}
    - action_save_po
    - action_restart
