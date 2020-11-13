from django.test import TestCase
from rest_framework.test import APIClient

from todo_app.models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add(self):
        todo_data = {"title": "task 1", "description": "description"}
        response = self.client.post("/todos/", todo_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Todo.objects.filter(**todo_data).exists())

    def test_get(self):
        todo_data = {"title": "task 1", "description": "description"}
        todo = Todo(**todo_data)
        todo.save()

        response = self.client.get("/todos/")
        self.assertEqual(response.status_code, 200)
        todo_result = response.data['results'][0]
        self.assertEqual(todo_result.get("title"), todo.title)
        self.assertEqual(todo_result.get("description"), todo.description)

    def test_delete(self):
        todo_data = {"title": "task 1", "description": "description"}
        todo = Todo(**todo_data)
        todo.save()

        response = self.client.delete(f"/todos/{todo.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Todo.objects.filter(**todo_data).exists())
