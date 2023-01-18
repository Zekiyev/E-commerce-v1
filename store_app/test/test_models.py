from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from store_app.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
#       self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(title='django beginners', category_id=1,
                                            created_by_id=1, slug='django-beginners',
                                            image='django', price=20)

        self.data2 = Product.objects.create(title='django advanced', category_id=1, price=20,
                                            slug='django-advanced', image='django',
                                            is_active=False, created_by_id=1)

    def test_products_model_entry(self):
        """
            Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

#    def test_products_url(self):
#        """
#           Test product model slug and URL reverse
#        """
#        data = self.data1
#        url = reverse('store:product_detail', args=[data.slug])
#        self.assertEqual(url, '/item/django-beginners/')
#        response = self.client.post(
#            reverse('store:product_detail', args=[data.slug]))
#        self.assertEqual(response.status_code, #200)
#    def test_products_custom_manager_basic(self):
#        """
#        Test product model custom manager returns only active products
#        """
#        data = Product.products.all()
#        self.assertEqual(data.count(), 1)
