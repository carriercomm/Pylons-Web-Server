Networking Lab 4
Daniel Robinson
0700662
Implement basic testing

Overview
--------
For this project, I implemented two different testing suites to test the functionality of my web app:
Nosetests and Selenium.


NoseTests
------------------

- Navigate to the networkingServer/ directory.
- Run:
	nosetests networkingserver/tests/functional/test_mainController.py
- The output should indicate 3 tests run and passed.

Selenium
------------------
- Start up the server:
	paster serve --reload development.ini
- Open Selenium IDE in Firefox
- Load the test suite named "Selenium.txt" in the root directory.
- Run the test suite.


