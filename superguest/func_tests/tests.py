from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os, unittest

class BlogTests (LiveServerTestCase):
       def setUp(self):
           self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

       def tearDown (self):
            self.browser.quit()

       # Insert our user story here
