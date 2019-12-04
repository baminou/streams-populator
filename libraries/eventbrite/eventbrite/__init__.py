
from uperations.library import Library
from .operations.LoadEvents import Loadevents

class Eventbrite(Library):

    @staticmethod
    def name():
        return "eventbrite"

    @staticmethod
    def description():
        return "Not description provided"

    def _init_operations(self):
        self._operations = {
            # operation_command: OperationClass(self)
            'loadevents': Loadevents(self)
        }
        return

    def operations(self):
        return self._operations