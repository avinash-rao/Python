class Base():
    def __init__(self):
        self.x = 10

    def test(self):
        print("Baratheon")


class Derived(Base):
    def __init__(self):
        self.x = 20

    def test(self):
        print("Stark")


d = Derived()

# This will print out the variables and functions inside Derived class and not Base class
# The Derived class methods and properties override Base class variables and methods
print(d.x)
d.test()


# Another dunder function used widely with inheritance
# This tells what all classes are inheriting from the Base class
print(Base.__subclasses__())