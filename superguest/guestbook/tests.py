from django.test import TestCase
from guestbook.models import Comment


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
        response = self.client.post('/', data={'comment_text': 'Very peaceful'})
        self.assertIn('Very peaceful', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class CommentModelTest(TestCase) :

    def test_saving_and_retriving_comments (self) :

        first_comment = Comment()
        first_comment.text = "the first comment"
        first_comment.save()

        second_comment = Comment()
        second_comment.text = "the second comment"
        second_comment.save()

        saved_comments = Comment.objects.all()
        self.assertEqual(saved_comments.count(),2)

        first_saved_comment = saved_comments[0]
        second_saved_comment = saved_comments[1]
        self.assertEqual(first_saved_comment.text, 'the first comment')
        self.assertEqual(second_saved_comment.text, 'the second comment')
    
