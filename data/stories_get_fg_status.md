## greet_user
* greet
    - utter_greet
    - utter_meme_options
* inform{"genre":"politics"}
    - action_utter_meme
    - utter_ask_for_more_memes
* deny
	- utter_glad_i_helped
	- action_restart
	
# greet_user_2
* greet
    - utter_greet
    - utter_meme_options
* inform{"genre":"politics"}
    - action_utter_meme
    - utter_ask_for_more_memes
* affirm
	- utter_meme_options
* inform{"genre":"politics"}
	- action_utter_meme
	- utter_ask_for_more_memes
* affirm
	- utter_meme_options
* inform{"genre":"politics"}
	- action_utter_meme
	- utter_ask_for_more_memes
* affirm
	- utter_meme_options
* inform{"genre":"politics"}
	- action_utter_meme
	- utter_ask_for_more_memes
* affirm
	- utter_meme_options
* inform{"genre":"politics"}
	- action_utter_meme
	- utter_ask_for_more_memes
* deny
	- utter_glad_i_helped
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




