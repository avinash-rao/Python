class Character(object):               # Very imp to pass object in this case
    def __init__(self, name):
        self.health = 100
        self.name = name

    def printName(self):
        print(self.name)


class Blacksmith(Character):
    def __init__(self, name, forgeName):
        super(Blacksmith, self).__init__(name)       # Calls the __init__ function of base class
        self.forge = Forge(forgeName)


class Forge:
    def __init__(self, forgeName):
        self.name = forgeName


x = Blacksmith("Bob", "Rick\'s Forge")
print(x.health)
x.printName()
print(x.forge.name)