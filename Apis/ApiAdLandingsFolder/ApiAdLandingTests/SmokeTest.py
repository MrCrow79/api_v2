import unittest

from Apis.ApiAdLandingsFolder.ApiAdLandingsFile import *


class AdLandingSmoke(unittest.TestCase):
    def setUp(self):
        self.current_api = ApiAdLandings()
        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params)

    def tearDown(self):
        del self.current_api

    def test_api_ad_landing(self):
        self.current_api = ApiAdLandings()
        self.current_api.send_request(self.current_api)
        self.current_api.check_server_answer(self.current_api)

        logger(type=self.current_api.type, full_url=self.current_api.full_url,
               no_response_errors=self.current_api.no_response_errors)

        self.assertTrue(self.current_api.no_response_errors, 'tst msg')
