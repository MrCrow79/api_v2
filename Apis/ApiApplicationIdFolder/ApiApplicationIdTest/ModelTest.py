import unittest

from Apis.ApiApplicationIdFolder.ApiApplicationIdFile import *
from Apis.ApiApplicationIdFolder.ApiApplicationIdCheckMethods import *


class ApplicationIdModel(unittest.TestCase):
    def test_model(self):

        self.current_api = ApiApplicationId()
        self.current_api.full_url = 3
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)
        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params)

        self.check_current_api = CheckApiApplicationId(self.current_api)
        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params,
               no_response_errors=self.current_api.no_response_errors,
               check_data_no_errors=self.check_current_api.check_data_no_errors)
        self.check_current_api.check_model()


