from rasa_sdk import Action
from rasa_sdk.events import FollowupAction, EventType
from rasa_sdk.events import SlotSet
from rasa_sdk.events import ActionReverted
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from .api_calls import ApiCalls
from . import error_constants
from . import message_constants
from . import other_constants
from .api_return_code import ApiResponse
import json
from .utils import Utils


class ActionAskPoType(Action):
    """Action for calling the 'GetInfo' API to get the type of POs that the user is allowed to make."""

    def name(self):
        return "action_ask_po_type"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # getting result from API -->
        api = ApiCalls()

        is_success, msg, button_list = api.get_po_type(api_host=api_host,
                                                       company_id=company_id,
                                                       user_id=user_id,
                                                       location_id=location_id,
                                                       client_code=client_code)

        # display the result to user -->
        if is_success:
            dispatcher.utter_button_message(msg, button_list)
        else:
            dispatcher.utter_message(error_constants.PO_MAKING_NOT_ALLOWED_ERROR)
            return [FollowupAction('action_restart')]

        return []


class ActionUpdatePoMetaData(Action):
    """Action for updating the metadata required for making the PO"""

    def name(self):
        return "action_update_po_meta_data"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->

        # STOPPING VALIDATION CUZ THIS IS SILENT ACTION
        user_id = tracker.get_slot("user_id")
        # if user_id is None or not user_id:
        #     dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
        #     return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        # if company_id is None or not company_id:
        #     dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
        #     return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        # if location_id is None or not location_id:
        #     dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
        #     return [FollowupAction('action_restart')]

        # if there is no metadata then fill the basic info in it -->
        po_meta_data = tracker.get_slot('po_meta_data')
        if po_meta_data is None or not po_meta_data:
            basic_info_data = {
                'company_Id': company_id,
                "location_Id": location_id,
                "user_Id": user_id
            }
            po_meta_data = json.dumps(basic_info_data)
            po_meta_data_dic = json.loads(po_meta_data)
        else:
            po_meta_data_dic = json.loads(po_meta_data)

        # now just access the slots and put them into the metadata -->

        po_type = tracker.get_slot('po_type')
        if po_type and 'po_type' not in po_meta_data_dic:
            po_meta_data_dic['po_type'] = po_type

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code and 'po_type_code' not in po_meta_data_dic:
            po_meta_data_dic['po_type_code'] = po_type_code

        po_vendor_name = tracker.get_slot('po_vendor_name')
        if po_vendor_name and 'po_vendor_name' not in po_meta_data_dic:
            po_meta_data_dic['po_vendor_name'] = po_vendor_name

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code and 'po_vendor_name_code' not in po_meta_data_dic:
            po_meta_data_dic['po_vendor_name_code'] = po_vendor_name_code

        po_vendor_bill_address = tracker.get_slot('po_vendor_bill_address')
        if po_vendor_bill_address:
            po_meta_data_dic['po_vendor_bill_address'] = po_vendor_bill_address

        po_vendor_bill_address_code = tracker.get_slot('po_vendor_bill_address_code')
        if po_vendor_bill_address_code:
            po_meta_data_dic['po_vendor_bill_address_code'] = po_vendor_bill_address_code

        po_vendor_ship_address = tracker.get_slot('po_vendor_ship_address')
        if po_vendor_ship_address:
            po_meta_data_dic['po_vendor_ship_address'] = po_vendor_ship_address

        po_vendor_ship_address_code = tracker.get_slot('po_vendor_ship_address_code')
        if po_vendor_ship_address_code:
            po_meta_data_dic['po_vendor_ship_address_code'] = po_vendor_ship_address_code

        po_vendor_pay_terms = tracker.get_slot('po_vendor_pay_terms')
        if po_vendor_pay_terms:
            po_meta_data_dic['po_vendor_pay_terms'] = po_vendor_pay_terms

        po_vendor_pay_terms_code = tracker.get_slot('po_vendor_pay_terms_code')
        if po_vendor_pay_terms_code:
            po_meta_data_dic['po_vendor_pay_terms_code'] = po_vendor_pay_terms_code

        po_vendor_dispatch_mode = tracker.get_slot('po_vendor_dispatch_mode')
        if po_vendor_dispatch_mode:
            po_meta_data_dic['po_vendor_dispatch_mode'] = po_vendor_dispatch_mode

        po_vendor_dispatch_mode_code = tracker.get_slot('po_vendor_dispatch_mode_code')
        if po_vendor_dispatch_mode_code:
            po_meta_data_dic['po_vendor_dispatch_mode_code'] = po_vendor_dispatch_mode_code

        po_vendor_currency = tracker.get_slot('po_vendor_currency')
        if po_vendor_currency:
            po_meta_data_dic['po_vendor_currency'] = po_vendor_currency

        po_vendor_currency_code = tracker.get_slot('po_vendor_currency_code')
        if po_vendor_currency_code:
            po_meta_data_dic['po_vendor_currency_code'] = po_vendor_currency_code

        # more slot access here -->
        #
        #
        # ...

        po_meta_data = json.dumps(po_meta_data_dic)

        return [SlotSet('po_meta_data', po_meta_data)]


class VendorNameForm(FormAction):
    """Form action for getting the vendor name from user"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "vendor_name_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["raw_vendor_name"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "raw_vendor_name": self.from_text()
        }

    def validate_raw_vendor_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value.casefold() == "/abort_ywjvcnq".casefold():
            return {"raw_vendor_name": value}

        """Validate raw_vendor_name value."""

        # validating the slots -->
        api_host = tracker.get_slot("api_host")

        user_id = tracker.get_slot("user_id")

        company_id = tracker.get_slot("company_id")

        location_id = tracker.get_slot("location_id")

        client_code = tracker.get_slot("client_code")

        api = ApiCalls()
        api_response, msg, button_list = api.get_vendor_list(raw_vendor_name=value,
                                                             api_host=api_host,
                                                             company_id=company_id,
                                                             user_id=user_id,
                                                             location_id=location_id,
                                                             client_code=client_code)
        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            return {"raw_vendor_name": value}
        elif api_response is ApiResponse.SUCCESS_NO_DATA or api_response is ApiResponse.NO_DATA_400:
            dispatcher.utter_message(message_constants.ASK_PO_VENDOR_NAME_AGAIN)
            return {"raw_vendor_name": None}
        else:
            return {"raw_vendor_name": value}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        raw_vendor_name = tracker.get_slot('raw_vendor_name')

        if raw_vendor_name.casefold() == "/abort_ywjvcnq".casefold():
            return [FollowupAction('action_abort')]

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, msg, button_list = api.get_vendor_list(raw_vendor_name=raw_vendor_name,
                                                             api_host=api_host,
                                                             company_id=company_id,
                                                             user_id=user_id,
                                                             location_id=location_id,
                                                             client_code=client_code)
        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            return []
        else:
            dispatcher.utter_message(error_constants.PO_GET_VENDOR_LIST_API_ERROR)
            return [FollowupAction('action_restart')]


class ActionListVendorNames(Action):
    """Action for listing the vendor names available based on the previously asked raw_vendor_name"""

    def name(self):
        return "action_list_vendor_names"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        raw_vendor_name = tracker.get_slot('raw_vendor_name')
        if raw_vendor_name is None or not raw_vendor_name:
            dispatcher.utter_message(error_constants.RAW_VENDOR_NAME_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, msg, button_list = api.get_vendor_list(raw_vendor_name=raw_vendor_name,
                                                             api_host=api_host,
                                                             company_id=company_id,
                                                             user_id=user_id,
                                                             location_id=location_id,
                                                             client_code=client_code)
        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            dispatcher.utter_button_message(msg, button_list)
            return []
        elif api_response is ApiResponse.SUCCESS_NO_DATA or api_response is ApiResponse.NO_DATA_400:
            dispatcher.utter_message(error_constants.RAW_VENDOR_NAME_NOT_PROVIDED)
            return [FollowupAction('action_restart')]
        else:
            dispatcher.utter_message(error_constants.PO_GET_VENDOR_LIST_API_ERROR)
            return [FollowupAction('action_restart')]


class ActionShowDefaultVendorAttributeValues(Action):
    """Action for showing user the default values associated with the selected vendor"""

    def name(self):
        return "action_show_default_vendor_attribute_values"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # get default vendor info result from API -->
        api = ApiCalls()
        is_success, msg, slots_to_set = api.get_default_vendor_attribute_values(api_host=api_host,
                                                                                company_id=company_id,
                                                                                user_id=user_id,
                                                                                location_id=location_id,
                                                                                client_code=client_code,
                                                                                po_vendor_name_code=po_vendor_name_code,
                                                                                po_type_code=po_type_code)
        if is_success:
            dispatcher.utter_message(msg)
            return [SlotSet(dic['slot_key'], dic['slot_value']) for dic in slots_to_set]
        else:
            dispatcher.utter_message(error_constants.DEFAULT_VENDOR_VALUES_NOT_FOUND)
            return [FollowupAction('action_restart')]


class ActionListPossibleValues(Action):
    """Action for listing the possible values of the attribute of vendor that the user wanted to change"""

    def name(self):
        return "action_list_possible_values"

    def run(self, dispatcher, tracker, domain):
        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_attribute_to_change = tracker.get_slot('po_vendor_attribute_to_change')
        if po_vendor_attribute_to_change is None or not po_vendor_attribute_to_change:
            dispatcher.utter_message(error_constants.PO_VENDOR_ATTRIBUTE_TO_CHANGE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # getting result form api -->
        api = ApiCalls()
        is_success, msg, button_list = api.get_the_attribute_value_list(api_host=api_host,
                                                                        company_id=company_id,
                                                                        user_id=user_id,
                                                                        location_id=location_id,
                                                                        client_code=client_code,
                                                                        po_vendor_name_code=po_vendor_name_code,
                                                                        po_vendor_attribute_to_change=po_vendor_attribute_to_change)
        if is_success:
            dispatcher.utter_button_message(msg, button_list)
        else:
            dispatcher.utter_message(error_constants.VENDOR_VALUES_TO_CHANGE_NOT_FOUND)
            return [FollowupAction('action_restart')]

        return []


class ActionUpdatePoVendorAttributeValue(Action):
    """Action for updating the corresponding slots in case
     if the user change some attribute value of the selected vendor"""

    def name(self):
        return "action_update_po_vendor_attribute_value"

    def run(self, dispatcher, tracker, domain):

        po_vendor_attribute_to_change = tracker.get_slot('po_vendor_attribute_to_change')
        po_vendor_attribute_value_to_change = tracker.get_slot('po_vendor_attribute_value_to_change')
        po_vendor_attribute_value_code_to_change = tracker.get_slot('po_vendor_attribute_value_code_to_change')
        if po_vendor_attribute_to_change == "BILL_ADDRESS_LIST":
            return [SlotSet('po_vendor_bill_address', po_vendor_attribute_value_to_change),
                    SlotSet('po_vendor_bill_address_code', po_vendor_attribute_value_code_to_change)]
        elif po_vendor_attribute_to_change == "SHIP_ADDRESS_LIST":
            return [SlotSet('po_vendor_ship_address', po_vendor_attribute_value_to_change),
                    SlotSet('po_vendor_ship_address_code', po_vendor_attribute_value_code_to_change)]
        elif po_vendor_attribute_to_change == "PAY_TERMS_LIST":
            return [SlotSet('po_vendor_pay_terms', po_vendor_attribute_value_to_change),
                    SlotSet('po_vendor_pay_terms_code', po_vendor_attribute_value_code_to_change)]
        elif po_vendor_attribute_to_change == "DISPATCH_MODE_LIST":
            return [SlotSet('po_vendor_dispatch_mode', po_vendor_attribute_value_to_change),
                    SlotSet('po_vendor_dispatch_mode_code', po_vendor_attribute_value_code_to_change)]
        elif po_vendor_attribute_to_change == "CURRENCY_LIST":
            return [SlotSet('po_vendor_currency', po_vendor_attribute_value_to_change),
                    SlotSet('po_vendor_currency_code', po_vendor_attribute_value_code_to_change)]
        else:
            return []


class ActionListItemTypeOrActivity(Action):
    """Action for asking the user Item Type or Activity"""

    def name(self):
        return "action_list_item_type_or_activity"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()

        if str(po_type_code).casefold() == 'J'.casefold():
            is_success, msg, button_list = api.get_activity_list(api_host=api_host,
                                                                 company_id=company_id,
                                                                 user_id=user_id,
                                                                 location_id=location_id,
                                                                 client_code=client_code,
                                                                 po_vendor_name_code=po_vendor_name_code)

            if is_success:
                dispatcher.utter_button_message(msg, button_list)
            else:
                dispatcher.utter_message(error_constants.PO_ACTIVITY_LIST_NOT_FOUND)
                return [FollowupAction('action_restart')]
        elif str(po_type_code).casefold() == 'M'.casefold():
            is_success, msg, button_list = api.get_item_type_list(api_host=api_host,
                                                                  company_id=company_id,
                                                                  user_id=user_id,
                                                                  location_id=location_id,
                                                                  client_code=client_code,
                                                                  po_vendor_name_code=po_vendor_name_code)

            if is_success:
                dispatcher.utter_button_message(msg, button_list)
            else:
                dispatcher.utter_message(error_constants.PO_ITEM_TYPE_LIST_NOT_FOUND)
                return [FollowupAction('action_restart')]
        else:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        return []


class RemarksForm(FormAction):
    """Form action for getting remarks from user"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "remarks_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["remarks"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "remarks": self.from_text()
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        remarks = tracker.get_slot('remarks')

        if remarks.casefold() == "/abort_ywjvcnq".casefold():
            return [FollowupAction('action_abort')]

        # raw_vendor_name = tracker.get_slot('raw_vendor_name')
        #
        # # utter submit template
        # dispatcher.utter_message(f"Alright! Validating the supplier name {raw_vendor_name}...")

        return []


class ActionQuitPo(Action):
    """Action for quitting the po making process"""

    def name(self):
        return "action_quit_po"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(message_constants.PO_PROCESS_ENDED)

        return [FollowupAction('action_restart')]


class ActionListPossibleCurrencyValues(Action):
    """Action for listing the possible currency values"""

    def name(self):
        return "action_list_possible_currency_values"

    def run(self, dispatcher, tracker, domain):
        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # getting result form api -->
        api = ApiCalls()
        is_success, msg, button_list = api.get_currency_list(api_host=api_host,
                                                             company_id=company_id,
                                                             user_id=user_id,
                                                             location_id=location_id,
                                                             client_code=client_code,
                                                             po_vendor_name_code=po_vendor_name_code)
        if is_success:
            dispatcher.utter_button_message(msg, button_list)
        else:
            dispatcher.utter_message(error_constants.PO_CURRENCY_LIST_NOT_FOUND)
            return [FollowupAction('action_restart')]

        return []


class ConversionRateForm(FormAction):
    """Form action for getting the conversion rate from user"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "conversion_rate_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["conversion_rate"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "conversion_rate": self.from_text()
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        conversion_rate = tracker.get_slot('conversion_rate')

        if conversion_rate.casefold() == "/abort_ywjvcnq".casefold():
            return [FollowupAction('action_abort')]

        return []


class ActionListPoDetailType(Action):
    """Action for listing the item type (in case of po only) to the user"""

    def name(self):
        return "action_list_po_detail_type"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        is_success, msg, button_list = api.get_po_detail_type(api_host=api_host,
                                                              company_id=company_id,
                                                              user_id=user_id,
                                                              location_id=location_id,
                                                              client_code=client_code)
        if is_success:
            dispatcher.utter_button_message(msg, button_list)
        else:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_LIST_NOT_FOUND)
            return [FollowupAction('action_restart')]

        return []


class PoDetailTypeRawNumberForm(FormAction):
    """Form action for getting the po detail type number (e.g. IND/XXX) from the user"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "po_detail_type_raw_number_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["po_detail_type_raw_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "po_detail_type_raw_number": self.from_text()
        }

    # def validate_po_detail_type_raw_number(
    #         self,
    #         value: Text,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate po_detail_type_raw_number's value from the api"""
    #
    #     if value.lower() in self.cuisine_db():
    #         # validation succeeded, set the value of the "cuisine" slot to value
    #         return {"cuisine": value}
    #     else:
    #         dispatcher.utter_message(template="utter_wrong_cuisine")
    #         # validation failed, set this slot to None, meaning the
    #         # user will be asked for the slot again
    #         return {"cuisine": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        po_detail_type_raw_number = tracker.get_slot('po_detail_type_raw_number')

        if po_detail_type_raw_number.casefold() == "/abort_ywjvcnq".casefold():
            return [FollowupAction('action_abort')]

        return []


class ActionListPoDetailTypeNumber(Action):
    """Action for listing the item type (in case of po only) to the user"""

    def name(self):
        return "action_list_po_detail_type_number"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_item_type_code = tracker.get_slot('po_item_type_code')
        po_activity_code = tracker.get_slot('po_activity_code')
        if (po_item_type_code is None and po_activity_code is None) or (not po_item_type_code and not po_activity_code):
            dispatcher.utter_message(error_constants.PO_ITEM_OR_ACTIVITY_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_code = tracker.get_slot('po_detail_type_code')
        if po_detail_type_code is None or not po_detail_type_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_raw_number = tracker.get_slot('po_detail_type_raw_number')
        if po_detail_type_raw_number is None or not po_detail_type_raw_number:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_RAW_NUMBER_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, msg, button_list = api.get_po_detail_type_number_list(api_host=api_host,
                                                                            company_id=company_id,
                                                                            user_id=user_id,
                                                                            location_id=location_id,
                                                                            client_code=client_code,
                                                                            po_type_code=po_type_code,
                                                                            po_item_type_code=po_item_type_code,
                                                                            po_activity_code=po_activity_code,
                                                                            po_vendor_name_code=po_vendor_name_code,
                                                                            po_detail_type_code=po_detail_type_code,
                                                                            po_detail_type_raw_number=po_detail_type_raw_number)
        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            dispatcher.utter_button_message(msg, button_list)
            return [SlotSet('wish_to_continue', 'yes')]
        elif api_response is ApiResponse.SUCCESS_NO_DATA or api_response is ApiResponse.NO_DATA_400:
            dispatcher.utter_message(message_constants.ASK_PO_DETAIL_TYPE_NUMBER_AGAIN)
            return [SlotSet('po_detail_type_raw_number', None), SlotSet('wish_to_continue', 'no')]
        else:
            dispatcher.utter_message(error_constants.PO_GET_DETAIL_TYPE_NUMBER_LIST_API_ERROR)
            return [FollowupAction('action_restart')]


class ActionListTopThree(Action):
    """Action for listing the top three I/J/O for that vendor"""

    def name(self):
        return "action_list_top_three"

    def run(self, dispatcher, tracker, domain):
        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_item_type_code = tracker.get_slot('po_item_type_code')
        po_activity_code = tracker.get_slot('po_activity_code')


        if (po_item_type_code is None and po_activity_code is None ) or (not po_item_type_code and not po_activity_code):
            dispatcher.utter_message(error_constants.PO_ITEM_OR_ACTIVITY_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]


        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # po_detail_type = tracker.get_slot('po_detail_type')
        # if po_detail_type is None or not po_detail_type:
        #     dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
        #     return [FollowupAction('action_restart')]

        po_detail_type_code = tracker.get_slot('po_detail_type_code')
        if po_detail_type_code is None or not po_detail_type_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, msg, button_list = api.get_top_three_po_detail_type_number_list(api_host=api_host,
                                                                                      company_id=company_id,
                                                                                      user_id=user_id,
                                                                                      location_id=location_id,
                                                                                      client_code=client_code,
                                                                                      po_type_code=po_type_code,
                                                                                      po_item_type_code=po_item_type_code,
                                                                                      po_activity_code=po_activity_code,
                                                                                      po_vendor_name_code=po_vendor_name_code,
                                                                                      po_detail_type_code=po_detail_type_code)
        enter_manually_button = {
            "title": "SEARCH MANUALLY",
            "payload": '/inform{"enter_manually": "yes"}'
        }

        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            button_list.append(enter_manually_button)
            dispatcher.utter_button_message(msg, button_list)
            return [SlotSet('po_detail_type_raw_number', None)]
        elif api_response is ApiResponse.SUCCESS_NO_DATA or api_response is ApiResponse.NO_DATA_400:
            msg = message_constants.NO_TOP_THREE_RESULT
            button_list.append(enter_manually_button)
            dispatcher.utter_button_message(msg, button_list)
            return [SlotSet('po_detail_type_raw_number', None)]
        else:
            dispatcher.utter_message(error_constants.PO_LIST_TOP_THREE_API_ERROR)
            return [FollowupAction('action_restart')]


class ActionGetItemDetailsPopupUser(Action):
    """Action for getting the item details from the api and showing it to the user in a popup"""

    def name(self):
        return "action_get_item_details_popup_user"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_code = tracker.get_slot('po_detail_type_code')
        if po_detail_type_code is None or not po_detail_type_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_number_code = tracker.get_slot('po_detail_type_number_code')
        if po_detail_type_number_code is None or not po_detail_type_number_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_NUMBER_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_item_type_code = tracker.get_slot('po_item_type_code')
        po_activity_code = tracker.get_slot('po_activity_code')
        if (po_item_type_code is None and po_activity_code is None) or (not po_item_type_code and not po_activity_code):
            dispatcher.utter_message(error_constants.PO_ITEM_OR_ACTIVITY_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, item_details = api.get_item_details(api_host=api_host,
                                                          company_id=company_id,
                                                          user_id=user_id,
                                                          location_id=location_id,
                                                          client_code=client_code,
                                                          po_vendor_name_code=po_vendor_name_code,
                                                          po_detail_type_code=po_detail_type_code,
                                                          po_detail_type_number_code=po_detail_type_number_code,
                                                          po_item_type_code=po_item_type_code,
                                                          po_activity_code=po_activity_code,
                                                          po_type_code=po_type_code)

        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            dispatcher.utter_message("Please click below to fill item details:")
            dispatcher.utter_custom_json({
                "data": {
                    "type": "popup",
                    "text": "ITEM DETAILS",
                    "payload": item_details
                }
            })
            return [SlotSet('wish_to_continue', 'yes')]
        elif api_response is ApiResponse.SUCCESS_NO_DATA or api_response is ApiResponse.NO_DATA_400:
            dispatcher.utter_message(message_constants.NO_DATA_HERE)
            return [SlotSet('wish_to_continue', 'no')]
        else:
            dispatcher.utter_message(error_constants.PO_GET_ITEM_DETAILS_API_ERROR)
            return [FollowupAction('action_restart')]


class ActionUtterAskForMoreItemDetails(Action):
    """Action for calling the 'GetInfo' API to get the type of POs that the user is allowed to make."""

    def name(self):
        return "action_utter_ask_for_more_item_details"

    def run(self, dispatcher, tracker, domain):

        util = Utils()
        is_success, payload = util.get_metadata(tracker=tracker, data_key='payload')
        if is_success:

            dispatcher.utter_message(template='utter_ask_for_more_item_details')

            selected_items = payload
            return [SlotSet('selected_items', selected_items)]
        else:
            dispatcher.utter_message(error_constants.PO_SELECTED_ITEMS_NOT_PROVIDED)
            return [FollowupAction('action_restart')]


class ActionSavePo(Action):
    """Action for getting the item details from the api and showing it to the user in a popup"""

    def name(self):
        return "action_save_po"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(message_constants.SAVING_PO)

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_code = tracker.get_slot('po_detail_type_code')
        if po_detail_type_code is None or not po_detail_type_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_number_code = tracker.get_slot('po_detail_type_number_code')
        if po_detail_type_number_code is None or not po_detail_type_number_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_NUMBER_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_item_type_code = tracker.get_slot('po_item_type_code')
        po_activity_code = tracker.get_slot('po_activity_code')
        if (po_item_type_code is None and po_activity_code is None) or (not po_item_type_code and not po_activity_code):
            dispatcher.utter_message(error_constants.PO_ITEM_OR_ACTIVITY_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_bill_address_code = tracker.get_slot('po_vendor_bill_address_code')
        if po_vendor_bill_address_code is None or not po_vendor_bill_address_code:
            dispatcher.utter_message(error_constants.PO_VENDOR_BILL_ADDRESS_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_ship_address_code = tracker.get_slot('po_vendor_ship_address_code')
        if po_vendor_ship_address_code is None or not po_vendor_ship_address_code:
            dispatcher.utter_message(error_constants.PO_VENDOR_SHIP_ADDRESS_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_pay_terms_code = tracker.get_slot('po_vendor_pay_terms_code')
        if po_vendor_pay_terms_code is None or not po_vendor_pay_terms_code:
            dispatcher.utter_message(error_constants.PO_VENDOR_PAY_TERMS_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_dispatch_mode_code = tracker.get_slot('po_vendor_dispatch_mode_code')
        if po_vendor_dispatch_mode_code is None or not po_vendor_dispatch_mode_code:
            dispatcher.utter_message(error_constants.PO_VENDOR_DISPATCH_MODE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_currency_code = tracker.get_slot('po_vendor_currency_code')
        if po_vendor_currency_code is None or not po_vendor_currency_code:
            dispatcher.utter_message(error_constants.PO_VENDOR_CURRENCY_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_code = tracker.get_slot('po_detail_type_code')
        if po_detail_type_code is None or not po_detail_type_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_detail_type_number_code = tracker.get_slot('po_detail_type_number_code')
        if po_detail_type_number_code is None or not po_detail_type_number_code:
            dispatcher.utter_message(error_constants.PO_DETAIL_TYPE_NUMBER_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        remarks = tracker.get_slot('remarks')
        if remarks is None or not remarks:
            dispatcher.utter_message(error_constants.PO_REMARKS_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        conversion_rate = tracker.get_slot('conversion_rate')
        if conversion_rate is None or not conversion_rate:
            conversion_rate = 1

        # util = Utils()
        # is_success, payload = util.get_metadata(tracker=tracker, data_key='payload')
        # if is_success:
        #     selected_items = payload
        # else:
        #     dispatcher.utter_message(error_constants.PO_SELECTED_ITEMS_NOT_PROVIDED)
        #     return [FollowupAction('action_restart')]

        selected_items = tracker.get_slot('selected_items')
        if selected_items is None or not selected_items:
            dispatcher.utter_message(error_constants.PO_SELECTED_ITEMS_NOT_SET)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        api_response, msg, final_po_id = api.save_po(api_host=api_host,
                                                     company_id=company_id,
                                                     user_id=user_id,
                                                     location_id=location_id,
                                                     client_code=client_code,
                                                     po_type_code=po_type_code,
                                                     po_vendor_name_code=po_vendor_name_code,
                                                     po_vendor_bill_address_code=po_vendor_bill_address_code,
                                                     po_vendor_ship_address_code=po_vendor_ship_address_code,
                                                     po_vendor_pay_terms_code=po_vendor_pay_terms_code,
                                                     po_vendor_dispatch_mode_code=po_vendor_dispatch_mode_code,
                                                     po_item_type_code=po_item_type_code,
                                                     po_activity_code=po_activity_code,
                                                     remarks=remarks,
                                                     po_vendor_currency_code=po_vendor_currency_code,
                                                     conversion_rate=conversion_rate,
                                                     po_detail_type_code=po_detail_type_code,
                                                     po_detail_type_number_code=po_detail_type_number_code,
                                                     selected_items=selected_items)

        if api_response is ApiResponse.SUCCESS_WITH_DATA:
            dispatcher.utter_message(msg)
            pdf_api_response, pdf_msg = api.make_pdf(api_host=api_host,
                                                     company_id=company_id,
                                                     user_id=user_id,
                                                     location_id=location_id,
                                                     client_code=client_code,
                                                     final_po_id=final_po_id)
            if pdf_api_response is ApiResponse.SUCCESS_WITH_DATA:
                dispatcher.utter_message(pdf_msg)
                return []
            else:
                dispatcher.utter_message(pdf_msg)
                return [FollowupAction('action_restart')]
        else:
            dispatcher.utter_message(msg)
            return [FollowupAction('action_restart')]

class ActionValidateSetItemTypeOrActivity(Action):

    """Action for asking the user Item Type or Activity"""

    def name(self):
        return "action_validate_set_item_type_or_activity"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_type_code = tracker.get_slot('po_type_code')
        if po_type_code is None or not po_type_code:
            dispatcher.utter_message(error_constants.PO_TYPE_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
        if po_vendor_name_code is None or not po_vendor_name_code:
            dispatcher.utter_message(error_constants.VENDOR_NAME_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()
        user_entered_item_or_activity_entity = tracker.get_slot("po_item_or_activity_entity")
        activities_dict = api.get_activity_item_list_dict(api_host=api_host,
                                                                 requirement="ACTIVITY_LIST",
                                                                 company_id=company_id,
                                                                 user_id=user_id,
                                                                 location_id=location_id,
                                                                 client_code=client_code,
                                                                 po_vendor_name_code=po_vendor_name_code)

        items_dict = api.get_activity_item_list_dict(api_host=api_host,
                                                                 requirement="ITEM_TYPE_LIST",
                                                                 company_id=company_id,
                                                                 user_id=user_id,
                                                                 location_id=location_id,
                                                                 client_code=client_code,
                                                                 po_vendor_name_code=po_vendor_name_code)

        print("Activity list dict recieved from get_activity_item_list_dict() function: \n", list(activities_dict.keys()))
        print("Items list dict recieved from get_activity_item_list_dict() function: \n",list(items_dict.keys()))
        if len(list(activities_dict.keys())) == 0 and len( list(activities_dict.keys())) == 0:
            dispatcher.utter_message("No activity or item type could be found in the database!")
            return [FollowupAction('action_restart')]


        if user_entered_item_or_activity_entity:
                for key in activities_dict.keys():
                    if user_entered_item_or_activity_entity.lower().strip() == key.lower().strip():
                        dispatcher.utter_message(f"User entered activity  name taken as {key}")
                        return [SlotSet("po_activity", key), SlotSet("po_activity_code", activities_dict[key])]
                for key in items_dict.keys():
                    if user_entered_item_or_activity_entity.lower().strip() == key.lower().strip():
                        dispatcher.utter_message(f"User entered item name taken as {key}")
                        return [SlotSet("po_item_type", key), SlotSet("po_item_type_code", items_dict[key])]
                dispatcher.utter_message(f"Invalid activity or item name was entered by the name {user_entered_item_or_activity_entity}")
                dispatcher.utter_message("Choose from the given options for the current user ")
                return [FollowupAction('action_list_item_type_or_activity')]
        else:
            dispatcher.utter_message("Activity or Item name couldn't be identified. Please Select a value from below")
            return [FollowupAction('action_list_item_type_or_activity')]


class ActionValidateSetPOType(Action):
    """Action for calling the 'GetInfo' API to get the type of POs that the user is allowed to make."""

    def name(self):
        return "action_validate_set_po_type"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # getting result from API -->
        api = ApiCalls()

        po_types_dict = api.get_po_type_info_dict(api_host = api_host,
                                       company_id = company_id,
                                       user_id = user_id,
                                       location_id = location_id,
                                       client_code = client_code)

        # display the result to user -->
        user_entered_po_type = tracker.get_slot(("po_type"))

        if not user_entered_po_type:
            user_entered_item_or_activity_entity = tracker.get_slot("po_item_or_activity_entity")
            po_vendor_name_code = tracker.get_slot('po_vendor_name_code')
            if po_vendor_name_code is None or not po_vendor_name_code:
                dispatcher.utter_message("Vendor name not valid. Couldn't fetch any valid vendor code for entered vendor!")
                dispatcher.utter_message("Please enter your query with correct vendor name.")
                return [FollowupAction('action_restart')]

            activities_dict = api.get_activity_item_list_dict(api_host=api_host,
                                                              requirement="ACTIVITY_LIST",
                                                              company_id=company_id,
                                                              user_id=user_id,
                                                              location_id=location_id,
                                                              client_code=client_code,
                                                              po_vendor_name_code=po_vendor_name_code)

            items_dict = api.get_activity_item_list_dict(api_host=api_host,
                                                         requirement="ITEM_TYPE_LIST",
                                                         company_id=company_id,
                                                         user_id=user_id,
                                                         location_id=location_id,
                                                         client_code=client_code,
                                                         po_vendor_name_code=po_vendor_name_code)

            user_entered_entity_type = determine_user_entered_entity_type(user_entered_item_or_activity_entity, activities_dict, items_dict)
            if user_entered_entity_type == "activity":
                user_entered_po_type = "jobwork"
            elif user_entered_entity_type == "item":
                user_entered_po_type = "purchase"
            else:
                pass

        if user_entered_po_type:
            valid_key_found = False
            if len(po_types_dict.keys()) != 0:
                for key in po_types_dict.keys():
                    if user_entered_po_type.lower() in key.lower() or key.lower() in user_entered_po_type.lower():
                        user_entered_po_type = key
                        valid_key_found = True
                        break
            if valid_key_found:
                dispatcher.utter_message(str("Entered PO type taken to be "+user_entered_po_type))
                return [SlotSet('po_type', user_entered_po_type), SlotSet('po_type_code', po_types_dict[user_entered_po_type])]
        else:
            dispatcher.utter_message(error_constants.PO_MAKING_NOT_ALLOWED_ERROR)
            return [FollowupAction('action_restart')]

class ActionValidateSetPODetailType(Action):
    """Action for calling the 'GetInfo' API to get the type of POs that the user is allowed to make."""

    def name(self):
        return "action_validate_set_po_detail_type"

    def run(self, dispatcher, tracker, domain):

        # validating the slots -->
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        company_id = tracker.get_slot("company_id")
        if company_id is None or not company_id:
            dispatcher.utter_message(error_constants.COMPANY_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        client_code = tracker.get_slot("client_code")
        if client_code is None or not client_code:
            dispatcher.utter_message(error_constants.CLIENT_CODE_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        location_id = tracker.get_slot("location_id")
        if location_id is None or not location_id:
            dispatcher.utter_message(error_constants.LOCATION_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        # getting result from API -->
        api = ApiCalls()

        po_detail_types_dict = api.get_po_detail_list_dict(api_host = api_host,
                                       company_id = company_id,
                                       user_id = user_id,
                                       location_id = location_id,
                                       client_code = client_code)

        # display the result to user -->
        user_entered_po_detail_type = tracker.get_slot(("po_detail_type"))
        po_item_or_activity_entity_type = tracker.get_slot(("po_item_or_activity_entity_type"))
        if po_item_or_activity_entity_type:
            if po_item_or_activity_entity_type =="activity":
                user_entered_po_detail_type="jobwork"
            else:
                user_entered_po_detail_type = "purchase"


        valid_key_found = False
        if len(po_detail_types_dict.keys()) != 0:
            for key in po_detail_types_dict.keys():
                if user_entered_po_detail_type.lower() in key.lower():
                    user_entered_po_detail_type = key
                    valid_key_found = True
                    break
        if valid_key_found:
            dispatcher.utter_message(str("Entered PO detail type taken to be "+user_entered_po_detail_type))
            return [SlotSet('po_detail_type', user_entered_po_detail_type), SlotSet('po_detail_type_code', po_detail_types_dict[user_entered_po_detail_type])]
        else:
            dispatcher.utter_message(error_constants.PO_MAKING_NOT_ALLOWED_ERROR)
            return [FollowupAction('action_restart')]


def determine_user_entered_entity_type(user_entered_item_or_activity_entity, activities_dict, items_dict):

    print("Activity list dict recieved from get_activity_item_list_dict() function: \n", list(activities_dict.keys()))
    print("Items list dict recieved from get_activity_item_list_dict() function: \n", list(items_dict.keys()))
    if len(list(activities_dict.keys())) == 0 and len(list(activities_dict.keys())) == 0:
        print("No activity or item type could be found in the database!. User entered entity type couldn't be determined in determine_user_entered_entity_type()")
        return "unknown"

    for key in activities_dict.keys():
        if user_entered_item_or_activity_entity.lower().strip() == key.lower().strip():
            return "activity"
    for key in items_dict.keys():
        if user_entered_item_or_activity_entity.lower().strip() == key.lower().strip():
            return "item"

        return "unknown"



