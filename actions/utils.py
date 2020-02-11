from typing import Tuple, Any, Optional
from rasa_sdk import Tracker


class Utils:
    """Some utility functions"""

    def idx_range_between_last_and_second_last__restart(self, tracker: Tracker) -> Tuple[int, int]:
        """
        If the conversation has not been restarted, ``0`` is returned."""

        count = 0
        last_event_index = 0
        second_last_event_index = 0
        for i, event in enumerate(reversed(tracker.events)):
            if event['event'] == 'action' and event['name'] == 'action_restart' and count == 0:
                last_event_index = len(tracker.events) - i
                count += 1
                continue
            if event['event'] == 'action' and event['name'] == 'action_restart' and count == 1:
                second_last_event_index = len(tracker.events) - i
                break
        return second_last_event_index, last_event_index

    def get_valid_activity_name(self, activity_name: str) -> str:
        activity_names = {
            'FABRIC_IN_HOUSE': ['fabric in house'],
            'CUTTING': ['cutting'],
            'PRINT_EMB': ['print emb', 'print', 'emb', 'embroidery', 'printing'],
            'SEWING': ['sewing'],
            'WASHING': ['washing'],
            'FINISHING': ['finishing'],
            'DISPATCH': ['dispatch', 'dispatching'],
            'GATE_PASS': ['gate pass', 'gate passing'],
            'GRN': ['grn'],
        }
        for k, v in activity_names.items():
            if activity_name in v:
                return k
        return activity_name

    def get_metadata(self, tracker: Tracker, data_key: str) -> Tuple[bool, Any]:
        events = tracker.current_state().get('events')
        # events = tracker.events_after_latest_restart()
        for i in reversed(events):
            # print("")
            # print("======================== AN EVENT =========================")
            # print(i)
            # print("===========================================================")
            # print("")
            if i.get('event') == 'user' and 'metadata' in i:
                custom_data = i.get('metadata')
                # print("")
                # print("======================== METADATA =====================")
                # print(custom_data)
                # print("=======================================================")
                # print("")
                if custom_data and data_key in custom_data:
                    return True, custom_data.get(data_key)
        return False, None

    def make_int_or_none(self, num) -> Optional[int]:
        try:
            return int(num)
        except TypeError:
            return None
