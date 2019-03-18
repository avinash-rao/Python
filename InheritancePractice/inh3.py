from abc import ABCMeta, abstractmethod

class BaseClass():
    __metaclass__ = ABCMeta         # Setting up abstract class

    @abstractmethod
    def printStark(self):
        pass


class DerivedClass(BaseClass):
    def printStark(self):
        print("Stark")


# Note: If you create an instance of BaseClass, it won't show any Error. On calling printStark function, it runs the BaseClass function

d = DerivedClass()
d.printStark()