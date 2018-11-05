# example from: https://marcobonzanini.com/2015/09/29/easy-text-analytics-with-the-dandelion-api-and-python/

import requests
import json
 
DANDELION_APP_ID = '6d5414fa19464204abdc1aa510ccc471'
DANDELION_APP_KEY = '6d5414fa19464204abdc1aa510ccc471'
 
ENTITY_URL = 'https://api.dandelion.eu/datatxt/nex/v1'
 
def get_entities(text, confidence=0.1, lang='en'):
    payload = {
        '$app_id': DANDELION_APP_ID,
        '$app_key': DANDELION_APP_KEY,
        'text': text,
        'confidence': confidence,
        'lang': lang,
        'social.hashtag': True,
        'social.mention': True
    }
    response = requests.get(ENTITY_URL, params=payload)
    return response.json()
 
def print_entities(data):
    for annotation in data['annotations']:
        print("Entity found: %s" % annotation['spot'])
 
if __name__ == '__main__':
    query = "Add boiling water into the cup. Take the cup and drop the water into the saucepan. Mix the butter, flour and sugar in the pan. Then, add bananas and strawberries. Cook for five minutes. "
    response = get_entities(query)
    print(json.dumps(response, indent=4))
