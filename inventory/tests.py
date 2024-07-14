from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import InventoryItem

class InventoryItemModelTest(TestCase):
    def setUp(self):
        self.item = InventoryItem.objects.create(
            name='Test Item',
            description='This is a test item',
            quantity=10,
            price=9.99
        )

    def test_inventory_item_creation(self):
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'This is a test item')
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(self.item.price, 9.99)

class InventoryItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {
            'name': 'API Test Item',
            'description': 'This is an API test item',
            'quantity': 5,
            'price': 19.99
        }
        self.item = InventoryItem.objects.create(**self.item_data)
        self.url = reverse('inventoryitem-list')

    def test_create_inventory_item(self):
        response = self.client.post(self.url, self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 2)
        self.assertEqual(InventoryItem.objects.get(id=2).name, 'API Test Item')

    def test_get_inventory_item(self):
        response = self.client.get(reverse('inventoryitem-detail', kwargs={'pk': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)
