import json
from Apis.helper_functions import logger

from Connectors import bo_connector

server = bo_connector.server


class ApiMethodsAndProperties:
    def __init__(self):
        self._url = 'ApiMethodsAndProperties hasn\'t url'
        self._type = 'ApiMethodsAndProperties hasn\'t type'
        self._required_params = {}
        self.params = None
        self._server = server
        self.request_data = {}
        self._error_page = ") Marketing Backoffice/</title>"
        self.no_response_errors = None
        self.response_data = None
        self.response_code = None
        self._full_url = self._url

    def __repr__(self):
        return 'server - {0},  type - {1},  url -  {2}, required params - {3}' \
               ''.format(self._server, self.type, self.url, self.required_params)

    @property
    def url(self):
        return self._url

    @property
    def type(self):
        return self._type

    @property
    def required_params(self):
        return self._required_params

    @property
    def full_url(self):
        return self._full_url

    @property
    def error_page(self):
        return self._error_page

    @staticmethod
    def set_params(api_instance,  new_params):

        api_instance.params = new_params

        if api_instance.type.lower() == 'get':

            new_params_string = '?'
            for new_param in new_params.items():
                new_params_string += '{0}={1}&'.format(new_param[0], new_param[1]).lower()

            for required_param in api_instance.required_params.items():
                if required_param[0].lower() not in new_params_string:
                    new_params_string += '{0}={1}&'.format(required_param[0], required_param[1]).lower()

            api_instance._full_url = api_instance.url + new_params_string[:-1]  # delete last symbol = &

        elif api_instance.type.lower() == 'post':

            api_instance.params = {}

            api_instance.params = api_instance.required_param
            for element in new_params.items():
                if api_instance.params.get(element[0]) is None:
                    api_instance.params[element[0]] = element[1]

    @staticmethod
    def send_request(api_instance):
        api_instance.response_data = bo_connector.send_request(api_instance)

    @staticmethod
    def check_server_answer(api_instance):
        api_instance.no_response_errors = False

        api_instance.response_code = api_instance.response_data.status_code
        api_instance.response_data = api_instance.response_data.text

        if ApiMethodsAndProperties()._error_page in api_instance.response_data:
            api_instance.response_error = 'server backs html page like {0}...' \
                                        ''.format(ApiMethodsAndProperties()._error_page)
            # print(api_instance.full_url, 'has error. server return typical error html page')
        elif api_instance.response_code in range(200, 400):
            api_instance.response_data = json.loads(api_instance.response_data)
            api_instance.no_response_errors = True
        else:
            api_instance.response_error = api_instance.response_data
            # print('ERROR: code = {0}, api = {1}'.format(api_instance.response_code, api_instance.full_url))





