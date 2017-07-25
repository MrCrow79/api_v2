from Apis.helper_functions import *
import json
from Apis.ApiAdLandingsFolder import ApiAdLandingsFile


class CheckApiAdLandings:

    def __init__(self, instance):
        self.no_response_errors = instance.no_response_errors
        self.response_data = instance.response_data
        self.response_code = instance.response_code
        self.full_url = instance.full_url
        self.url = instance.url
        self.check_data_no_errors = False
        self.check_net_no_error = False
        self.check_app_no_error = False

    def __repr__(self):
        return 'code - {0}, full_url - {1}, no_response_errors - {2}'.format(self.response_code, self.full_url,
                                                                             self.no_response_errors)

    def check_model(self):
        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

            error_message = 'landings_locales, {0} has non-{1} type, {2}\n{3}'
            error_message_element = 'landings_locales, element, {0} has non-{1} type, {2}\n{3}'

            check_type(list, self.response_data, '', error_message)
            for locale in self.response_data:
                check_data_in_dict(locale, (('id', 'app', 'cluster', 'net'), int), error_message_element)
                check_data_in_dict(locale, (('name', 'url', 'locale', 'link_type', 'type'), str), error_message_element)

    def check_net(self):
        if self.no_response_errors:
            net = int(self.full_url.split('net_id=')[1].split('&')[0])
            for locale in self.response_data:
                if locale.get('net') != net:
                    print('{0}, has net != 14, net = {1}'.format(self.url, net))
                else:
                    self.check_net_no_error = True
        else:
            print('{0}, check_net, errors in data'.format(self.url))

    def check_app(self):
        if self.no_response_errors:
            app = int(self.full_url.split('app_id=')[1].split('&')[0])
            for locale in self.response_data:
                if locale.get('app') != app:
                    print('{0}, has app in answer != app in url\napp_url = {1}\napp_answer = {2}'
                          ''.format(self.url, app, locale.get('app')))
                else:
                    self.check_app_no_error = True
        else:
            print('{0}, check_app, errors in data'.format(self.url))


