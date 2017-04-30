class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
    pass

class Cat(Animal):
    def __init__(self, hairy):
        self.hairy = hairy
    pass

class Person(object):
    def __init__(self, name):
        self.name = name
    pass
        
class Immigrant(Person):
    def __init__(self, citizen):
        self.citizen = citizen
    pass

Igor = Immigrant("Igor")

print Igor.citizen
