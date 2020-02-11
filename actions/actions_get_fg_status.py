from rasa_sdk import Action
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from .api_calls import ApiCalls
from .utils import Utils
from . import error_constants


class ActionFetchFGStatusUtterResult(Action):
    """Action for fetching the fg status by calling the api and then showing that result."""

    def name(self):
        return "action_fetch_fg_status_utter_result"

    def run(self, dispatcher, tracker, domain):
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return []

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return []

        utils = Utils()
        api = ApiCalls()

        activity_name = tracker.get_slot("activity_name")
        if activity_name:
            activity_name = utils.get_valid_activity_name(activity_name)

        fg_code = tracker.get_slot("id")
        if fg_code:
            is_final, message, api_user_message = api.get_fg_status(api_host=api_host,
                                                                    fg_code=fg_code,
                                                                    user_id=user_id,
                                                                    activity_name=activity_name)
            if is_final:
                if api_user_message:
                    dispatcher.utter_message(api_user_message)
                dispatcher.utter_message(message)
                return [SlotSet('has_multi_db_records', 'no')]
            else:
                dispatcher.utter_button_message(api_user_message, message)
                return [SlotSet('has_multi_db_records', 'yes')]
        else:
            dispatcher.utter_message(error_constants.FG_CODE_NOT_PROVIDED)

        return []


class ActionGetFGWithOrderId(Action):
    """Action for getting the dpr status with a particular order id"""

    def name(self):
        return "action_get_fg_with_order_id"

    def run(self, dispatcher, tracker, domain):
        api_host = tracker.get_slot("api_host")
        if api_host is None or not api_host:
            dispatcher.utter_message(error_constants.API_HOST_NOT_PROVIDED)
            return []

        user_id = tracker.get_slot("user_id")
        if user_id is None or not user_id:
            dispatcher.utter_message(error_constants.USER_ID_NOT_PROVIDED)
            return []

        api = ApiCalls()
        utils = Utils()

        activity_name = tracker.get_slot("activity_name")
        if activity_name:
            activity_name = utils.get_valid_activity_name(activity_name)

        order_id = tracker.get_slot("id")
        fg_code = order_id
        if order_id:
            is_final, message, api_user_message = api.get_fg_status(api_host=api_host,
                                                                    fg_code=fg_code,
                                                                    user_id=user_id,
                                                                    activity_name=activity_name,
                                                                    order_id=order_id)
            if is_final:
                if api_user_message:
                    dispatcher.utter_message(api_user_message)
                dispatcher.utter_message(message)
            else:
                dispatcher.utter_message(error_constants.API_RESULT_NOT_FINAL)
        else:
            dispatcher.utter_message(error_constants.ORDER_ID_NOT_PROVIDED)

        return [SlotSet('has_multi_db_records', 'no')]
