
from uperations.library import Library
from .operations.LoadEvents import Loadevents
from .operations.PopulateEvents import PopulateEvents
from .operations.FeedStreams import FeedStreams

class Meetup(Library):

    @staticmethod
    def name():
        return "meetup"

    @staticmethod
    def description():
        return "Not description provided"

    def _init_operations(self):
        self._operations = {
            'loadevents': Loadevents(self),
            'populateevents': PopulateEvents(self),
            'feedstreams': FeedStreams(self)
        }
        return

    def operations(self):
        return self._operations