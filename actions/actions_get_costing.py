from rasa_sdk import Action
from rasa_sdk.events import FollowupAction
from .api_calls import ApiCalls
from . import error_constants


class ActionGetCosting(Action):
    """get costing for user input string containing garment description"""

    def name(self):
        return "action_get_costing"

    def run(self, dispatcher, tracker, domain):

        ccid = tracker.get_slot('ccid')
        if ccid is None or not ccid:
            dispatcher.utter_message(error_constants.CCID_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        cost_user = tracker.get_slot('cost_user')
        if cost_user is None or not cost_user:
            dispatcher.utter_message(error_constants.COST_USER_NOT_PROVIDED)
            return [FollowupAction('action_restart')]

        url = "http://bluekaktus.ml/costing_api"

        api = ApiCalls()

        message_obtained = tracker.latest_message["text"].lower()

        if "costing" in message_obtained:
            user_garment_text_description = message_obtained.split("costing")[-1]
            dispatcher.utter_message(str("Alright! getting costing information for " + user_garment_text_description))
            costing_result = api.get_costing_data(url,
                                                  user_garment_text_description,
                                                  company_id=ccid,
                                                  username=cost_user)

            if not costing_result or costing_result == "no such garment" or costing_result == "invalid company id or user id":
                dispatcher.utter_message(
                    str("Sorry! costing engine couldn't find any information for " + user_garment_text_description))
                return [FollowupAction('action_restart')]

            keys_order = ["FABRIC", "CMT", "TRIMS", "PACKING", "VALUE ADDITION", "TOTAL_COST", "LINK"]

            table_draft = ["ITEM | Price", ":--- | ---:"]
            link = ""
            for key in keys_order:
                if key == "LINK":
                    link = costing_result[key]
                    continue
                table_draft.append(f'{key} | {costing_result[key]}')
            final_message = "  \n".join(table_draft) + "  \n"
            final_message += "Click here for[ detailed costing information](" + link + ")"
            dispatcher.utter_message(final_message)

        return [FollowupAction('action_restart')]
