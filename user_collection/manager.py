from decouple import config  # Import config from decouple
import requests
from requests.auth import HTTPBasicAuth
# Load the SECRET_KEY from .env
CLIENT_KEY = config('SECRET_KEY')
CLIENT_PASS = config('SECRET_PASS')


class UserCollectionManager:

    @staticmethod
    def getAllMovies():
        # Define the API endpoint and your credentials
        print('hii')
        api_url = "https://demo.credy.in/api/v1/maya/movies/"
        username = CLIENT_KEY
        password = CLIENT_PASS

        # Option 1: If the API requires Basic Auth
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password), verify=False)
        if response.status_code == 200:
            data = response.json()
            return(data)
        else:
            print(f"Failed with status code {response.status_code}")
            print(response.text)


