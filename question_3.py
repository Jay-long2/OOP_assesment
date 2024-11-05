class Animal():
    def __init__(self):
        pass

    def eat(self):
        return "Eating"
    
    def sleep(self):
        return "Sleeping"
    
class Dog(Animal):

    def bark(self):
        return "The dog is barking!"

creature = Dog()
# Using inherited methods from Animal
print(creature.eat())
print(creature.sleep())
# Using the new method from Dog
print(creature.bark())

        