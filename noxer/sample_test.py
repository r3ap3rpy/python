import unittest

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(3, 4) == 12

class Multiplier(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiply(3, 4), 12)


