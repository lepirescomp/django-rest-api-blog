from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(self):
        testUser1 = User.objects.create_user("test1","test1@test1.com","123")
        testUser1.save()

        testpost1 = Post.objects.create(auth=testUser1, title="Title1", body="Body1")
        testpost1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        auth = f'{post.auth}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(auth, 'test1')
        self.assertEqual(title, 'Title1')
        self.assertEqual(body, 'Body1')
