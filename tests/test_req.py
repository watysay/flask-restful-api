import unittest
import json

from app import app

class ReqTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_successful_get(self):
        # When
        response = self.app.get('/fruits/1', headers={"Content-Type": "application/json"}, data='')

        # Then
        self.assertEqual(str, type(response.json['name']))
        self.assertEqual(200, response.status_code)

        # When
        response = self.app.get('/fruits/2', headers={"Content-Type": "application/json"}, data='')

        # Then
        print(response.json['name'])
        self.assertEqual(str, type(response.json['name']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass