from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from .utils import Utils
from . import frontend_constants
from . import message_constants
import random
import yagmail

#pip3 install “python-socketio<4.3” “python-engineio<3.9” for resolving socket problem with webchat, which gives bit under training

class ActionUtterChitchat(Action):
    """Revertible mapped action for chitchat"""

    def name(self):
        return "action_utter_chitchat"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_chitchat", tracker)

        return [FollowupAction('action_restart')]

class ActionShowImage(Action):
    """action for image showing"""

    def name(self):
        return "action_utter_meme"

    def run(self, dispatcher, tracker, domain):
        politics = ["https://www.dropbox.com/s/gl5irprdfbtfouq/photo_2020-02-12_16-36-25.jpg?raw=1",
                    "https://www.dropbox.com/s/dayzbbll4ppjxxr/photo_2020-02-12_16-36-51.jpg?raw=1",
                    "https://www.dropbox.com/s/m14dqkevxnsyzh4/photo_2020-02-12_16-36-56.jpg?raw=1",
                    "https://www.dropbox.com/s/w2joicvfofhg8fv/photo_2020-02-12_16-37-01.jpg?raw=1"]

        programming = ["https://www.dropbox.com/s/9a67qicpo4puz6m/photo_2020-02-12_16-39-09.jpg?raw=1",
                       "https://www.dropbox.com/s/2t0thy3ekupv470/photo_2020-02-12_16-39-15.jpg?raw=1",
                       "https://www.dropbox.com/s/wlwmzbik70ipc2p/photo_2020-02-12_16-39-20.jpg?raw=1",
                       "https://www.dropbox.com/s/zauwwhbgx7xnylk/photo_2020-02-13_12-28-07.jpg?raw=1"]

        mixed =["https://www.dropbox.com/s/u6xazv3pjkjznsy/download.jpg?dl=0",
                 "https://www.dropbox.com/s/xnrysju407fj1o0/photo_2020-02-13_12-28-16.jpg?raw=1",
                 "https://www.dropbox.com/s/krdv5xhc3v71lxa/photo_2020-02-13_12-28-20.jpg?raw=1"]+politics+programming


        genre = tracker.get_slot(("genre"))
        if genre == "politics":
            dispatcher.utter_image_url(random.choice(politics))
        elif genre == "programming":
            dispatcher.utter_image_url(random.choice(politics))
        else:
            dispatcher.utter_image_url(random.choice(mixed))


        return [FollowupAction('action_restart')]

class ActionAbort(Action):
    """Action for aborting any story and notifying user about it."""

    def name(self):
        return "action_abort"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(message_constants.PROCESS_ABORTED)

        return [FollowupAction('action_restart')]


class ActionRaiseTicketSilently(Action):
    """Action for raising_ticket/sending_email when the user has had previous conversation with the bot."""

    def name(self):
        return "action_raise_ticket_silently"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("Alright! hold on, I'm notifying the support team...")

        """ Code for getting custom data from frontend """
        company_name = str(tracker.get_slot('company_name'))
        project_name = str(tracker.get_slot('project_name'))
        user_name = str(tracker.get_slot('user_name'))
        user_email = str(tracker.get_slot('user_email'))

        utils = Utils()

        """ Code for getting the latest conversation log for raising ticket """
        # print("========================\n")
        # print(tracker.current_state())
        # print("========================\n")
        #
        # print("========EVENTS=======EVENTS============\n")
        # print(list(reversed(tracker.events)))
        # print("=======================================\n")
        second_last_restart_index, last_restart_index = utils.idx_range_between_last_and_second_last__restart(tracker)
        eve = tracker.events[second_last_restart_index:last_restart_index]

        """ Drafting the email """
        email_draft = []
        email_draft.append("Company Name: " + company_name + '\n')
        email_draft.append("Project Name: " + project_name + '\n')
        email_draft.append("User Name: " + user_name + '\n')
        email_draft.append("User Email: " + user_email + '\n')
        email_draft.append('\n')
        email_draft.append('\n')
        email_draft.append('Last Conversation Log: ' + '\n')
        email_draft.append('\n')
        for i in eve:
            if i['event'] == 'user':
                email_draft.append("<strong>" + user_name + "</strong>: " + i['text'] + '\n')
                # print("user:", i['text'], '\n')
            elif i['event'] == 'bot':
                email_draft.append("<strong>Mili</strong>: " + i['text'] + '\n')
                # print("bot:", i['text'])

        """ Code for sending mail to support team """
        # Connect to smtp server.
        yag_smtp_connection = yagmail.SMTP(user="rdpl.mili@gmail.com", password="Bluekaktus@1A", host='smtp.gmail.com')
        # Subject of the email
        subject = '[Mili] User query of ' + company_name
        # Content of the email.
        contents = email_draft
        # Sending the email
        yag_smtp_connection.send(['rdpl.mili+p1@gmail.com',
                                  'sumit.jain@bluekaktus.com'
                                  ],
                                 subject,
                                 contents,
                                 cc='sajeev@bluekaktus.com'
                                 )

        """ Notifying the user about the sent email. """
        dispatcher.utter_message("I have notified the **Support Team**.  \nThey'll contact you shortly.\n")

        return [FollowupAction('action_restart')]


class ActionRestart(Action):
    """A custom restart action which prevents slot reset of a few unfeaturized slots"""

    def name(self) -> Text:
        return 'action_restart'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """ Collecting slots which should not be reset """
        company_name = tracker.get_slot('company_name')
        project_name = tracker.get_slot('project_name')
        user_name = tracker.get_slot('user_name')
        user_email = tracker.get_slot('user_email')
        user_id = tracker.get_slot('user_id')
        api_host = tracker.get_slot('api_host')
        ccid = tracker.get_slot('ccid')
        cost_user = tracker.get_slot('cost_user')
        company_id = tracker.get_slot('company_id')
        location_id = tracker.get_slot('location_id')
        client_code = tracker.get_slot('client_code')

        clear_po_cache = {
            "data": {
                "type": "action",
                "component": "",
                "subComponent": "",
                "payload": {
                    "actionType": frontend_constants.CLEAR_PO_CACHE
                }
            }
        }
        dispatcher.utter_message(json_message=clear_po_cache)

        return [Restarted(),
                SlotSet('company_name', company_name),
                SlotSet('project_name', project_name),
                SlotSet('user_name', user_name),
                SlotSet('user_email', user_email),
                SlotSet('user_id', user_id),
                SlotSet('api_host', api_host),
                SlotSet('ccid', ccid),
                SlotSet('cost_user', cost_user),
                SlotSet('company_id', company_id),
                SlotSet('location_id', location_id),
                SlotSet('client_code', client_code),
                ]


class ActionDefaultFallback(Action):
    """Mapped action for fallback"""

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_for_fallback_inform", tracker)

        return [FollowupAction('action_restart')]


class ActionResetAllSlots(Action):
    """Action for total restart wiping the bot's memory clean."""

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
