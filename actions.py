# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class SearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = 'No cuisine mentioned'
        for e in entities: 
            if e['entity'] == 'cuisine':
                cuisine = e['value']
                if cuisine == 'indian':
                    message = 'https://www.greavesindia.co.uk/12-best-indian-restaurants-india/'
                elif cuisine=='chinese':
                    message = 'https://www.tripadvisor.in/Restaurants-g186338-c11-London_England.html'
                else:
                    message = "We do not have any restaurants for this cuisine"
        dispatcher.utter_message(text=message)

        return []
