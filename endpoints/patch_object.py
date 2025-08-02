import requests

from endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    def patch_object(self, url, payload, headers):
        self.response = requests.patch(url=url, json=payload, headers=headers)
        self.response_json = self.response.json()
