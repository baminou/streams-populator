
from uperations.operation import Operation
import mysql.connector
import os
from uperation_base.operation_types.dot_env_operation import DotEnvOperation

class Createdatabase(DotEnvOperation):

    @staticmethod
    def name():
        return "Createdatabase"

    @staticmethod
    def description():
        return "Create the initial database"

    def _parser(self, main_parser):
        #main_parser.add_argument('first_argument', help="Argparse argument example")
        return

    def _run(self):
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USERNAME'),
            passwd=os.getenv('MYSQL_PASSWORD')
        )

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE %s" % (os.getenv('MYSQL_DB')))
        return