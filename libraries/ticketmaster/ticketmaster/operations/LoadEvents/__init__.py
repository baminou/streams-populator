
from uperations.operation import Operation
from ...api import get_events

class LoadEvents(Operation):

    @staticmethod
    def name():
        return "Loadevents"

    @staticmethod
    def description():
        return "Loadevents has not been documented yet."

    def _parser(self, main_parser):
        #main_parser.add_argument('first_argument', help="Argparse argument example")
        return

    def _run(self):
        API_KEY=""
        print(get_events(API_KEY))
        return