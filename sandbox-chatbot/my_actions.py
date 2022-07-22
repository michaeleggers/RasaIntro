import json
from msilib import knownbits
from pathlib import Path
from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckStudentsExistence(Action):
    
    knowledge = Path("data/students.txt").read_text().split("\n")
    
    def name(self) -> Text:
        return "action_check_students_existence"
    
    async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob["entity"] == "student_name":
                name = blob["value"]
                if name in self.knowledge:
                    dispatcher.utter_message(text="found")
                else:
                    dispatcher.utter_message(text="not found")
        return []
    


