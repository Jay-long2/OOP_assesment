class Cat:

    def make_sound(self):
        return "meow"
    
class Dog:

    def make_sound(self):
        return "woof"
    
#function to demonstrate polymorphism
def animal_sounds(name):
    return name.make_sound()

dog = Dog()
cat = Cat()

# Passing instances of Cat and Dog to the animal_sound function
print(animal_sounds(dog))
print(animal_sounds(cat))
