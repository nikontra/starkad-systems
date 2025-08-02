import requests

from endpoints.base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):

    def put_object(self, url, payload,  headers=None):
        self.response = requests.put(url=url, json=payload, headers=headers)
        self.response_json = self.response.json()

