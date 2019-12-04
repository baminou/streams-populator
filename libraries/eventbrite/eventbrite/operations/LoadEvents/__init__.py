
from uperation_base.operation_types.dot_env_operation import DotEnvOperation
import requests
import json

class Loadevents(DotEnvOperation):

    @staticmethod
    def name():
        return "Loadevents"

    @staticmethod
    def description():
        return "Load events from eventbrite"

    def _parser(self, main_parser):
        main_parser.add_argument('--address', help="Address to look around", default='Toronto')
        return

    def _run(self):
        search_url = "https://www.eventbriteapi.com/v3/events/search?sort_by=%s&location.address=%s" % ('date', self.args.address)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '
        }
        print(requests.get(search_url,headers=headers).content)
        return