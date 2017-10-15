from django.test import TestCase


class HomePageTest (TestCase) :
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Le Corbusier Guesthouse </title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'Very peaceful'})
        self.assertIn('Very peaceful', response.content.decode())
