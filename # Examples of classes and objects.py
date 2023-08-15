# Examples of classes and objects

class Dog:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def bark(self):
        print("Woof, woof!")

# Example of objects

my_dog = Dog("Bubby", 3)
 
print(my_dog.name) # Output: Bubby
print(my_dog.age)  # Output: 3
my_dog.bark()      # Output: Woof, woof!
