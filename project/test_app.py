import unittest
import json

from .app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_GET_no_args(self):
        resp = self.app.get("/person")
        self.assertEqual(200, resp.status_code)

        '''
    def test_POST(self):
        data = json.dumps({"id": 1, "first_name": "devin", "last_name": "kadillak"})
        resp = self.app.post(data)
        self.assertEqual(200, resp.status_code)
        '''


