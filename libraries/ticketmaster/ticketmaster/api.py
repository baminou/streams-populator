

import requests

API_URL="https://app.ticketmaster.com/"

def get_events(api_key, size=1, city='toronto'):
    response = requests.get(API_URL+"/discovery/v2/events.json?city=toronto&size="+str(size)+"&apikey="+api_key)
    return response.json()