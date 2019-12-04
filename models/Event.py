
import json

class Event(object):
    def __init__(self, source, source_id, link, name=None, lat=None, lng=None, address=None, description=None, start_datetime=None, 
        end_datetime=None, picture=None, info=None):
        self.source = source
        self.source_id = source_id
        self.link = link
        self.name = name
        self.lat = lat
        self.lng = lng
        self.address = address
        self.description = description
        self.picture = picture
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.info = info
        return
    
    def get_name(self):
        return self.name
    
    def get_source(self):
        return self.source
    
    def get_source_id(self):
        return self.source_id

    def get_lat(self):
        return self.lat
    
    def get_address(self):
        return self.address
    
    def get_source(self):
        return self.source
    
    def get_link(self):
        return self.link
    
    def get_lng(self):
        return self.lng
    
    def get_lat(self):
        return self.lat

    def get_info(self):
        return self.info

    def get_description(self):
        return self.description

    def get_picture(self):
        return self.picture
    
    def get_start_datetime(self):
        return self.start_datetime
    
    def get_end_datetime(self):
        return self.end_datetime

    def set_name(self, name):
        self.name = name
        return
    
    def load_from_json(json_object):
        j = json.loads(json_object)
        e = Event(**j)
        return e
    
    def load_from_array(array_object):
        return Event.load_from_json(json.dumps(array_object))
