import unittest

from Apis.ApiAdLandingsFolder.ApiAdLandingsFile import *


class AdLandingCheckModel(unittest.TestCase):
    def setUp(self):
        # see comments in ApiAdLandingTests/DataTest
        self.current_api = ApiAdLandings()
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)
        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params)

    def tearDown(self):
        del self.current_api

    def test_api_ad_landing_check_data(self):
        self.current_api.check_model()

        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params,
               no_response_errors=self.current_api.no_response_errors)