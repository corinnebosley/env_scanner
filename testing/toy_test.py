### MY TOY TEST FILE ###

import toy
import unittest

class TestMyFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(toy.MyFunction(1, 2).add(), 3)

    def test_subtract(self):
        self.assertEqual(toy.MyFunction(6, 2).subtract(), 4)

    def test_multiply(self):
        self.assertEqual(toy.MyFunction(3, 3).multiply(), 9)


if __name__ == '__main__':
    unittest.main()

