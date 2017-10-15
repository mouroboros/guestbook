from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os, unittest

class GuestTests (LiveServerTestCase):
       def setUp(self):
           self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
           self.browser.implicitly_wait(3)
           
       def tearDown (self):
            self.browser.quit()


       def test_first_user_lands_on_home_page (self) :
              # Upon leaving a guesthouse, John is offered
              # the opportunity to leave comments about his stay
              # via a web browser 
              self.browser.get('http://localhost:8000')
              # John notices the guesthouse title
              self.assertIn("Guesthouse",self.browser.title)
              # John is invited to leave a comment
              inputbox = self.browser.find_element_by_id('id_new_comment')
              self.assertEqual(
                     inputbox.get_attribute('placeholder'),
                     'Please enter a comment')
              # John types "A very nice stay"
              inputbox.send_keys('A very nice stay')
              # John hits enter, the page updates
              inputbox.send_keys(Keys.ENTER)
              time.sleep(5)
              # and the new page shows John's comment on the webpage
              table = self.browser.find_element_by_id('id_comment_table')
              rows = table.find_elements_by_tag_name('tr')
              self.assertTrue(
                     any(row.text == 'A very nice stay' for row in rows),
                     f"New comment item did not appear in table. Contents were:\n{table.text}"
                     )

       def test_second_user_adds_a_comment (self) :
              # Steve checks out the guestbook app
              self.browser.get('http://localhost:8000')
              # Steve notices the comment "A very nice stay" has already been
              # submitted by another guest.
              table = self.browser.find_element_by_id('id_comment_table')
              rows = table.find_elements_by_tag_name('tr')
              self.assertTrue(
                     any(row.text == 'A very nice stay' for row in rows),
                     f"first comment item did not appear in table. Contents were:\n{table.text}"
                     )
              # Steve types "I had a relaxing visit"
              inputbox = self.browser.find_element_by_id('id_new_comment')
              inputbox.send_keys('I had a relaxing visit')
              # Steve presses enter
              inputbox.send_keys(Keys.ENTER)
              time.sleep(5)
              # Steve is directed a new page which shows Steves comments
              table = self.browser.find_element_by_id('id_comment_table')
              rows = table.find_elements_by_tag_name('tr')
              self.assertTrue(
                     any(row.text == 'I had a relaxing visit' for row in rows),
                     f"first comment item did not appear in table. Contents were:\n{table.text}"
                     )
              # Steve also sees the original comments by John.
              self.assertTrue(
                     any(row.text == 'A very nice stay' for row in rows),
                     f"first comment item did not appear in table. Contents were:\n{table.text}"
                     )
