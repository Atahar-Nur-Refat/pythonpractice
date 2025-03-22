#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)

# Using the pow() function
# pow(x, y) returns x raised to the power of y (x^y)
x = pow(4, 3)  # 4^3 = 4 * 4 * 4 = 64
print(x)  # Output: 64

# Importing the math module to use additional mathematical functions
import math

# Using math.sqrt() to find the square root of a number
x = math.sqrt(64)  # Square root of 64 is 8.0
print(x)  # Output: 8.0

# Using math.ceil() and math.floor()
y = math.ceil(1.4)   # Rounds 1.4 up to the nearest integer (2)
z = math.floor(1.4)  # Rounds 1.4 down to the nearest integer (1)
print(y)  # Output: 2
print(z)  # Output: 1

# Using math.pi to get the value of PI
pi_value = math.pi  # PI value (3.141592653589793)
print(pi_value)  # Output: 3.141592653589793
