import requests

from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    def get_object(self, url, headers, params=None):
        self.response = requests.get(url=url, headers=headers, params=params)
        self.response_json = self.response.json()

    def check_response_is_404(self):
        assert self.response.status_code == 404

    def check_id(self, object_id):
        assert self.response_json['id'] == object_id

    def check_is_verify_resource(self):
        assert self.response_json['verified'] == True

    def check_is_not_active(self):
        assert self.response_json['active'] == False

    def check_list(self, *args):
        for i in range(len(args)):
            assert args[i] == self.response_json[i]["id"]
