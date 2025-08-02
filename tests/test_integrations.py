from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.patch_object import PatchObject
from schemas.integrations import valid_schema
from test_data.data import Data

URL = f"{Data.base_url}/api/integrations"

class TestIntegrations:

    def test_post_integration(self, user, resource_verified, offer_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = URL
        payload = {
            "resourceId": f"{resource_verified}",
            "adOfferId": f"{offer_id}",
        }
        new_integration = CreateObject()
        new_integration.create_object(url, payload, headers)
        new_integration.check_response_is_201()
        new_integration.check_response_jsonschema(valid_schema)
        url_delete = f"{URL}/{new_integration.response_json["id"]}"
        delete_integration = DeleteObject()
        delete_integration.delete_object(url=url_delete, headers=headers)

    def test_delete_integration(self, user, integration_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/{integration_id}"
        delete_integration = DeleteObject()
        delete_integration.delete_object(url, headers=headers)
        delete_integration.check_response_is_204()
        get_integration = GetObject()
        get_integration.get_object(url, headers=headers)
        get_integration.check_is_not_active()

    def test_update_integration(self, user, integration_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_path = f"{URL}/{integration_id}"
        payload = Data.integration_patch
        update_integration = PatchObject()
        update_integration.patch_object(url_path, payload, headers)
        update_integration.check_response_is_200()
        payload["active"] = payload["isActive"]
        del payload["isActive"]
        update_integration.check_data_after_change(payload)

    def test_list_integrations(self, user, integrations):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = URL
        get_integration = GetObject()
        get_integration.get_object(url, headers=headers)
        get_integration.check_response_is_200()
        get_integration.check_list(*integrations)

    def test_get_integration_by_id(self, user, integration_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/{integration_id}"
        get_integration = GetObject()
        get_integration.get_object(url, headers=headers)
        get_integration.check_response_is_200()
        get_integration.check_id(integration_id)
    #
    def test_get_integration_by_resource(self, user, integration_id, resource_verified):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/resource/{resource_verified}"
        get_integration = GetObject()
        get_integration.get_object(url, headers=headers)
        get_integration.check_response_is_200()
        get_integration.check_list(integration_id)