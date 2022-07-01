import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Player
from .serializers import UserSerializer

class TestError(TestCase):
    def test_index_page_loads_ok(self):
        print("hello")

class PlayerTestCases(APITestCase):
    def test_get_users(self):
        response = self.client.get("/players/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registration(self):
        data = {"username": "testcase", "email": "test@test.com", "password": "1234", "id": "1", }
        response = self.client.post("/players/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_by_id(self):
        data = {"username": "testcase", "email": "test@test.com", "password": "1234", }
        self.client.post("/players/", data)
        response = self.client.get("/players/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        data = {"username": "testcase", "email": "test@test.com", "password": "1234", }
        self.client.post("/players/", data)
        data2 = {"username": "1234"}
        response = self.client.patch("/players/1/", data2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "1234")

    def test_delete_user(self):
        data = {"username": "testcase", "email": "test@test.com", "password": "1234", }
        self.client.post("/players/", data)
        response = self.client.delete("/players/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

class ShopTestCase(APITestCase):
    def test_get_shops(self):
        response = self.client.get("/shops/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_shop(self):
        response = self.client.get("/shop/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    #def test_sort_items_by_price(self):
     #   data = 

class TaskTestCase(APITestCase):
    def test_get_tasks(self) :
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_tasks(self) :
        response = self.client.get("/task/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_task_by_id(self) :
        data = {"task": "wash the dishes", "task_difficulty": 2, "is_complete": False}
        self.client.post("/tasks/", data)
        response = self.client.get("/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_task(self) :
        data = {"task": "wash the dishes", "task_difficulty": 2, "is_complete": False}
        response = self.client.post("/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task_by_id(self):
        data = {"task": "wash the dishes", "task_difficulty": 2, "is_complete": False}
        response = self.client.post("/tasks/", data)
        data2 = {"is_complete" : True}
        response = self.client.patch("/tasks/1/", data2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["is_complete"], True)

    def test_delete_task_by_id(self):
        data = {"task": "wash the dishes", "task_difficulty": 2, "is_complete": False}
        self.client.post("/tasks/", data)
        response = self.client.delete("/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
        
