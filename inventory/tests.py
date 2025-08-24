from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token  
from .models import Category, Item


class APITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create a token for authentication
        self.token = Token.objects.create(user=self.user)  
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)  

        # Create a category
        self.category = Category.objects.create(name="Electronics")

        # Create an item
        self.item = Item.objects.create(
            name="Laptop",
            price=1000,
            category=self.category
        )

    def test_list_categories(self):
        url = reverse('category-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        url = reverse('category-list')
        data = {"name": "Furniture"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_items(self):
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item(self):
        url = reverse('item-list')
        data = {"name": "Phone", "price": 500, "category": self.category.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_price_patch(self):
        url = reverse('update-price', args=[self.item.id])
        data = {"price": 1200}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.price, 1200)

    def test_item_detail(self):
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
