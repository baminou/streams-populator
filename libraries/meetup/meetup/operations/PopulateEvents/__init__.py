
from uperation_base.operation_types.dot_env_operation import DotEnvOperation
import json
import argparse
from models.Event import Event
import os
import mysql.connector

class PopulateEvents(DotEnvOperation):

    @staticmethod
    def name():
        return "Populateevents"

    @staticmethod
    def description():
        return "Populate events to a database"

    def _parser(self, main_parser):
        main_parser.add_argument('file', type=argparse.FileType('r'), help="Events json")
        return

    def _run(self):
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USERNAME'),
            passwd=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )

        mycursor = mydb.cursor()

        for line in self.args.file.readlines():
            event = Event.load_from_json(line)

            sql = "INSERT INTO events (source,source_id,name, link, lat, lng, address, description, picture, info, start, end) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = [event.get_source(), event.get_source_id(), event.get_name(), event.get_link(),event.get_lat(),event.get_lng(),
            event.get_address(),event.get_description(),event.get_picture(), json.dumps(event.get_info()),
            event.get_start_datetime(),event.get_end_datetime()]
            try:
                mycursor.execute(sql, val)
                mydb.commit()
            except mysql.connector.errors.IntegrityError:
                print(event.get_name()+" already populated")
            except mysql.connector.errors.DatabaseError:
                print("Database error")
        return