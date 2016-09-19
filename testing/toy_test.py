### MY TOY TEST FILE ###

# This is an small example of bottom-up integration testing.

import toy
import unittest

class TestMyFunction(unittest.TestCase):
    # Start with some unit tests for the basic functionality
    def test_add(self):
        self.assertEqual(toy.MyFunction(1., 2.).add(), 3.)

    def test_subtract(self):
        self.assertEqual(toy.MyFunction(6., 2.).subtract(), 4.)

    def test_multiply(self):
        self.assertEqual(toy.MyFunction(3., 3.).multiply(), 9.)

    def test_divide(self):
        self.assertEqual(toy.MyFunction(3., 3.).divide(), 1.)

    # Check that error will occur if anything other than a float is used
    def test_nan(self):
        self.assertRaises(ValueError, toy.MyFunction, 'one', 'two')

    # Now check that the hierarchy works properly
    def test_bh(self):
        self.assertEqual(toy.BlackHole(500., 1000.).bh_mass(),
                         0.00037458795325142344)


if __name__ == '__main__':
    unittest.main()

