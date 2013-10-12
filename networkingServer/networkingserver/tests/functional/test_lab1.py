from networkingserver.tests import *

class TestLab1Controller(TestController):

    def test_index(self):
        response = self.app.get(url(controller='lab1', action='index'))
        # Test response...
