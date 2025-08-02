import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_object(self, url, headers):
        self.response = requests.delete(url=url, headers=headers)
        # self.response_json = self.response.json()
