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

    def tearDown(self):
        del self.current_api
        del self.check_current_api

    def test_api_ad_landing_check_net(self):
        """function for check app in answer"""

        self.check_current_api.check_net()

        assert self.check_current_api.check_net_no_error, "{0}\n{1}\n{2}".format(self.current_api.response_code,
                                                                                 self.current_api.full_url,
                                                                                 self.current_api.response_error)

    def test_api_ad_landing_check_app(self):
        """function for check app in answer"""
        self.check_current_api.check_app()

        assert self.check_current_api.check_app_no_error, "{0}\n{1}\n{2}".format(self.current_api.response_code,
                                                                                 self.current_api.full_url,
                                                                                 self.current_api.response_error)
