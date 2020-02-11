from rasa_sdk import Action
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from .api_calls import ApiCalls
from . import error_constants


class ActionMarkActivityClose(Action):
    """Action for marking a given activity of a given fg code as 'complete'"""

    def name(self):
        return "action_mark_activity_close"

    def run(self, dispatcher, tracker, domain):
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()

        activity_name = tracker.get_slot("activity_name")
        if activity_name is None or not activity_name:
            dispatcher.utter_message(error_constants.ACTIVITY_NAME_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        fg_code = tracker.get_slot("id")
        if fg_code:
            is_final, message, api_user_message = api.mark_activity_close(api_host=api_host,
                                                                          fg_code=fg_code,
                                                                          activity_name=activity_name,
                                                                          user_id=user_id)
            if is_final:
                dispatcher.utter_message(api_user_message)
                # dispatcher.utter_message(message)
                return [SlotSet('has_multi_db_records', 'no')]
            else:
                dispatcher.utter_button_message(api_user_message, message)
                return [SlotSet('has_multi_db_records', 'yes')]
        else:
            dispatcher.utter_message(error_constants.FG_CODE_NOT_PROVIDED)

        return [FollowupAction('action_restart')]


class ActionCloseActivityWithOrderId(Action):
    """Action for closing an activity with a particular order id"""

    def name(self):
        return "action_close_activity_with_order_id"

    def run(self, dispatcher, tracker, domain):
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        api = ApiCalls()

        activity_name = tracker.get_slot("activity_name")
        if activity_name is None or not activity_name:
            dispatcher.utter_message(error_constants.ACTIVITY_NAME_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        order_id = tracker.get_slot("id")
        tna_activity_id = tracker.get_slot('tna_activity_id')
        fg_code = order_id
        if order_id and tna_activity_id:
            is_final, message, api_user_message = api.mark_activity_close(api_host=api_host,
                                                                          fg_code=fg_code,
                                                                          activity_name=activity_name,
                                                                          user_id=user_id,
                                                                          order_id=order_id,
                                                                          tna_activity_id=tna_activity_id)
            if is_final:
                dispatcher.utter_message(api_user_message)
                # dispatcher.utter_message(message)
            else:
                dispatcher.utter_message(error_constants.API_RESULT_NOT_FINAL)
        else:
            dispatcher.utter_message(error_constants.ORDER_OR_TNA_ID_NOT_PROVIDED)

        return [SlotSet('has_multi_db_records', 'no')]
