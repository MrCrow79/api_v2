import unittest

from Apis.ModelTypicalTestsFolder.ModelTypes import *

apis_with_model_type_1 = open('Apis\\ModelTypicalTestsFolder\\apis_for_model',
                              'r').read().split('type_1')[1].split('type_')[0].split()
apis_with_model_type_2 = open('Apis\\ModelTypicalTestsFolder\\apis_for_model',
                              'r').read().split('type_2')[1].split('type_')[0].split()
apis_with_model_type_3 = open('Apis\\ModelTypicalTestsFolder\\apis_for_model',
                              'r').read().split('type_3')[1].split('type_')[0].split()


class TypicalModel(unittest.TestCase):
    def setUp(self):
        self.current_api = ApiMethodsAndProperties()
        self.current_api._type = 'get'

    def test_cases_for_apis_with_model_1(self):

        for k in apis_with_model_type_1:
            self.current_api._url = k
            self.current_api._full_url = k
            self.current_api.send_request(self.current_api)
            self.current_api.check_server_answer(self.current_api)

            self.check_current_api = ModelType1(self.current_api)
            self.check_current_api.check_model()

    def test_cases_for_apis_with_model_2(self):

        for k in apis_with_model_type_2:
            self.current_api._url = k
            self.current_api._full_url = k
            self.current_api.send_request(self.current_api)
            self.current_api.check_server_answer(self.current_api)

            self.check_current_api = ModelType2(self.current_api)
            self.check_current_api.check_model()

    def test_cases_for_apis_with_model_3(self):

        for k in apis_with_model_type_3:
            self.current_api._url = k
            self.current_api._full_url = k
            self.current_api.send_request(self.current_api)
            self.current_api.check_server_answer(self.current_api)

            self.check_current_api = ModelType3(self.current_api)
            self.check_current_api.check_model()