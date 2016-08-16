### MY TOY FILE ###

# Start with a basic function:
#a + b = c

# Now need to work out how to accept inputs for this function.
# Turn the function into a definition inside a class with an __init__.


class MyFunction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + self.b
        return c

    def subtract(self):
        d = self.a - self.b
        return d

    def multiply(self):
        e = self.a * self.b
        return e


#answer = MyFunction(1, 2)
#print(answer.add())

