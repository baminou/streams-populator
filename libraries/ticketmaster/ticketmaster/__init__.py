
from uperations.library import Library
from .operations.LoadEvents import LoadEvents

class Ticketmaster(Library):

    @staticmethod
    def name():
        return "ticketmaster"

    @staticmethod
    def description():
        return "Not description provided"

    def _init_operations(self):
        self._operations = {
            'loadevents': LoadEvents(self)
        }
        return

    def operations(self):
        return self._operations