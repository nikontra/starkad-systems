import faker

from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from test_data.data import Data

URL = f"{Data.base_url}/api/users/profile"


class TestUsers:
    def test_users_get_profile(self, user):
        access_token = user["accessToken"]
        headers = {'Authorization': f'Bearer {access_token}'}
        profile = GetObject()
        profile.get_object(URL, headers=headers)
        profile.check_response_is_200()


    def test_users_edit_profile(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        profile = PutObject()
        profile.put_object(url=URL, payload=Data.user_put, headers=headers)
        profile.check_response_is_200()
        profile.check_data_after_change(Data.user_put)
