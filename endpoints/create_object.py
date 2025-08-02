import logging

import requests

from endpoints.base_endpoint import BaseEndpoint

logger = logging.getLogger(__name__)


class CreateObject(BaseEndpoint):

    def create_object(self, url, payload, headers=None):
        self.response = requests.post(url=url, json=payload, headers=headers)
        self.response_json = self.response.json()
        logger.info(self.response.text)


