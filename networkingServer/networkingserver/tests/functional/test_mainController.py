from networkingserver.tests import *

class TestMaincontrollerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='mainController', action='index'))
        # Test response...
