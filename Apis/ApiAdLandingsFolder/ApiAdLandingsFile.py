from Apis.ApiMethodsAndPropertiesFile import *
from jsonobject import *
from Apis.helper_functions import *


class ApiAdLandings(ApiMethodsAndProperties):

    def __init__(self):
        ApiMethodsAndProperties.__init__(self)
        self._type = 'get'
        self._url = '/test'
        self._required_params = {'net_id': 14, 'app_id': 3}
        self._full_url = self._url
        self.set_params(self, self.required_params)

    def check_model(self):
        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors

        error_message = 'landings_locales, {0} has non-{1} type, {2}\n{3}'
        error_message_element = 'landings_locales, element, {0} has non-{1} type, {2}\n{3}'

        check_type(list, self.response_data, '', error_message)
        for locale in self.response_data:
            check_data_in_dict(locale, (('id', 'app', 'cluster', 'net'), int), error_message_element)
            check_data_in_dict(locale, (('name', 'url', 'locale', 'link_type', 'type'), str), error_message_element)
