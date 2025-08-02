from jsonschema import validate


class BaseEndpoint:
    response = None
    response_json = None
    url = ""

    # @staticmethod
    # def custom_request(method, url, **kwargs):
    #     return requests.request(method, url, **kwargs)

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_201(self):
        assert self.response.status_code == 201

    def check_response_is_204(self):
        assert self.response.status_code == 204

    def check_response_jsonschema(self, schema):
        validate(instance=self.response_json, schema=schema)

    def check_email(self, email):
        assert self.response_json["email"] == email

    def check_data_after_change(self, data):
        for i in data:
            assert i in self.response_json
