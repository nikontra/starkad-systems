from endpoints.get_object import GetObject
from test_data.data import Data

URL = f"{Data.base_url}/api/statistics"

class TestStatistics():

    def test_get_statistics(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        get_statistics = GetObject()
        get_statistics.get_object(url=URL, headers=headers, params=Data.statistics_date)
        get_statistics.check_response_is_200()

    def test_get_statistics_by_integration(self, user, integration_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_get = f"{URL}/integration/{integration_id}"
        get_statistics = GetObject()
        get_statistics.get_object(url_get, headers=headers, params=Data.statistics_date)
        get_statistics.check_response_is_200()

    def test_get_statistics_by_resource(self, user, resource):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url_get = f"{URL}/resource/{resource["id"]}"
        get_statistics = GetObject()
        get_statistics.get_object(url_get, headers=headers, params=Data.statistics_date)
        get_statistics.check_response_is_200()

