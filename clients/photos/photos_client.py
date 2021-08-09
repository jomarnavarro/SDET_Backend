from json import dumps
from clients.base_client import BaseClient
from config import BASE_URL, API_KEY
from utils.request import APIRequest
from utils.file_reader import read_file

class PhotosClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.url = BASE_URL
        self.request = APIRequest()

    
    def get_mars_photos(self, num_photos=None, date_type='sol', date_value=1000):
        params = {
            "API_KEY": API_KEY,
            date_type: date_value
        }
        if num_photos is not None:
            params["page"] = 1

        response = self.request.get(self.url, headers=None, url_params=params)
        print(response.status_code)
        if num_photos is not None:
            return response.as_dict['photos'][:num_photos]
        return response.as_dict['photos']