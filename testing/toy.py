### MY TOY FILE ###

# Start with a basic function:
# a + b = c

# Now need to work out how to accept inputs for this function.
# Turn the function into a definition inside a class with an __init__.


class MyFunction:
    """
    A basic maths class providing four functions to work with.

    Arguments must be floats.
    """
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        c = self.a + self.b
        return c

    def subtract(self):
        d = self.a - self.b
        return d

    def multiply(self):
        e = self.a * self.b
        return e

    def divide(self):
        f = self.a / self.b
        return f

# Next I need to write a different class which uses the functions in this class.
# This will properly allow an integration test to be written as it will give
# the toy some hierarchy.

class BlackHole:
    """
    A class which uses the basic maths functions to provide an answer to a
    more complex function.

    Gives this toy some hierarchy to test.

    Args:
        * v = velocity in m/s
        * r = radius in m^2

    Returns:
        * mass in kg
    """
    def __init__(self, v, r):
        self.v = float(v)
        self.r = float(r)
        self.G = 6.674 * (10**11)

    def bh_mass(self):
        vsq = MyFunction(self.v, self.v).multiply()
        numerator = MyFunction(vsq, self.r).multiply()
        mass = MyFunction(numerator, self.G).divide()
        return mass



