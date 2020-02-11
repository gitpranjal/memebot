## greet user
* greet
    - utter_greet
    - action_utter_image
    - action_restart

## just affirm
* affirm
	- utter_glad_i_helped
	- action_restart

## just deny 1
* deny
	- utter_sorry_want_escalate
* affirm
	- action_raise_ticket_silently
	- action_restart

## just deny 2
* deny
	- utter_sorry_want_escalate
* deny
	- utter_what_else
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

