from endpoints.get_object import GetObject
from test_data.data import Data

URL = f"{Data.base_url}/api/offers"

class TestOffers:

    def test_get_offers(self, user):
        headers = {'Authorization': f'Bearer {user["accessToken"]}'}
        get_offers = GetObject()
        get_offers.get_object(URL, headers)
        get_offers.check_response_is_200()
        print(get_offers.response_json)

    # def test_get_offer_by_id(self, user, offer_id):
    #     headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    #     url = f"{URL}/{offer_id}"
    #     get_offer = GetObject()
    #     get_offer.get_object(url, headers)
    #     get_offer.check_response_is_200()
    #     get_offer.check_id(offer_id)
    # #
    # def test_get_offers_recommended(self, user):
    #     headers = {'Authorization': f'Bearer {user["accessToken"]}'}
    #     url = f"{URL}/recommended"
    #     get_offers = GetObject()
    #     get_offers.get_object(url, headers)
    #     get_offers.check_response_is_200()
