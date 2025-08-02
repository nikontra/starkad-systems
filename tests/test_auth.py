import faker
import psycopg2
import requests
import logging

from services.user import delete_user
from test_data.data import Data
from endpoints.create_object import CreateObject
from test_data.data import Data


URL = f"{Data.base_url}/api/auth"

logger = logging.getLogger(__name__)

fake = faker.Faker()


class TestAuth:
    def test_register_user(self):
        url = URL + "/register"
        user = CreateObject()
        user.create_object(url, Data.user_login)
        user.check_response_is_201()
        user.check_email(Data.user_login["email"])
        delete_user(Data.user_login["email"])


    def test_login_user(self, user):
        url = URL + "/login"
        login = CreateObject()
        login.create_object(url, Data.user_login)
        login.check_response_is_200()
        login.check_email(Data.user_login["email"])


    def test_refresh_token(self, user):
        url = URL + "/refresh-token"
        payload = {"refreshToken": user["refreshToken"]}
        refresh_token = CreateObject()
        refresh_token.create_object(url, payload)
        refresh_token.check_response_is_200()
        refresh_token.check_email(Data.user_login["email"])
