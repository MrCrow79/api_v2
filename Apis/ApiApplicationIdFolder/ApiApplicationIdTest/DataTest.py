import unittest

from Apis.ApiApplicationIdFolder.ApiApplicationIdFile import *
from Apis.ApiApplicationIdFolder.ApiApplicationIdCheckMethods import *


class ApplicationIdCheckData(unittest.TestCase):

    def setUp(self):
        self.current_api = ApiApplicationId()

    def tearDown(self):
        pass

    def test_application_id_app_is_3(self):
        self.current_api.full_url = 3
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_current_api = CheckApiApplicationId(self.current_api)

        assert self.current_api.no_response_errors, "{0}\n{1}\n{2}".format(self.current_api.response_code,
                                                                           self.current_api.full_url,
                                                                           self.current_api.response_error)

    def test_application_id_app_is_36(self):
        self.current_api.full_url = 36
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_api_application_id = CheckApiApplicationId(self.current_api)

        assert self.current_api.no_response_errors, "{0}\n{1}\n{2}".format(self.current_api.response_code,
                                                                           self.current_api.full_url,
                                                                           self.current_api.response_error)

    def test_application_id_app_is_asd(self):
        self.current_api.full_url = 'asd'
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        self.check_api_application_id = CheckApiApplicationId(self.current_api)

        assert self.current_api.no_response_errors, "{0}\n{1}\n{2}".format(self.current_api.response_code,
                                                                           self.current_api.full_url,
                                                                           self.current_api.response_error)
