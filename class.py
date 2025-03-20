# Create a class named MyClass, with a property named x:
class MyClass:
    x = 5  # Class variable

# Printing the class itself (not an object, so this prints metadata)
print(MyClass)  # Output: <class '__main__.MyClass'>

# Create an object named p1, and print the value of x:
p1 = MyClass()  # Create an instance of MyClass
print(p1.x)  # Output: 5

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.fullname = name  # Assigning parameter value to an instance variable
        self.time = age       # Assigning parameter value to an instance variable

p1 = Person("John", 25)
print(p1.fullname)  # Output: John
print(p1.time)      # Output: 25

# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)  # Output: <__main__.Person object at some_memory_address>

# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # This method customizes what is printed when we use print(p1)
        return f"{self.name} ({self.age} years old)"

p1 = Person("John", 36)
print("The name is", p1.name, "and age is", p1.age)
# Output: The name is John and age is 36
print(p1)  # Output: John (36 years old)

# Object Methods - Creating a method inside a class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):  # A method inside the class
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

p1 = Person("John", 36)
p1.myfunc()
# Output: Hello, my name is John and I am 36 years old.

# Modify object properties - Set the age of p1 to 40:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p1.age = 40  # Modifying the property
print(p1.age, p1.name)  # Output: 40 John

# Delete object properties like age, and also delete the whole object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

del p1.age  # Deleting the 'age' attribute
