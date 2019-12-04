
from uperations.operation import Operation
import mysql.connector
import os
from uperation_base.operation_types.dot_env_operation import DotEnvOperation

class Migrate(DotEnvOperation):

    @staticmethod
    def name():
        return "Migrate"

    @staticmethod
    def description():
        return "Create tables in the database"

    def _parser(self, main_parser):
        #main_parser.add_argument('first_argument', help="Argparse argument example")
        return

    def _run(self):
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USERNAME'),
            passwd=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )
        mycursor = mydb.cursor()

        query = """
            CREATE TABLE events (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                source VARCHAR(255) NOT NULL,
                source_id VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                link TEXT,
                lat DECIMAL(12,8),
                lng DECIMAL(12,8),
                address TEXT,
                description TEXT,
                picture TEXT,
                info JSON,
                start timestamp default current_timestamp,
                end timestamp default current_timestamp,
                alias VARCHAR(12),
                created_at timestamp default current_timestamp,
                updated_at timestamp default current_timestamp,
                UNIQUE(source, source_id)
            )
        """

        mycursor.execute(query)