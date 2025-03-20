# Polymorphism in Python

# Polymorphism allows methods/functions to have different behaviors based on the object they are acting upon.
# It can be applied in function calls, class methods, and even inheritance.

# Function Polymorphism

# Example 1: len() function works differently on different objects
# String
x = "Hello World!"
print(len(x))  # Output: 12 (Length of the string)

# Tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Output: 3 (Number of items in the tuple)

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # Output: 3 (Number of key-value pairs in the dictionary)


# Class Polymorphism

# Example 2: Different classes with the same method name, demonstrating polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

# Creating objects of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Using a for loop to call the same method `move()` on all objects
for x in (car1, boat1, plane1):
  x.move()  # Output: Drive! Sail! Fly!

# The method move() behaves differently depending on the object (Car, Boat, or Plane)


# Inheritance Class Polymorphism

# Example 3: Using inheritance with polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass  # Car inherits the move method from Vehicle

class Boat(Vehicle):
  def move(self):
    print("Sail!")  # Boat overrides the move method

class Plane(Vehicle):
  def move(self):
    print("Fly!")  # Plane overrides the move method

# Creating objects of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Using a for loop to call the move method on all objects
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()  # Output: Move! Sail! Fly!
