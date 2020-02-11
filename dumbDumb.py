# from rasa.core.actions.action import ActionDefaultFallback
# import requests
#
# from rasa.core.trackers import DialogueStateTracker
#
# from rasa.core.actions.action import (  # pytype: disable=pyi-error
#         ACTION_LISTEN_NAME,
#     )
#
# # url = 'http://rdpl1.cloudapp.net:8094/Service1.svc/GetPODetails/{}/test48'.format(po_number)
# # url = 'http://rdpl1.cloudapp.net:8094/Service1.svc/GetPODetails/ABCD/test48'
# url = 'http://rdpl1.cloudapp.net:8094/Service1.svc/GetPODetails/5950/test48'
#
#             # result = api.get_po_details(url)
#             #
#             # print(result)
# response = requests.get(url)
#
# print(response.status_code)run actions
# from rasa.core.channels.telegram.py

# import enum
#
#
# class FrontendActions(enum.Enum):
#     SUCCESS_WITH_DATA = 1
#     SUCCESS_NO_DATA = 2
#     NOT_SUCCESS_200 = 3
#     NOT_200 = 4
#     NO_DATA_400 = 5
#     NOT_SUCCESS_400 = 6