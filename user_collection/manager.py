from decouple import config  # Import config from decouple
import requests
from requests.auth import HTTPBasicAuth
from user_collection.models import Collection, Movie

CLIENT_KEY = config('SECRET_KEY')
CLIENT_PASS = config('SECRET_PASS')




class UserManagement:
    @staticmethod
    def get_movies_list():
        url = 'https://demo.credy.in/api/v1/maya/movies/'
        headers = {
            'Username': 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',
            'Password': 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to connect: {response.status_code}")


class CollectionManagement:
    @staticmethod
    def add_new_collection(request, data):
        user_id = request.user.id
        collection = Collection.objects.create(title=data['title'], user_id=user_id, description=data['description'])
        for i in data['movies']:
            movie = Movie.objects.filter(uuid=i['uuid'])
            if not movie:
                movie = Movie.objects.create(
                    uuid=i['uuid'],
                    title=i['title'],
                    description=i['description'],
                    genres=i['genres']
                )




