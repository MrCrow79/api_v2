import unittest
from Apis.ApiMethodsAndPropertiesFile import *

all_apis = open('Apis\\apis_for_smoke_test.txt', 'r').read().split()


class ApisSmoke(unittest.TestCase):
    has_errors = False

    def test_api_menu(self):

        for k in all_apis:
            self.current_api = ApiMethodsAndProperties()
            self.current_api._full_url = k
            self.current_api._type = 'get'
            self.current_api.send_request(self.current_api)
            self.current_api.check_server_answer(self.current_api)
            try:
                assert self.current_api.no_response_errors, '{0}'.format(self.current_api.response_error)
            except AssertionError:
                self.has_errors = True

        if self.has_errors:
            raise AssertionError
