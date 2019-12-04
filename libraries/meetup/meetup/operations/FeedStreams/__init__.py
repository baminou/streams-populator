
from uperation_base.operation_types.dot_env_operation import DotEnvOperation
import os
import mysql.connector
from models.Event import Event
import requests
import cloudinary.uploader

class FeedStreams(DotEnvOperation):

    @staticmethod
    def name():
        return "Feedstreams"

    @staticmethod
    def description():
        return "Feed streams in Wegopix"

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
        mycursor.execute("""
            SELECT * FROM events 
            WHERE `alias` IS NULL
        """)
        field_names = [i[0] for i in mycursor.description]
        headers = {'Authorization':'Bearer '+os.getenv('WEGOPIX_TOKEN'), 'Accept':'application/json'}

        for result in mycursor.fetchall():
            data = dict(zip(field_names,result))
            if 'picture' in data: continue
            if data['address']==None or data['lat']==None or data['lng']==None:
                continue

            picture_url = cloudinary.uploader.upload(data['picture'],
                cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
                api_key=os.getenv('CLOUDINARY_API_KEY'),
                api_secret=os.getenv('CLOUDINARY_API_SECRET')
                )['secure_url']

            f = open('tmp.jpg','wb')
            f.write(requests.get(picture_url).content)
            f.close()

            files = {'picture': open('tmp.jpg', 'rb')}

            stream_data = {
                'name': data['name'],
                'lat': data['lat'],
                'lng': data['lng'],
                'address': data['address'],
                'visibility': os.getenv('MEETUP_VISIBILITY'),
                'start_date': data['start'].strftime('%m-%Y-%d'),
                'end_date': data['end'].strftime('%m-%Y-%d'),
                'start_time': data['start'].strftime('%I:%M %p'),
                'end_time': data['end'].strftime('%I:%M %p')
            }
            print(stream_data)
            response = requests.post(os.getenv('WEGOPIX_URL')+"/api/v1/streams",
                files=files,
                data=stream_data,
                headers=headers)
            
            if response.status_code == 200:
                mycursor.execute("""
                    UPDATE events
                    SET alias=%s
                    WHERE id=%s
                """,[response.json()['alias'], data['id']])
                mydb.commit()
            print(response.json())
        
        return