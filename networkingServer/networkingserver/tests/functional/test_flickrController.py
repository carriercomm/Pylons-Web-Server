from networkingserver.tests import *

class TestFlickrcontrollerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='flickrController', action='index'))
        # Test response...
