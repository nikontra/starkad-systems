import pytest

from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from test_data.data import Data

URL = f"{Data.base_url}/api/payments"

class TestPayments:

    def test_list_payments(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        get_payments = GetObject()
        get_payments.get_object(url=URL, headers=headers)
        get_payments.check_response_is_200()

    @pytest.mark.xfail
    def test_get_payment_by_id(self, user, payment_id):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/{payment_id}"
        get_payment = GetObject()
        get_payment.get_object(url, headers=headers)
        get_payment.check_response_is_200()

    @pytest.mark.xfail
    def test_withdrawal(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/withdrawal"
        create_withdrawal = CreateObject()
        create_withdrawal.create_object(url, Data.payment_withdrawal, headers)
        create_withdrawal.check_response_is_200()

    def test_balance(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/balance"
        get_balance = GetObject()
        get_balance.get_object(url, headers=headers)
        get_balance.check_response_is_200()

    def test_get_available_payment_methods(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        url = f"{URL}/methods"
        get_available_payment_methods = GetObject()
        get_available_payment_methods.get_object(url, headers)
        get_available_payment_methods.check_response_is_200()
