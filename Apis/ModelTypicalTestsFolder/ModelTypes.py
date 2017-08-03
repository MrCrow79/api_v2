from Apis.helper_functions import *
from Apis.ApiMethodsAndPropertiesFile import *


class ModelType1(DataForCheckApi):
    def __init__(self, instance):
        DataForCheckApi.__init__(self, instance)

    def check_model(self):

        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors
        error_message = '{0}'.format(self.url)
        error_message += ', {0} has non-{1}, {2}\n{3}'

        for k in self.response_data:
            check_data_in_dict(k, ('id', int), error_message)
            check_data_in_dict(k, ('name', str), error_message)


class ModelType2(DataForCheckApi):
    def __init__(self, instance):
        DataForCheckApi.__init__(self, instance)

    def check_model(self):

        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors
        error_message = '{0}'.format(self.url)
        error_message += ', {0} has non-{1}, {2}\n{3}'

        for k in self.response_data:
            check_data_in_dict(k, ('id', int), error_message)
            check_data_in_dict(k, ('value', str), error_message)


class ModelType3(DataForCheckApi):
    def __init__(self, instance):
        DataForCheckApi.__init__(self, instance)

    def check_model(self):

        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors
        error_message = '{0}'.format(self.url)
        error_message += ', {0} has non-{1}, {2}\n{3}'

        for k in self.response_data:
            check_data_in_dict(k, (('name', 'id'), str), error_message)
