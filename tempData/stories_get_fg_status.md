## story_get_fg_happy_path_single_record_2
* get_fg_status{"info_type": "fg status", "id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_fg_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_fg_happy_path_multi_record_2
* get_fg_status{"info_type": "fg status", "id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_fg_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_fg_with_order_id{"id": "LA_102"}
    - action_get_fg_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_fg_id_missing_single_record_2
* get_fg_status{"info_type": "fg status"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_fg_status_utter_result
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_get_fg_id_missing_multi_record_2
* get_fg_status{"info_type": "fg status"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- action_fetch_fg_status_utter_result
	- slot{"has_multi_db_records": "yes"}
* get_fg_with_order_id{"id": "LA_102"}
    - action_get_fg_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart


