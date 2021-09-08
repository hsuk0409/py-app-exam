from unittest import TestCase
import sample_requests


class TestSampleRequests(TestCase):

    def test_call_url(self):
        response = sample_requests.call_url()
        print(response)
        print(response.json())
        print(response.status_code)

        self.assertEqual(response.status_code, 200)