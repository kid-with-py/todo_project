from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import TodoItem

class TodoItemAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_item_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'completed': False
        }
        self.todo_item = TodoItem.objects.create(**self.todo_item_data)
        self.todo_item_url = f'/todoitems/{self.todo_item.id}/'

    def test_get_todo_items(self):
        response = self.client.get('/todoitems/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo_item(self):
        response = self.client.post('/todoitems/', self.todo_item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_get_todo_item_detail(self):
        response = self.client.get(self.todo_item_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_item(self):
        updated_data = {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'completed': True
        }
        response = self.client.put(self.todo_item_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.title, 'Updated Todo')
        self.assertEqual(self.todo_item.description, 'Updated Description')
        self.assertEqual(self.todo_item.completed, True)

    def test_delete_todo_item(self):
        response = self.client.delete(self.todo_item_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TodoItem.objects.count(), 0)
