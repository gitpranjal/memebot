from typing import Any, List, Tuple, Optional
import requests
from . import error_constants
from . import message_constants
from . import other_constants
from .api_return_code import ApiResponse
import logging
import json
from .utils import Utils
import uuid

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler('rasa_api_calls_info.log')
file_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
file_formater = logging.Formatter(
    '%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(funcName)s - %(message)s')
file_handler.setFormatter(file_formater)

# Add handlers to the logger
logger.addHandler(file_handler)


class ApiCalls:
    """A class with different methods for calling different APIs and returning data."""

    def make_pdf(self,
                 api_host: str,
                 company_id: str,
                 user_id: str,
                 location_id: str,
                 client_code: str,
                 final_po_id: str) -> Tuple[ApiResponse, str]:
        """
        get the pdf content from hitting the pdf api and save it to a file.
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :param final_po_id: the id returned by the save po api
        :return: api response, link or error message
        """

        url = f"{api_host}/api/Chatbot/GetPOPdf"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "po_Details": {
                "po_mt": {
                    "po_id": int(final_po_id)
                }
            }
        }

        response = requests.post(url=url, json=data)
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/octet-stream':
            # filename = str(response.headers['Content-Disposition']).split('=')[-1]
            filename = f"po_{str(uuid.uuid4().hex)}.pdf"
            # po_dir = other_constants.SERVER_PDF_PO_STATIC_DIR  # live
            po_dir = other_constants.LOCAL_PDF_PO_STATIC_DIR  # local
            with open(f'{po_dir}/{filename}', 'wb') as file:
                file.write(response.content)
            generated_file_link = f"http://13.67.41.38/media/pdf/po/{filename}"
            msg = f"[View PO]({generated_file_link})"
            logger.info(
                f"Print PDF API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response headers: {response.headers}\n")
            return ApiResponse.SUCCESS_WITH_DATA, msg
        else:
            logger.info(
                f"Print PDF API response code not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response headers: {response.headers}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, error_constants.PRINT_PDF_API_ERROR

    def save_po(self,
                api_host: str,
                company_id: str,
                user_id: str,
                location_id: str,
                client_code: str,
                po_type_code: str,
                po_vendor_name_code: str,
                po_vendor_bill_address_code: str,
                po_vendor_ship_address_code: str,
                po_vendor_pay_terms_code: str,
                po_vendor_dispatch_mode_code: str,
                po_item_type_code: str,
                po_activity_code: str,
                remarks: str,
                po_vendor_currency_code: str,
                conversion_rate: str,
                po_detail_type_code: str,
                po_detail_type_number_code: str,
                selected_items: str) -> Tuple[ApiResponse, str, Optional[str]]:
        """
        save the po by calling the api and return the link to user
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param po_type_code: po (M)/jpo (J)
        :param po_vendor_name_code: the unique id of the supplier
        :param po_vendor_bill_address_code: bill address code of the supplier
        :param po_vendor_ship_address_code: shipping address code of the supplier
        :param po_vendor_pay_terms_code: pay terms code of the supplier
        :param po_vendor_dispatch_mode_code: dispatch mode code of the supplier
        :param po_item_type_code: code of this --> e.g.: Fabric/Trims/Packing/Others
        :param po_activity_code: code of the activity in case of jpo
        :param remarks: the remarks entered by the user
        :param po_vendor_currency_code: the code of the currency that the user selected
        :param conversion_rate: the conversion rate entered by the user
        :param po_detail_type_code: code of this --> e.g.: Indent no./Job no./Order no.
        :param client_code: the client code for identifying the database
        :param po_detail_type_number_code:
        :param selected_items:
        :return: api response type, message, and final_po_id
        """
        util = Utils()
        po_activity_code = util.make_int_or_none(po_activity_code)
        po_item_type_code = util.make_int_or_none(po_item_type_code)

        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/SavePODetails"
        logger.info(f"In function 'save_po', selected_items: {selected_items}\n")
        data = {
            "basic_info": {
                "company_id": int(company_id),
                "location_id": int(location_id),
                "user_id": int(user_id),
                "client_code": str(client_code)
            },
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "po_details": {
                "po_mt": {
                    "po_type": str(po_type_code),
                    "party_id": int(po_vendor_name_code),
                    "pay_terms_id": int(po_vendor_pay_terms_code),
                    "remarks": str(remarks),
                    "dispatch_mode_id": int(po_vendor_dispatch_mode_code),
                    "currency_id": int(po_vendor_currency_code),
                    "curr_rate": str(conversion_rate),
                    "bill_address_id": int(po_vendor_bill_address_code),
                    "ship_address_id": int(po_vendor_ship_address_code),
                    "process_id": po_activity_code,
                    "item_group_type": po_item_type_code
                },
                "po_dt": selected_items
            }
        }

        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                api_data = body['data']
                if api_data:
                    msg = body['message']
                    final_po_id = api_data['po_id']

                    logger.info(
                        f"Save PO API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_WITH_DATA, msg, final_po_id
                else:
                    logger.info(
                        f"Save PO API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_NO_DATA, error_constants.SAVE_PO_API_ERROR, None
            else:
                logger.info(
                    f"Save PO API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_200, error_constants.SAVE_PO_API_ERROR, None
        else:
            logger.info(
                f"Save PO API response code not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, error_constants.SAVE_PO_API_ERROR, None

    def get_item_details(self,
                         api_host: str,
                         company_id: str,
                         user_id: str,
                         location_id: str,
                         client_code: str,
                         po_vendor_name_code: str,
                         po_detail_type_code: str,
                         po_detail_type_number_code: str,
                         po_item_type_code: str,
                         po_activity_code: str,
                         po_type_code: str) -> Tuple[ApiResponse, List]:

        """
        get the item details from API and send it to the frontend for formatting as a POPUP
        :param po_item_type_code: code of this --> e.g.: Fabric/Trims/Packing/Others
        :param po_activity_code: code of the activity (only in case of jpo)
        :param po_type_code: code of this --> po (M)/jpo (J)
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param po_vendor_name_code: the unique id of the selected vendor
        :param po_detail_type_code: Indent no.(I)/Job no.(J)/Order no.(O)
        :param po_detail_type_number_code: the code of the selected I/J/O no., e.g.: for 'IND/XXX' it might be '1231'
        :param client_code: the client code for identifying the database
        :return:
        """

        if po_item_type_code is None:
            po_item_type_code = 0

        if po_activity_code is None:
            po_activity_code = 0

        url = f"{api_host}/api/Chatbot/GetItemDetails"
        data = {
            "basic_info": {
                "company_id": int(company_id),
                "location_id": int(location_id),
                "user_id": int(user_id),
                "client_code": str(client_code)
            },
            "raw_data": {
                "input_code": str(po_detail_type_code),
                "input_value": int(po_detail_type_number_code)
            },
            "party_details": {
                "party_id": int(po_vendor_name_code)
            },
            "po_details": {
                "po_mt": {
                    "item_group_type": int(po_item_type_code),
                    "process_id": int(po_activity_code),
                    "po_type": str(po_type_code)
                }
            }
        }

        response = requests.post(url=url, json=data)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                api_data = body['data']
                if api_data:
                    logger.info(
                        f"Get item details API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_WITH_DATA, api_data
                else:
                    logger.info(
                        f"Get item details API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_NO_DATA, []
            else:
                logger.info(
                    f"Get item details API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_200, []
        elif response.status_code == 400:
            try:
                body = response.json()
                if not body.get('data'):
                    logger.info(
                        f"Get item details API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NO_DATA_400, []
                else:
                    logger.info(
                        f"Get item details API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NOT_SUCCESS_400, []
            except ValueError:
                logger.info(
                    f"Get item details API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_400, []
        else:
            logger.info(
                f"Get item details API response code not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, []

    def get_top_three_po_detail_type_number_list(self,
                                                 api_host: str,
                                                 company_id: str,
                                                 user_id: str,
                                                 location_id: str,
                                                 client_code: str,
                                                 po_type_code: str,
                                                 po_item_type_code: str,
                                                 po_activity_code: str,
                                                 po_vendor_name_code: str,
                                                 po_detail_type_code: str) -> Tuple[ApiResponse, str, List]:
        """
        get the po top three detail type number list which the user can select (e.g. the indent number list)
        :param po_activity_code: e.g. code of activity (cutting/stitching/etc)
        :param po_item_type_code: e.g. code of 'Fabric/Trims/etc.'
        :param po_type_code: M/J
        :param po_vendor_name_code: the unique id of vendor (party_id)
        :param po_detail_type_code: the code of indent_no, job_no, order_no
        :param po_detail_type_raw_number: the raw number entered by user (e.g. IND/XXX)
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        util = Utils()

        po_item_type_code = util.make_int_or_none(po_item_type_code)
        po_activity_code = util.make_int_or_none(po_activity_code)

        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "INPUT_TYPE_LIST",
            "raw_Data": {
                "input_type_code": str(po_detail_type_code),
                "input_type_value": None
            },
            "party_Details": {
                "party_id": str(po_vendor_name_code)
            },
            "po_Details": {
                "po_mt": {
                    "po_type": str(po_type_code),
                    "process_id": po_activity_code,
                    "item_group_type": po_item_type_code
                }
            }
        }

        data = json.dumps(data)

        print(
            "DATA SENT TO PO DETAIL TYPE API TO GET THE ACTUAL PO DETAIL TYPE VALUES IN THE get_top_three_po_detail_type_number_list()#########: \n",
            data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                data = body['data']
                if data:
                    for dic in data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"enter_manually": "no", "po_detail_type_number_value": "{str(dic["Value"])}", "po_detail_type_number_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get top three po detail type number list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_WITH_DATA, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get top three po detail type number list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_NO_DATA, str(body['message']), []
            else:
                logger.info(
                    f"Get top three po detail type number list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_200, str(body['message']), []
        elif response.status_code == 400:
            try:
                body = response.json()
                if not body.get('data'):
                    logger.info(
                        f"Get top three po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NO_DATA_400, str(body.get('message')), []
                else:
                    logger.info(
                        f"Get top three po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NOT_SUCCESS_400, "", []
            except ValueError:
                logger.info(
                    f"Get top three po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_400, "", []
        else:
            logger.info(
                f"Get top three po detail type number list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, "", []

    def get_po_detail_type_number_list(self,
                                       api_host: str,
                                       company_id: str,
                                       user_id: str,
                                       location_id: str,
                                       client_code: str,
                                       po_type_code: str,
                                       po_item_type_code: str,
                                       po_activity_code: str,
                                       po_vendor_name_code: str,
                                       po_detail_type_code: str,
                                       po_detail_type_raw_number: str) -> Tuple[ApiResponse, str, List]:
        """
        get the po detail type number list which the user can select (e.g. the indent number list)
        :param po_activity_code: e.g. code of activity (cutting/stitching/etc)
        :param po_item_type_code: e.g. code of 'Fabric/Trims/etc.'
        :param po_type_code: M/J
        :param po_vendor_name_code: the unique id of vendor (party_id)
        :param po_detail_type_code: the code of indent_no, job_no, order_no
        :param po_detail_type_raw_number: the raw number entered by user (e.g. IND/XXX)
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        util = Utils()

        po_item_type_code = util.make_int_or_none(po_item_type_code)
        po_activity_code = util.make_int_or_none(po_activity_code)

        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "INPUT_TYPE_LIST",
            "raw_Data": {
                "input_type_code": str(po_detail_type_code),
                "input_type_value": str(po_detail_type_raw_number)
            },
            "party_Details": {
                "party_id": str(po_vendor_name_code)
            },
            "po_Details": {
                "po_mt": {
                    "po_type": str(po_type_code),
                    "process_id": po_activity_code,
                    "item_group_type": po_item_type_code
                }
            }
        }
        print("DATA SENT TO PO DETAIL TYPE API TO GET THE ACTUAL PO DETAIL TYPE VALUES IN THE get_po_detail_type_number_list()#########: \n",data )
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                data = body['data']
                if data:
                    for dic in data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_detail_type_number_value": "{str(dic["Value"])}", "po_detail_type_number_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get po detail type number list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_WITH_DATA, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get po detail type number list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_NO_DATA, str(body['message']), []
            else:
                logger.info(
                    f"Get po detail type number list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_200, str(body['message']), []
        elif response.status_code == 400:
            try:
                body = response.json()
                if not body.get('data'):
                    logger.info(
                        f"Get po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NO_DATA_400, str(body.get('message')), []
                else:
                    logger.info(
                        f"Get po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NOT_SUCCESS_400, "", []
            except ValueError:
                logger.info(
                    f"Get po detail type number list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_400, "", []
        else:
            logger.info(
                f"Get po detail type number list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, "", []

    def get_po_detail_type(self,
                           api_host: str,
                           company_id: str,
                           user_id: str,
                           location_id: str,
                           client_code: str) -> Tuple[bool, str, List]:
        """
        get the po detail type list and show it to user
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "PO_INPUT_LIST",
            "raw_data": {},
            "party_details": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_detail_type": "{str(dic["Value"])}", "po_detail_type_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get po detail type API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get po detail type API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), []
            else:
                logger.info(
                    f"Get po detail type API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), []
        else:
            logger.info(
                f"Get po detail type API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", []

    def get_po_detail_list_dict(self,
                          api_host: str,
                          company_id: str,
                          user_id: str,
                          location_id: str,
                          client_code: str,
                         ) :
        """
        returns a dictionary of po_detail_types mapped against their codes
        :param po_vendor_name_code: party_id
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param requirement: ITEM_TYPE_LIST or ACTIVITY_LIST
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """

        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "PO_INPUT_LIST",
            "raw_data": {},
            "party_details": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body["status"] == "success":
                data_dict = {}
                for dic in body["data"]:
                    data_dict[dic["Value"]] = dic["Code"]
                return data_dict

            print("API could not send po detail type names and codes for current user. Request sent is invalid")
            print(body["message"])
            return {}

        print("Internal Server error or invalid URL. Response status: ", response.status_code())
        return {}


    def get_currency_list(self,
                          api_host: str,
                          company_id: str,
                          user_id: str,
                          location_id: str,
                          client_code: str,
                          po_vendor_name_code: str) -> Tuple[bool, str, List]:
        """
        get the item currency list and show it to user
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param po_vendor_name_code: the unique id of the vendor selected by the user
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "CURRENCY_LIST",
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "raw_data": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_vendor_currency": "{str(dic["Value"])}", "po_vendor_currency_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get currency list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get currency list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), []
            else:
                logger.info(
                    f"Get currency list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), []
        else:
            logger.info(
                f"Get currency list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", []

    def get_item_type_list(self,
                           api_host: str,
                           company_id: str,
                           user_id: str,
                           location_id: str,
                           client_code: str,
                           po_vendor_name_code: str) -> Tuple[bool, str, List]:
        """
        get the item type list and show it to user
        :param po_vendor_name_code: party_id
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "ITEM_TYPE_LIST",
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "raw_data": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_item_type": "{str(dic["Value"])}", "po_item_type_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get item type list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get item type list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), []
            else:
                logger.info(
                    f"Get item type list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), []
        else:
            logger.info(
                f"Get item type list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", []

    def get_activity_item_list_dict(self,
                          requirement: str,
                          api_host: str,
                          company_id: str,
                          user_id: str,
                          location_id: str,
                          client_code: str,
                          po_vendor_name_code: str) :
        """
        returns a dictionary of activities mapped against activity codes
        :param po_vendor_name_code: party_id
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param requirement: ITEM_TYPE_LIST or ACTIVITY_LIST
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """

        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": requirement,
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "raw_data": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body["status"] == "success":
                data_dict = {}
                for dic in body["data"]:
                    data_dict[dic["Value"]] = dic["Code"]
                return data_dict

            logger.info(f"API:{url} could not send activity names and codes for current user. POST Request sent was {data}")
        else:
            logger.info(
                f"API:{url} could not send a response with response status not equal to 200. POST Request sent, which was invalid is {data}")
            return {}

        print("Internal Server error or invalid URL. Response status: ", response.status_code())
        return {}


    def get_activity_list(self,
                          api_host: str,
                          company_id: str,
                          user_id: str,
                          location_id: str,
                          client_code: str,
                          po_vendor_name_code: str) -> Tuple[bool, str, List]:
        """
        get the activity list and show it to user
        :param po_vendor_name_code: party_id
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "ACTIVITY_LIST",
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "raw_data": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_activity": "{str(dic["Value"])}", "po_activity_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get activity list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get activity list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), []
            else:
                logger.info(
                    f"Get activity list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), []
        else:
            logger.info(
                f"Get activity list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", []

    def get_the_attribute_value_list(self,
                                     api_host: str,
                                     company_id: str,
                                     user_id: str,
                                     location_id: str,
                                     client_code: str,
                                     po_vendor_name_code: str,
                                     po_vendor_attribute_to_change: str) -> Tuple[bool, str, List]:
        """
        get the different values of the attribute that the user want to change for a particular vendor
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param po_vendor_name_code: the unique id of the vendor name
        :param po_vendor_attribute_to_change: the vendor's attribute's name that the user want to change
        :param client_code: the client code for identifying the database
        :return: success status, message, button list
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": str(po_vendor_attribute_to_change),
            "party_details": {
                "party_id": str(po_vendor_name_code)
            },
            "raw_data": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_vendor_attribute_to_change": "{po_vendor_attribute_to_change}", "po_vendor_attribute_value_to_change": "{str(dic["Value"])}", "po_vendor_attribute_value_code_to_change": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get attribute value list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get attribute value list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), []
            else:
                logger.info(
                    f"Get attribute value list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), []
        else:
            logger.info(
                f"Get attribute value list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", []

    def get_default_vendor_attribute_values(self,
                                            api_host: str,
                                            company_id: str,
                                            user_id: str,
                                            location_id: str,
                                            client_code: str,
                                            po_vendor_name_code: str,
                                            po_type_code: str) -> Tuple[bool, str, List]:
        """
        get the default values for the vendor from the API and send for rendering in proper format
        :param client_code: the client code for identifying the database
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :param po_vendor_name_code: the unique code name of the vendor
        :param po_type_code: the unique code name of the PO Type (E.g. 'M', 'J', etc.)
        :return: success status, properly formatted msg, slot_to_be_set_list
        """

        url = f"{api_host}/api/Chatbot/GetDefaultPartyInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "party_Details": {
                "party_id": str(po_vendor_name_code)
            },
            "po_Details": {
                "po_mt": {
                    "po_type": str(po_type_code)
                }
            }
        }

        slots_to_set = []

        response = requests.post(url=url, json=data)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                msg = str(body['message']) + "  \n"
                api_data = body['data']
                if api_data:
                    for dic in api_data:

                        if str(dic['ATTR_NAME']).casefold() != "Currency".casefold():
                            msg += f"**{str(dic['ATTR_NAME'])}**:  \n{str(dic['ATTR_VALUE'])}\n\n"

                        if str(dic['ATTR_NAME']).casefold() == "Bill Address".casefold():
                            slots_to_set.append({'slot_key': 'po_vendor_bill_address',
                                                 'slot_value': str(dic['ATTR_VALUE'])})
                            slots_to_set.append({'slot_key': 'po_vendor_bill_address_code',
                                                 'slot_value': str(dic['ATTR_ID'])})

                        elif str(dic['ATTR_NAME']).casefold() == "Ship Address".casefold():
                            slots_to_set.append({'slot_key': 'po_vendor_ship_address',
                                                 'slot_value': str(dic['ATTR_VALUE'])})
                            slots_to_set.append({'slot_key': 'po_vendor_ship_address_code',
                                                 'slot_value': str(dic['ATTR_ID'])})

                        elif str(dic['ATTR_NAME']).casefold() == "Pay Terms".casefold():
                            slots_to_set.append({'slot_key': 'po_vendor_pay_terms',
                                                 'slot_value': str(dic['ATTR_VALUE'])})
                            slots_to_set.append({'slot_key': 'po_vendor_pay_terms_code',
                                                 'slot_value': str(dic['ATTR_ID'])})

                        elif str(dic['ATTR_NAME']).casefold() == "Mode of Dispatch".casefold():
                            slots_to_set.append({'slot_key': 'po_vendor_dispatch_mode',
                                                 'slot_value': str(dic['ATTR_VALUE'])})
                            slots_to_set.append({'slot_key': 'po_vendor_dispatch_mode_code',
                                                 'slot_value': str(dic['ATTR_ID'])})

                        elif str(dic['ATTR_NAME']).casefold() == "Currency".casefold():
                            slots_to_set.append({'slot_key': 'po_vendor_currency',
                                                 'slot_value': str(dic['ATTR_VALUE'])})
                            slots_to_set.append({'slot_key': 'po_vendor_currency_code',
                                                 'slot_value': str(dic['ATTR_ID'])})

                        else:
                            msg = f"Vendor default value has an unknown attribute {str(dic['ATTR_NAME'])}"
                            return False, msg, []

                    logger.info(
                        f"Get default vendor attribute values API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, msg, slots_to_set
                else:
                    logger.info(
                        f"Get default vendor attribute values API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, msg, slots_to_set
            else:
                logger.info(
                    f"Get default vendor attribute values API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, "", slots_to_set
        else:
            logger.info(
                f"Get default vendor attribute values API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", slots_to_set

    def get_vendor_list(self,
                        raw_vendor_name: str,
                        api_host: str,
                        company_id: str,
                        user_id: str,
                        location_id: str,
                        client_code: str) -> Tuple[ApiResponse, str, List]:

        """
        hit the 'GetInfo' api with raw vendor name to fetch the list of vendors to display on the frontend
        :param client_code: the client code for identifying the database
        :param raw_vendor_name: the name which the user entered to search for the vendor
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :return: Success status, message, list of buttons to be rendered by the frontend
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "PARTY_LIST",
            "raw_Data": {
                "party_name": str(raw_vendor_name)
            },
            "party_details": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                button_list = []
                api_data = body['data']
                if api_data:
                    for dic in api_data:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_vendor_name": "{str(dic["Value"])}", "po_vendor_name_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get vendor list API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_WITH_DATA, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get vendor list API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.SUCCESS_NO_DATA, error_constants.PO_API_NO_RECORD_FOUND, button_list
            else:
                logger.info(
                    f"Get vendor list API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_200, "", []
        elif response.status_code == 400:
            try:
                body = response.json()
                if not body.get('data'):
                    logger.info(
                        f"Get vendor list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NO_DATA_400, str(body.get('message')), []
                else:
                    logger.info(
                        f"Get vendor list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return ApiResponse.NOT_SUCCESS_400, "", []
            except ValueError:
                logger.info(
                    f"Get vendor list API status 400. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return ApiResponse.NOT_SUCCESS_400, "", []
        else:
            logger.info(
                f"Get vendor list API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return ApiResponse.NOT_200, error_constants.PO_API_ERROR, []

    def get_po_type_info_dict(self,
                    api_host: str,
                    company_id: str,
                    user_id: str,
                    location_id: str,
                    client_code: str) :
        """
        get a dictionary with po types mapped to their respective codes.
        :param client_code: the client code for identifying the database.
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :return: Success status, message, a dictionary of po types mapped against their respective codes
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "PO_TYPE_LIST",
            "raw_data": {},
            "party_details": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }

        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                api_data = body['data']
                if api_data and type(api_data) == list and len(api_data) != 0:
                    data_dic = {}
                    for dic in api_data:
                        data_dic[dic["Value"]] = dic["Code"]
                    return data_dic

                print(f"{api_host}/api/Chatbot/GetInfo", " API could not fetch proper result in the get_po_type_info_dict() function")
                print("API message: ", body["message"])
                return {}

            print(f"{api_host}/api/Chatbot/GetInfo",
                  " API could not fetch proper result in the get_po_type_info_dict() function with response status fail")
            print("API message: ", body["message"])
            return {}

        print(f"{api_host}/api/Chatbot/GetInfo",
              " Internal server error in the API or incorrect URL requested")
        return {}




    def get_po_type(self,
                    api_host: str,
                    company_id: str,
                    user_id: str,
                    location_id: str,
                    client_code: str) -> Tuple[bool, str, List]:
        """
        get the types of po and send properly formatted response back to the user.
        :param client_code: the client code for identifying the database.
        :param api_host: the url where the 'GetInfo' api is hosted, e.g. http://192.168.1.13:86
        :param company_id: ID of the company
        :param user_id: ID of the user
        :param location_id: ID of the location from where the user is trying to access the chatbot
        :return: Success status, message, list of buttons to be rendered by the frontend
        """
        header = {"Content-Type": "application/json"}
        url = f"{api_host}/api/Chatbot/GetInfo"
        data = {
            "basic_Info": {
                "company_Id": int(company_id),
                "location_Id": int(location_id),
                "user_Id": int(user_id),
                "client_code": str(client_code)
            },
            "info_Type": "PO_TYPE_LIST",
            "raw_data": {},
            "party_details": {},
            "po_details": {
                "po_mt": {
                    "po_type": None,
                    "item_group_type": None,
                    "process_id": None
                }
            }
        }

        button_list = []
        # slots_to_set = []
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            body = response.json()
            if body['status'] == 'success':
                api_data = body['data']
                if api_data:
                    for dic in body['data']:
                        button_list.append(
                            {
                                "title": f"{dic['Value']}",
                                "payload": f'/inform{{"po_type": "{str(dic["Value"])}", "po_type_code": "{str(dic["Code"])}"}}'
                            }
                        )
                    logger.info(
                        f"Get PO type API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return True, str(body['message']), button_list
                else:
                    logger.info(
                        f"Get PO type API didn't return data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                    return False, str(body['message']), button_list
            else:
                logger.info(
                    f"Get PO type API status not 'success'. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, str(body['message']), button_list
        else:
            logger.info(
                f"Get PO type API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return False, "", button_list

    def get_dpr_status(self,
                       api_host: str,
                       fg_code: str,
                       user_id: str,
                       activity_name: str = None,
                       order_id: str = None) -> Tuple[Any, Any, Any]:
        """
        Sends a GET request to fetch the dpr status.
        API url is assumed to be known.
        :param order_id: when an order id is passed to the api, the api ignores the fg code and
         returns result based on just the order id and activity name (if given)
        :param api_host: The host where the api is hosted, e.g.: http://192.168.1.13:86
        :param fg_code: str
        :param activity_name: this needs to be a valid activity name which the api can search,
         e.g. 'fabric_in_house' is ok, 'fabric in house' is not ok
        :param user_id: user id of the user (rasa gets this from frontend)
        :return: dpr status table in markdown format, or errors in .md format
        """

        if order_id is not None and activity_name is not None:
            url = f"{api_host}/api/v1/dprstatus?activity={activity_name}&orderId={order_id}&userId={user_id}"
        elif order_id is not None:
            url = f"{api_host}/api/v1/dprstatus?orderId={order_id}&userId={user_id}"
        elif activity_name is not None:
            url = f"{api_host}/api/v1/dprstatus?fgCode={fg_code}&activity={activity_name}&userId={user_id}"
        else:
            url = f"{api_host}/api/v1/dprstatus?fgCode={fg_code}&userId={user_id}"

        response = requests.get(url)
        if response.status_code == 200:
            body = response.json()
            if body['data']['isFinal']:
                table_draft = [
                    "Activity &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Value",
                    ":--- | ---:"
                ]
                for dic in body['data']['actualResult']:
                    table_draft.append(f'{dic["activity"]} | {dic["value"]}')
                logger.info(
                    f"Get DPR Status API returned final data. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
                return True, "  \n".join(table_draft), body['data']['userMessage']
            else:
                button_list = []
                for dic in body['data']['actualResult']:
                    button_list.append(
                        {
                            "title": f"{dic['value']}",
                            "payload": f'/get_dpr_with_order_id{{"id": "{str(dic["orderId"])}"}}'
                        }
                    )
                logger.info(
                    f"Get DPR Status API didn't returned final data. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
                return False, button_list, body['data']['userMessage']

        elif response.status_code == 400:
            logger.info(
                f"Get DPR Status API returned 400 error. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = ""
            return True, "  \n".join(error_list), error_msg

        else:
            logger.info(
                f"Get DPR Status API returned 500 or other error. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = ""
            return True, "  \n".join(error_list), error_msg

    def mark_activity_close(self,
                            api_host: str,
                            fg_code: str,
                            activity_name: str,
                            user_id: str,
                            order_id: str = None,
                            tna_activity_id: str = None) -> Tuple[Any, Any, Any]:
        """
        Sends a post request to update the status of a given fg code's activity as complete.
        :param tna_activity_id: this id indicated the actual record in the bluekaktus' database which we have to mark complete.
        :param order_id: when order_id is given then
        the api is expected to return details of a single db record (fg code)
        :param api_host: the host where the api is hosted, e.g.: http://192.168.1.13:86
        :param fg_code: str
        :param activity_name: should be a valid activity name which the api can search.
        :param user_id: user id (rasa gets this from front-end)
        :return: properly formatted (.md) message
        """

        url = f"{api_host}/api/v1/closeActivity"

        data = {
            "fgCode": f"{fg_code}",
            "activity": f"{activity_name}",
            "userId": f"{user_id}",
            "orderId": order_id if order_id is not None else "0",
            "tna_activity_id": tna_activity_id if tna_activity_id is not None else "0"
        }

        response = requests.post(url=url, data=data)
        if response.status_code == 200:
            body = response.json()
            if body['data']['isFinal']:
                logger.info(
                    f"Mark activity close API returned final data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return True, "", body['data']['userMessage']
            else:
                button_list = []
                for dic in body['data']['actualResult']:
                    button_list.append(
                        {
                            "title": f"{dic['value']}",
                            "payload": f'/close_activity_with_order_id{{"id": "{str(dic["orderId"])}", "tna_activity_id": "{str(dic["tna_activity_id"])}"}}'
                        }
                    )
                logger.info(
                    f"Mark activity close API didn't returned final data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False, button_list, body['data']['userMessage']

        elif response.status_code == 400:
            logger.info(
                f"Mark activity close API returned 400 error. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = "**Validation Error**:  \n"
            return True, "", "  \n".join(error_list),
        else:
            logger.info(
                f"Mark activity close API returned 500 or other error. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = "**API Error**:  \n"
            return True, "", "  \n".join(error_list)

    def get_costing_data(self, url, string_query, company_id, username):
        """sends post request to the costing API and return/receives a json"""

        data = {
            "query": string_query,
            "user_id": username,
            "company_id": company_id

        }
        try:
            response = requests.post(url, json=data)
            # print("Costing engine response status ", response.status_code)
            if response.status_code != 200:
                # print("Api server side error with status code " + str(response.status_code))
                logger.info(
                    f"Get costing data API response not 200. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
                return False
        except Exception as e:
            logger.exception(e)
            logger.info("Get costing data API url not working")
            # print("API url not working")

            return False

        try:
            logger.info(
                f"Get costing data API returned data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return response.json()
        except:
            # print("Response type not convertible to json with response being: ", response.text)
            logger.info(
                f"Get costing data API didn't return properly formatted data. Request Type: POST\nUrl: {url}\nData sent: {data}\nAPI response: {response.text}\n")
            return response.text

    def get_fg_status(self,
                      api_host: str,
                      fg_code: str,
                      user_id: str,
                      activity_name: str = None,
                      order_id: str = None) -> Tuple[Any, Any, Any]:
        """
        Sends a GET request to fetch the dpr status.
        API url is assumed to be known.
        :param order_id: when an order id is passed to the api, the api ignores the fg code and
         returns result based on just the order id and activity name (if given)
        :param api_host: The host where the api is hosted, e.g.:
        :param fg_code: str
        :param activity_name: this needs to be a valid activity name which the api can search,
         e.g. 'fabric_in_house' is ok, 'fabric in house' is not ok
        :param user_id: user id of the user (rasa gets this from frontend)
        :return: fg status table in markdown format, or errors in .md format
        """
        activity_name = None
        if order_id is not None and activity_name is not None:
            url = f"{api_host}/api/v1/fgstatus?activity={activity_name}&orderId={order_id}&userId={user_id}"
        elif order_id is not None:
            url = f"{api_host}/api/v1/fgstatus?fgCode={fg_code}&userId={user_id}&orderId={order_id}"
        elif activity_name is not None:
            url = f"{api_host}/api/v1/fgstatus?fgCode={fg_code}&activity={activity_name}&userId={user_id}"
        else:
            url = f"{api_host}/api/v1/fgstatus?fgCode={fg_code}&userId={user_id}"

        response = requests.get(url)
        if response.status_code == 200:
            body = response.json()
            if body['data']['isFinal']:
                table_draft = [
                    "Activity &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Value",
                    ":--- | ---:"
                ]
                for dic in body['data']['actualResult']:
                    table_draft.append(f'{dic["key"]} | {dic["value"]}')
                logger.info(
                    f"Get FG Status API returned final data. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
                return True, "  \n".join(table_draft), body['data']['userMessage']
            else:
                button_list = []
                for dic in body['data']['actualResult']:
                    button_list.append(
                        {
                            "title": f"{dic['value']}",
                            "payload": f'/get_dpr_with_order_id{{"id": "{str(dic["orderId"])}"}}'
                        }
                    )
                logger.info(
                    f"Get FG Status API didn't return final data. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
                return False, button_list, body['data']['userMessage']

        elif response.status_code == 400:
            logger.info(
                f"Get FG Status API returned error 400. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = ""
            return True, "  \n".join(error_list), error_msg

        else:
            logger.info(
                f"Get FG Status API returned error 500 or other error. Request Type: GET\nUrl: {url}\nAPI response: {response.text}\n")
            body = response.json()
            error_list = body['errors']
            error_msg = ""
            return True, "  \n".join(error_list), error_msg
