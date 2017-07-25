import unittest

from Apis.ApiAdLandingsFolder.ApiAdLandingsFile import *
from Apis.ApiAdLandingsFolder.ApiAdLandingsCheckMethods import *


class AdLandingCheckData(unittest.TestCase):
    """tests will started automatically"""
    def setUp(self):
        # crate instance
        self.current_api = ApiAdLandings()
        # send request
        self.current_api.send_request(self.current_api)
        # check answer(fill some fields in instance)
        self.current_api.check_server_answer(self.current_api)
        # create instance for checking data
        self.check_current_api = CheckApiAdLandings(self.current_api)
        # save some data in log
        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params)

    def tearDown(self):
        del self.current_api
        del self.check_current_api

    def test_api_ad_landing_check_net(self):
        """function for check app in answer"""

        self.check_current_api.check_net()

        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params,
               no_response_errors=self.current_api.no_response_errors,
               check_net_no_error=self.check_current_api.check_net_no_error)

        self.assertTrue(self.check_current_api.check_net_no_error,
                        'check_net_no_error = {0}'.format(self.check_current_api.check_net_no_error))

    def test_api_ad_landing_check_app(self):
        """function for check app in answer"""
        self.check_current_api.check_app()

        logger(type=self.current_api.type, full_url=self.current_api.full_url, params=self.current_api.params,
               no_response_errors=self.current_api.no_response_errors,
               check_app_no_error=self.check_current_api.check_app_no_error)

        self.assertTrue(self.check_current_api.check_app_no_error,
                        'check_app_no_error = {0}'.format(self.check_current_api.check_app_no_error))
