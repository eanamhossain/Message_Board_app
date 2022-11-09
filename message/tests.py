from audioop import reverse
from cgi import test
from turtle import title
from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePage(TestCase):
    def setUp(self):
        Post.objects.create(title='this is another test')
    
    def test_view_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_virw_usese_templates(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

        

