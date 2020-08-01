import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class action_check_existence(Action):
    confidentieldoc = open("confidentiel.txt").read()
    sensibledoc = open("sensible.txt").read()
    internedoc = open("interne.txt").read()
    diffusabledoc = open("diffusable.txt").read()
    

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'classification':
                name = blob['value']
                if name in self.confidentieldoc:
                    dispatcher.utter_message(name)
                elif name in self.sensibledoc:
                    dispatcher.utter_message(name)
                elif name in self.internedoc:
                    dispatcher.utter_message(name)
                elif name in self.diffusabledoc:
                    dispatcher.utter_message(name)
                else:
                    gt = {"buttons": [
                                        {
                                            "type": "postback",
                                            "payload": "/diffusable",
                                            "title": "ces informations peuvent être publiées en ligne sans risque pour l'entreprise"
                                        },
                                        {
                                            "type": "postback",
                                            "payload": "/interne",
                                            "title": "ce fichier peut etre partagees a l'interne de l'entreprise sans risque"
                                        },
                                        {
                                            "type": "postback",
                                            "payload": "/sensible",
                                            "title": "ce fichier est adressé a un departement ou un groupe restreint de personnes bien identifier"
                                        },
                                        {
                                            "type": "postback",
                                            "payload": "/confidentiel",
                                            "title": "ce fichier est adressé à un groupe restreint de personnes bien identifier seulement"
                                        },
                                    ]
                        }
                    dispatcher.utter_custom_json(gt)
        return []
