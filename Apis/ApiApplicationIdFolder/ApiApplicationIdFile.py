from Apis.ApiMethodsAndPropertiesFile import *
from Apis.helper_functions import *


class ApiApplicationId(ApiMethodsAndProperties):

    def __init__(self):
        ApiMethodsAndProperties.__init__(self)
        self._type = 'get'
        self._url = '/test/{0}'
        self._full_url = self.url
        self.set_params(self, self.required_params)

    @property
    def full_url(self):
        return self._full_url

    @full_url.setter
    def full_url(self, value):
        self._full_url = self._url.format(value)

    def check_model(self):

        if not self.no_response_errors:
            logger(full_url=self.full_url, error_code=self.response_code, response_data=self.response_data)

        assert self.no_response_errors
        error_message = 'api_applications_id, {0} has non-{1}, {2}\n{3}'
        error_message_nets = 'api_applications_id, supported_nets, {0},  has non-{1}, {2}\n{3}'
        error_message_cluster = 'api_applications_id, supported_nets, clusters, {0}, has non-{1}, {2}\n{3}'
        error_message_platform = 'api_applications_id, supported_nets, platform, {0}, has non-{1}, {2}\n{3}'
        error_message_client = 'api_applications_id, supported_nets, platform, client, {0}, has non-{1}, {2}\n{3}'

        check_data_in_dict(self.response_data, ('id', int), error_message)
        check_data_in_dict(self.response_data, (('name', 'short_name'), str), error_message)
        check_data_in_dict(self.response_data, (('full_integration', 'is_multiplatform'), bool), error_message)

        check_data_in_dict(self.response_data, ('supported_nets', (list, None)), error_message)
        for net in self.response_data.get('supported_nets'):
            check_data_in_dict(net, ('id', int), error_message_nets)
            check_data_in_dict(net, (('name', 'short_name', 'default_device'), str), error_message_nets)
            check_data_in_dict(net, ('support_different_devices', bool), error_message_nets)

            check_data_in_dict(net, ('clusters', list), error_message_nets)
            for cluster in net.get('clusters'):
                check_data_in_dict(cluster, (('name', 'short_name'), str), error_message_cluster)
                check_data_in_dict(cluster, (('id', 'db_id'), int), error_message_cluster)

                check_data_in_dict(net, ('platforms', list), error_message_nets)
                for platform in net.get('platforms'):
                    check_data_in_dict(platform, ('id', int), error_message_platform)
                    check_data_in_dict(platform, ('name', str), error_message_platform)

                    check_data_in_dict(platform, ('clients', list), error_message_platform)
                    for client in platform.get('clients'):
                        check_data_in_dict(client, ('id', int), error_message_client)
                        check_data_in_dict(client, ('name', str), error_message_client)



