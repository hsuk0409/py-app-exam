import unittest
import backend


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.domain = 'http://localhost:5000/api/multiply'

    def test_get(self):
        self.assertEqual(backend.multiply(6, 3), 18)


class UnitTest(unittest.TestCase):
    def test_right(self):
        self.assertEqual(backend.multiply(10, 2), 20)


if __name__ == '__main__':
    unittest.main()