# Iterators in Python

# An iterator is an object that contains a countable number of values
# It implements the iterator protocol with the methods __iter__() and __next__()

# Example 1: Getting an iterator from a tuple and iterating through it
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # Creating an iterator

# Using next() to get each value
print(next(myit))  # Output: apple
print(next(myit))  # Output: banana
print(next(myit))  # Output: cherry

# Example 2: Strings are also iterable and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # Output: b
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a

# Example 3: Looping through an iterator using a for loop
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)  # Prints each item in the tuple

mystr = "banana"
for x in mystr:
    print(x)  # Prints each character in the string

# The for loop automatically handles iteration using the iterator protocol

# Example 4: Creating a custom iterator using a class
class MyNumbers:
    def __iter__(self):
        self.a = 1  # Initialize starting value
        return self

    def __next__(self):
        x = self.a  # Store current value
        self.a += 1  # Increment for next iteration
        return x  # Return current value

# Creating an instance of MyNumbers
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # Output: 1
print(next(myiter))  # Output: 2
print(next(myiter))  # Output: 3
print(next(myiter))  # Output: 4
print(next(myiter))  # Output: 5

# Example 5: Using StopIteration to prevent infinite loops
class MyNumbers:
    def __iter__(self):
        self.a = 1  # Initialize counter
        return self

    def __next__(self):
        if self.a <= 20:  # Stop after 20 iterations
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Raise StopIteration error when limit is reached

# Creating an instance
myclass = MyNumbers()
myiter = iter(myclass)

# Using a for loop to iterate through the numbers
for x in myiter:
    print(x)  # Prints numbers from 1 to 20
