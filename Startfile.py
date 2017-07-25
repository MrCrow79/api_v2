import unittest
import cherrypy
from Apis.helper_functions import logger

loader = unittest.TestLoader()


class StartTests:

    @staticmethod
    def run_tests(test_level):
        suite = loader.discover(start_dir=r'.\Apis', pattern=test_level + '*Test.py')
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if result.errors:
            logger(errors=result.errors[0][0]._testMethodName, traceback=result.errors[0][1])
        if result.failures:
            logger(fails=result.failures[0][0]._testMethodName, traceback=result.failures[0][1])

        return result

    @staticmethod
    def str_test_result(test_result):
        return_string = r'<br>Started {0} cases<br>' \
                        '<br>Passed {3}' \
                        '<br>Failed {1}' \
                        '<br>errors {2}<br>' \
                        ''.format(test_result.testsRun, len(test_result.failures), len(test_result.errors),
                                  test_result.testsRun - (len(test_result.failures) + len(test_result.errors)))

        if test_result.failures:
            failures = str(test_result.failures).replace('<', '').replace('>', '').replace(r'\n', '<br>')
            return_string += r'<br>failures: <br>{0}'.format(failures)

        if test_result.errors:
            errors = str(test_result.errors).replace('<', '').replace('>', '').replace(r'\n', '<br>')
            return_string += r'<br>errors: <br>{0}'.format(errors)

        return return_string

    @cherrypy.expose
    def index(self):
        return 'there are 3 pages: /Smoke, /Model, /Data'

    @cherrypy.expose
    def smoke(self):
        fails = self.run_tests('Smoke')
        return self.str_test_result(fails)

    @cherrypy.expose
    def model(self):
        fails = self.run_tests('Model')
        return self.str_test_result(fails)

    @cherrypy.expose
    def data(self):
        fails = self.run_tests('Data')
        return self.str_test_result(fails)

# cherrypy.quickstart(StartTests())

#smoke = StartTests().run_tests('smoke')
#model = StartTests().run_tests('model')
data = StartTests().run_tests('data')
