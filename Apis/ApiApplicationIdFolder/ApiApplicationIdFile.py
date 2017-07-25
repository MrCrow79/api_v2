from Apis.ApiMethodsAndPropertiesFile import *


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



