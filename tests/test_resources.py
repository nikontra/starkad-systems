from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from schemas.integrations import valid_schema
from test_data.data import Data

URL = f"{Data.base_url}/api/resources"

class TestResources:

    def test_create_resource(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        new_resource = CreateObject()
        new_resource.create_object(url=URL, payload=Data.resource_data, headers=headers)
        new_resource.check_response_is_201()
        new_resource.check_response_jsonschema(valid_schema)
        url_delete = f"{URL}/{new_resource.response_json["id"]}"
        delete_resource = DeleteObject()
        delete_resource.delete_object(url=url_delete, headers=headers)

    def test_delete_resource(self, user, resource):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f'{URL}/{resource["id"]}'
        delete_resource = DeleteObject()
        delete_resource.delete_object(url=url, headers=headers)
        delete_resource.check_response_is_204()
        get_resource = GetObject()
        get_resource.get_object(url=url, headers=headers)
        get_resource.check_response_is_404()

    def test_update_resource(self, user, resource):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_put = f'{URL}/{resource["id"]}'
        update_resource = PutObject()
        update_resource.put_object(url=url_put, payload=Data.resource_put, headers=headers)
        update_resource.check_response_is_200()
        update_resource.check_data_after_change(Data.resource_put)

    def test_list_resources(self, user, resources):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        get_resources = GetObject()
        get_resources.get_object(url=URL, headers=headers)
        get_resources.check_response_is_200()
        get_resources.check_list(*resources)

    def test_get_resource(self, user, resource):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_get = f'{URL}/{resource["id"]}'
        get_resource = GetObject()
        get_resource.get_object(url=url_get, headers=headers)
        get_resource.check_response_is_200()
        get_resource.check_id(resource["id"])
    #
    def test_get_resource_verify(self, user, resource):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_get = f'{URL}/{resource["id"]}/verify'
        params = {'token': resource['verificationToken']}
        get_verify = GetObject()
        get_verify.get_object(url=url_get, headers=headers, params=params)
        get_verify.check_response_is_200()
        get_verify.check_is_verify_resource()
