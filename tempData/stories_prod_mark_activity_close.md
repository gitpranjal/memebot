## story_mark_activity_close_happy_path_single_record_1
* mark_activity_close{"id": "UWTS1071", "activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
    - action_mark_activity_close
    - slot{"has_multi_db_records": "no"}
    - action_restart

## story_mark_activity_close_happy_path_multi_record_1
* mark_activity_close{"id": "UWTS1071", "activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
    - action_mark_activity_close
    - slot{"has_multi_db_records": "yes"}
* close_activity_with_order_id{"id": "LA_102", "tna_activity_id": "2056271"}
    - action_close_activity_with_order_id
    - slot{"has_multi_db_records": "no"}
    - action_restart

## story_mark_activity_close_fg_code_missing_single_record
* mark_activity_close{"activity_name": "cutting"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_mark_activity_close
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_mark_activity_close_fg_code_missing_multi_record
* mark_activity_close{"activity_name": "cutting"}
	- utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_mark_activity_close
	- slot{"has_multi_db_records": "yes"}
* close_activity_with_order_id{"id": "LA_102", "tna_activity_id": "2056271"}
    - action_close_activity_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_mark_activity_close_activity_missing_single_record
* mark_activity_close{"id": "UWTS1071"}
	- utter_ask_activity
* inform{"activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_mark_activity_close
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_mark_activity_close_activity_missing_multi_record
* mark_activity_close{"id": "UWTS1071"}
	- utter_ask_activity
* inform{"activity_name": "cutting"}
    - slot{"activity_name": "cutting"}
    - slot{"id": "UWTS1071"}
	- action_mark_activity_close
	- slot{"has_multi_db_records": "yes"}
* close_activity_with_order_id{"id": "LA_102", "tna_activity_id": "2056271"}
    - action_close_activity_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

## story_mark_activity_close_fg_code_and_activity_missing_single_record
* mark_activity_close
    - utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- utter_ask_activity
* inform{"activity_name": "cutting"}
    - slot{"activity_name": "cutting"}    
	- action_mark_activity_close
	- slot{"has_multi_db_records": "no"}
	- action_restart

## story_mark_activity_close_fg_code_and_activity_missing_multi_record
* mark_activity_close
    - utter_ask_fg_code
* inform{"id": "UWTS1071"}
    - slot{"id": "UWTS1071"}
	- utter_ask_activity
* inform{"activity_name": "cutting"}
    - slot{"activity_name": "cutting"}    
	- action_mark_activity_close
	- slot{"has_multi_db_records": "yes"}
* close_activity_with_order_id{"id": "LA_102", "tna_activity_id": "2056271"}
    - action_close_activity_with_order_id
    - slot{"has_multi_db_records": "no"}
	- action_restart

