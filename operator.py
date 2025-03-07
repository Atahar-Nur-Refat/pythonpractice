# Python Arithmetic Operators
x, y = 10, 3
print("Addition:", x + y)  # 13
print("Subtraction:", x - y)  # 7
print("Multiplication:", x * y)  # 30
print(f"Division: {x / y:.2f}")  # Output: Division: 3.33print("Modulus:", x % y)  # 1 (remainder)
print("Exponentiation:", x ** y)  # 10^3 = 1000
print("Floor Division:", x // y)  # 3 (removes decimal)

# Python Assignment Operators
a = 5
a += 3  # a = a + 3
print("a after += 3:", a)  # 8#as i declared a+= 3 thats why in hre it will print 8 not 5
a -= 2  # a = a - 2
print("a after -= 2:", a)  # 6#now 8 will be the value of a and 8-2 will happen
a *= 4  # a = a * 4
print("a after *= 4:", a)  # 24
a /= 6  # a = a / 6
print("a after /= 6:", a)  # 4.0
a %= 3  # a = a % 3
print("a after %= 3:", a)  # 1.0
a //= 2  # a = a // 2
print("a after //= 2:", a)  # 0.0
a **= 3  # a = a ** 3
print("a after **= 3:", a)  # 0.0

# Python Comparison Operators
p, q = 10, 5
print("Equal:", p == q)  # False
print("Not Equal:", p != q)  # True
print("Greater than:", p > q)  # True
print("Less than:", p < q)  # False
print("Greater or equal:", p >= q)  # True
print("Less or equal:", p <= q)  # False

# Python Logical Operators
m, n = True, False
print("AND:", m and n)  # False (Both must be True)
print("OR:", m or n)  # True (At least one is True)
print("NOT:", not m)  # False (Reverses the value)

# Python Identity Operators
a, b = [1, 2, 3], [1, 2, 3]
c = a
print("a is c:", a is c)  # True (Same memory reference)
print("a is b:", a is b)  # False (Different objects with same values)
print("a is not b:", a is not b)  # True

# Python Membership Operators
text = "Hello World"
print("'H' in text:", 'H' in text)  # True
print("'z' not in text:", 'z' not in text)  # True

# Python Bitwise Operators
x, y = 6, 3  # 6 = 110, 3 = 011 in binary
print("Bitwise AND:", x & y)  # 2 (010)
print("Bitwise OR:", x | y)  # 7 (111)
print("Bitwise XOR:", x ^ y)  # 5 (101)
print("Bitwise NOT:", ~x)  # -7
print("Left Shift:", x << 2)  # 24 (11000)
print("Right Shift:", x >> 2)  # 1 (001)

# Operator Precedence means which operators operation is done first then which comes next in order
print("Precedence Example 1:", (6 + 3) - (6 + 3))  # 0
print("Precedence Example 2:", 100 + 5 * 3)  # 115
