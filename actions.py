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
    CasSpecial = ["procédure d'organisation","procédure","procedure"]
    buttons = [{'title': 'Contenu', 'payload': '/based_content'}, {'title': 'La cible', 'payload': '/based_cible'}, {'title': 'Impact', 'payload': '/based_impact'}]

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'classification':
                name = blob['value']
                if name in self.CasSpecial:
                    dispatcher.utter_message(text="Ce sont des documents qui peuvent être internes ou sensibles. Pouvez-vous donner plus de détails sur votre document")
                elif name in self.confidentieldoc:
                    dispatcher.utter_message(text="Votre document doit être classifié confidentiel")
                elif name in self.sensibledoc:
                    dispatcher.utter_message(text="Votre document doit être classifié sensible")
                elif name in self.internedoc:
                    dispatcher.utter_message(text="Votre document doit être classifié interne")
                elif name in self.diffusabledoc:
                    dispatcher.utter_message(text="Votre document doit être classifié diffusable")
                else:
                    dispatcher.utter_button_message("Je ne peux malheureusement pas vous aider. Merci de vous référer au groupe Teams de classification de la donnée <link_here>\n OU \n vous voulez classer votre document en fonction de :", self.buttons)
        return []
