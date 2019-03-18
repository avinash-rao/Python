class Base(object):             # Passing object is necessary as it will allow to call Base class variable from derived class
    def Ham(self):
        print("Ham")


class Derived(Base):
    pass

# Instance of derived class created
x = Derived()

# Called function of base class
x.Ham()