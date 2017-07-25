import unittest

from Apis.ApiApplicationIdFolder.ApiApplicationIdFile import *


class ApplicationIdSmoke(unittest.TestCase):

    def test_api_api_application_id_app_is_3(self):
        self.current_api = ApiApplicationId()
        self.current_api.full_url = 3

        logger(type=self.current_api.type, full_url=self.current_api.full_url)

        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        logger(type=self.current_api.type, full_url=self.current_api.full_url,
               no_response_errors=self.current_api.no_response_errors)

        assert self.current_api.no_response_errors

