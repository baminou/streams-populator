
from uperation_base.operation_types.dot_env_operation import DotEnvOperation
import requests
import json
import os
from models.Event import Event
from datetime import datetime

class Loadevents(DotEnvOperation):

    @staticmethod
    def name():
        return "Loadevents"

    @staticmethod
    def description():
        return "Loadevents has not been documented yet."

    def _parser(self, main_parser):
        main_parser.add_argument('output', help="Output jsonl file")
        return

    def _run(self):
        token = os.getenv('MEETUP_TOKEN')
        lat = 43.6532
        lon = -79.3832
        search_url = "https://api.meetup.com/find/upcoming_events?key=%s&lat=%s&lon=%s&fields=featured_photo" % (token, str(lat), str(lon))
        events = []
        for event_data in json.loads(requests.get(search_url).content)['events']:
            new_event = Event(
                source='meetup.com',
                source_id=self.event_data_id(event_data),
                link=self.event_data_link(event_data),
                name=self.event_data_name(event_data),
                lat=self.event_data_lat(event_data),
                lng=self.event_data_lng(event_data),
                address=self.event_data_address(event_data),
                #description=self.event_data_description(event_data),
                start_datetime=str(self.event_data_start_datetime(event_data)),
                end_datetime=str(self.event_data_end_datetime(event_data)),
                picture=self.event_data_picture(event_data),
                info=self.event_data_info(event_data)
            )
            events.append(new_event)
            print(new_event.__dict__)
        with open(self.args.output,'w') as fp:
            for i in range(0,len(events)):
                json.dump(events[i].__dict__,fp)
                fp.write('\n')
        return
    
    def event_data_info(self, event_data):
        return event_data
    
    def event_data_name(self, event_data):
        return event_data['name']
    
    def event_data_link(self, event_data):
        return event_data['link']
    
    def event_data_description(self, event_data):
        try:
            return event_data['description']
        except KeyError:
            return None
    
    def event_data_start_datetime(self, event_data):
        return datetime.strptime(event_data['local_date']+" "+event_data['local_time'],"%Y-%m-%d %H:%M")
    
    def event_data_end_datetime(self, event_data):
        start = self.event_data_start_datetime(event_data).timestamp()
        return datetime.fromtimestamp(start + event_data['duration']/1000)
    
    def event_data_id(self, event_data):
        return event_data['id']
    
    def event_data_lat(self, event_data):
        try:
            return event_data['venue']['lat']
        except KeyError:
            return None
    
    def event_data_lng(self, event_data):
        try:
            return event_data['venue']['lon']
        except KeyError:
            return None

    def event_data_address(self, event_data):
        try:
            return event_data['venue']['address_1']
        except KeyError:
            return None
    
    def event_data_picture(self, event_data):
        try:
            return event_data['featured_photo']['highres_link']
        except KeyError:
            return None
