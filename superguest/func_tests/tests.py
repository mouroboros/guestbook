from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os, unittest

class GuestTests (LiveServerTestCase):
       def setUp(self):
           self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

       def tearDown (self):
            self.browser.quit()

       # Insert our user story here

       def test_user_lands_on_home_page (self) :
              # Upon leaving a guesthouse, John is offered
              # the opportunity to leave comments about his stay
              # via a web browser 
              self.browser.get('http://localhost:8000')
              # John notices the guesthouse title
              self.assertIn("Guesthouse",self.browser.title)
              # John is invited to leave a comment
              # John types "A very nice stay"
              # John hits enter, the page updates
              # and the new page shows John's comment on the webpage
