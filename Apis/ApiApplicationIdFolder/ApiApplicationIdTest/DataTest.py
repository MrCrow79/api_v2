import unittest

from Apis.ApiApplicationIdFolder.ApiApplicationIdFile import *
from Apis.ApiApplicationIdFolder.ApiApplicationIdCheckMethods import *


class ApplicationIdCheckData(unittest.TestCase):

    def setUp(self):
        self.current_api = ApiApplicationId()
        logger(type=self.current_api.type, full_url=self.current_api.full_url)

    def tearDown(self):
        pass

    def test_application_id_app_is_3(self):
        self.current_api.full_url = 3
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_current_api = CheckApiApplicationId(self.current_api)

        logger(type=self.current_api.type, full_url=self.current_api.full_url,
               no_response_errors=self.current_api.no_response_errors)

        assert self.current_api.no_response_errors is True

    def test_application_id_app_is_36(self):
        self.current_api.full_url = 36
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_api_application_id = CheckApiApplicationId(self.current_api)

        logger(type=self.current_api.type, full_url=self.current_api.full_url,
               no_response_errors=self.current_api.no_response_errors)

        assert self.current_api.no_response_errors is True

    def test_application_id_app_is_asd(self):
        self.current_api.full_url = 'asd'
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_api_application_id = CheckApiApplicationId(self.current_api)

        logger(type=self.current_api.type, full_url=self.current_api.full_url,
               no_response_errors=self.current_api.no_response_errors)

        assert self.current_api.no_response_errors
