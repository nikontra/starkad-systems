import pytest
import faker
import logging

from endpoints.get_object import GetObject
from services.user import delete_user

logger = logging.getLogger(__name__)

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from test_data.data import Data

fake = faker.Faker()

@pytest.fixture
def user():
    url = f"{Data.base_url}/api/auth/register"
    new_user = CreateObject()
    payload=Data.user_login
    payload['email'] = fake.email()
    new_user.create_object(url, payload=Data.user_login)
    yield new_user.response_json
    email = new_user.response_json['email']
    delete_user(email)

@pytest.fixture
def resource(user):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url_create = f"{Data.base_url}/api/resources"
    new_resource = CreateObject()
    new_resource.create_object(url=url_create, payload=Data.resource_data, headers=headers)
    yield new_resource.response_json
    url_delete = f"{url_create}/{new_resource.response_json["id"]}"
    delete_resource = DeleteObject()
    delete_resource.delete_object(url=url_delete, headers=headers)


@pytest.fixture
def resource_verified(user, resource):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url_get = f'{Data.base_url}/api/resources/{resource["id"]}/verify'
    params = {'token': resource['verificationToken']}
    get_verify = GetObject()
    get_verify.get_object(url=url_get, headers=headers, params=params)
    return get_verify.response_json['id']


@pytest.fixture
def resources(user):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url_create= f"{Data.base_url}/api/resources"
    resources_list = []
    for i in range(2):
        payload = Data.resource_data
        payload["url"] = fake.url()
        resource = CreateObject()
        resource.create_object(url=url_create, payload=payload, headers=headers)
        url_verify = f'{Data.base_url}/api/resources/{resource.response_json["id"]}/verify'
        params = {'token': resource.response_json['verificationToken']}
        get_verify = GetObject()
        get_verify.get_object(url=url_verify, headers=headers, params=params)
        resources_list.append(resource.response_json["id"])
    yield resources_list
    for i in resources_list:
        url_delete = f"{url_create}/{i}"
        delete_resource = DeleteObject()
        delete_resource.delete_object(url=url_delete, headers=headers)


@pytest.fixture
def offer_id(user):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url = f"{Data.base_url}/api/offers"
    get_offers = GetObject()
    get_offers.get_object(url, headers)
    return get_offers.response_json["content"][0]["id"]


@pytest.fixture
def integration_id(user, resource_verified, offer_id):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url = f"{Data.base_url}/api/integrations"
    payload = {
        "resourceId": f"{resource_verified}",
        "adOfferId": f"{offer_id}",
    }
    new_integration = CreateObject()
    new_integration.create_object(url, payload, headers)
    yield new_integration.response_json["id"]
    url_delete = f"{url}/{new_integration.response_json["id"]}"
    delete_integration = DeleteObject()
    delete_integration.delete_object(url=url_delete, headers=headers)

@pytest.fixture
def integrations(user, resources, offer_id):
    headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    url = f"{Data.base_url}/api/integrations"
    integrations_list = []
    for i in resources:
        payload = {
            "resourceId": f"{i}",
            "adOfferId": f"{offer_id}",
        }
        new_integration = CreateObject()
        new_integration.create_object(url, payload, headers)
        integrations_list.append(new_integration.response_json["id"])
    yield integrations_list
    for i in integrations_list:
        url_delete = f"{url}/{i}"
        delete_integration = DeleteObject()
        delete_integration.delete_object(url=url_delete, headers=headers)

@pytest.fixture
def payment_id(user):
    pass



