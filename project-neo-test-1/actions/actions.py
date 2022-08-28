# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, EventType

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "custom_find_course_path"

    def run(self, dispatcher, tracker, domain):
        study_whats_good_list = tracker.get_slot("study_whats_good")
        # TODO: trigger correct form by study_whats_good_list input
        return [FollowupAction(name="form_study_organization")]
