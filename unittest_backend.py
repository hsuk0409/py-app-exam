import unittest
import backend
import requests
import json

class UnitTestBackEnd(unittest.TestCase):
    def setUp(self):
        self.app = backend.app.test_client()
        self.right_param = {
            'param1': 3,
            'param2': 6
        }
        self.wrong_param = {
            'param1': 3
        }

    def test_wrong_param(self):
        response = self.app.get('/api/multiply', data=self.wrong_param)
        data = json.loads(response.get_data())
        self.assertEqual(18, data['response'])
        self.assertEqual(1, data['state'])

    def test_wrong_result(self):
        response = self.app.get('/api/multiply', data=self.right_param)
        data = json.loads(response.get_data())
        self.assertEqual(10, data['response'])
        self.assertEqual(1, data['state'])

    def test_multipy_right(self):
        response = self.app.get('/api/multiply', data=self.right_param)
        data = json.loads(response.get_data())
        self.assertEqual(18, data['response'])
        self.assertEqual(1, data['state'])


if __name__ == '__main__':
    unittest.main()