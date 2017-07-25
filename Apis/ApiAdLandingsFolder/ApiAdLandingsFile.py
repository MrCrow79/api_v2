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


class CheckApiAdLandings:

    def __init__(self, api_ad_landings_instance):
        self.no_response_errors = api_ad_landings_instance.no_response_errors
        self.response_data = api_ad_landings_instance.response_data
        self.response_code = api_ad_landings_instance.response_code
        self.full_url = api_ad_landings_instance.full_url
        self.url = api_ad_landings_instance.url
        self.check_data_no_errors = False
        self.check_net_no_error = False
        self.check_app_no_error = False

    def check_data(self):
        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors

        error_message = 'landings_locales, {0} has non-{1} type, {2}\n{3}'
        error_message_element = 'landings_locales, element, {0} has non-{1} type, {2}\n{3}'

        check_type(list, self.response_data, '', error_message)
        for locale in self.response_data:
            check_data_in_dict(locale, (('id', 'app', 'cluster', 'net'), int), error_message_element)
            check_data_in_dict(locale, (('name', 'url', 'locale', 'link_type', 'type'), str), error_message_element)

    def check_net(self):
        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors

        net = int(self.full_url.split('net_id=')[1].split('&')[0])

        for locale in self.response_data:
            if locale.get('net') != net:
                logger(full_url=self.full_url, message='net in answer != 14, net = {0}'.format(net))
            else:
                self.check_net_no_error = True

    def check_app(self):
        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors

        app = int(self.full_url.split('app_id=')[1].split('&')[0])

        for locale in self.response_data:
            if locale.get('app') != app:
                logger(full_url=self.full_url, message='app in answer != app in url\napp_url = {0}\napp_answer = {1}'
                                                       ''.format(app, locale.get('app')))
            else:
                self.check_app_no_error = True
