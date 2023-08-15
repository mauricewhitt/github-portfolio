# Examples of Inheritance and Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implent this method")

class Dog(Animal):
    def speak(self):
        print("Woof, woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")




# Example of Polymorphism

def make_animal_speak(animal):
    animal.speak()
dog = Dog("Buddy")
cat = Cat("Whiskers")

make_animal_speak(dog) # output: woof, woof!
make_animal_speak(cat) # output: Meow!
