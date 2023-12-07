import unittest
from fastapi.testclient import TestClient

from api.main import app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api_url = 'http://127.0.0.1:8000'
        self.client = TestClient(app)

    def test_get_existing_user_by_id(self):
        user_id: int = 1
        response = self.client.get(f"{self.api_url}/users/{user_id}")
        expected_response = {"id": 1, "name": "Biba"}
        print(response.content)
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json())

    def test_get_not_existing_user_by_id(self):
        user_id: int = 10000
        response = self.client.get(f"{self.api_url}/users/{user_id}")
        print(response.content)
        self.assertEqual(404, response.status_code)
        expected_detail = f"User with id = '{user_id}' does not exist"
        self.assertEqual(expected_detail, response.json()['detail'])

    def test_add_user(self):
        user_data = {"id": 4, "name": "Pupa"}
        response = self.client.post(f"{self.api_url}/users", json=user_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(user_data, response.json())

    def test_update_existing_user(self):
        user_data = {"id": 3, "name": "Lupa"}
        response = self.client.put(f"{self.api_url}/users/{user_data['id']}", json=user_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(user_data, response.json())

    def test_update_not_existing_user(self):
        user_data = {"id": 1000, "name": "Lupa"}
        user_id = user_data['id']
        response = self.client.put(f"{self.api_url}/users/{user_id}", json=user_data)
        self.assertEqual(404, response.status_code)
        expected_detail = f"User with id = '{user_id}' does not exist"
        self.assertEqual(expected_detail, response.json()['detail'])

    def test_delete_existing_user(self):
        user_id: int = 2
        response = self.client.delete(f"{self.api_url}/users/{user_id}")
        self.assertEqual(204, response.status_code)

    def test_delete_not_existing_user(self):
        user_id: int = 10000
        response = self.client.delete(f"{self.api_url}/users/{user_id}")
        self.assertEqual(response.status_code, 404)
        expected_detail = f"User with id = '{user_id}' does not exist"
        self.assertEqual(expected_detail, response.json()['detail'])

    def tearDown(self):
        app.dependency_overrides.clear()
