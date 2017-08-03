import unittest
import time
from Apis.ApiMethodsAndPropertiesFile import *

all_apis = open('Apis\\SmokeTests\\apis_for_smoke_test.txt', 'r').read().split()


class ApisSmoke(unittest.TestCase):
    has_errors = False
    errors = []

    def test_api_menu(self):

        for k in all_apis:
            timer = time.time()
            self.current_api = ApiMethodsAndProperties()
            self.current_api._full_url = k
            self.current_api._type = 'get'
            self.current_api.send_request(self.current_api)
            self.current_api.check_server_answer(self.current_api)
            try:
                assert self.current_api.no_response_errors, '{0}'.format(self.current_api.response_error)
            except AssertionError as error:
                self.has_errors = True
                self.errors.append(error)
                logger(full_url=self.current_api.full_url, error=self.current_api.response_error)
            finally:
                logger(url=self.current_api.full_url, time=(time.time()-timer))

        if self.has_errors:
            raise AssertionError
