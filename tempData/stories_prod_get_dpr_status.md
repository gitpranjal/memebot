## story_get_dpr_happy_path_single_record_1
* get_dpr_status{"info_type": "dpr", "id": "UWTS1071", "activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_happy_path_multi_record_1
* get_dpr_status{"info_type": "dpr", "id": "UWTS1071", "activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_dpr_with_order_id{"id": "LA_102"}
    - action_get_dpr_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_happy_path_single_record_2
* get_dpr_status{"info_type": "dpr", "id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_happy_path_multi_record_2
* get_dpr_status{"info_type": "dpr", "id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_dpr_with_order_id{"id": "LA_102"}
    - action_get_dpr_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_id_missing_single_record_1
* get_dpr_status{"info_type": "dpr", "activity_name": "cutting"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_id_missing_multi_record_1
* get_dpr_status{"info_type": "dpr", "activity_name": "cutting"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_dpr_with_order_id{"id": "LA_102"}
    - action_get_dpr_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_id_missing_single_record_2
* get_dpr_status{"info_type": "dpr"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_dpr_id_missing_multi_record_2
* get_dpr_status{"info_type": "dpr"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_dpr_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_dpr_with_order_id{"id": "LA_102"}
    - action_get_dpr_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart


