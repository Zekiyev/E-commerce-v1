from unittest import skip

from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.http import HttpRequest

from django.contrib.auth.models import User
from store_app.models import Category, Product
from store_app.views import all_products

# @skip('demonstrating skipping')
# class TestSkip(TestCase):
#    def test_skip_example(self):
#        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')

#       self.factory = RequestFactory()
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
            Test allowed hosts
        """
#        response = self.c.get('/', HTTP_HOST='noaddress.com')
#        self.assertEqual(response.status_code, 400)
#        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store_app:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse('store_app:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
            Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
            Example: Using request factory
        """
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
