
#Method	                  Description

#capitalize()	          Converts the first character to upper case
#casefold()	              Converts string into lower case
# center()	              Returns a centered string
# count()	                  Returns the number of times a specified value occurs in a string
# encode()	              Returns an encoded version of the string
# endswith()	              Returns true if the string ends with the specified value
#expandtabs()	          Sets the tab size of the string
#find()	                  Searches the string for a specified value and returns the position of where it was found
#format()	              Formats specified values in a string
#format_map()	          Formats specified values in a string
#index()	                  Searches the string for a specified value and returns the position of where it was found
#isalnum()	              Returns True if all characters in the string are alphanumeric
#isalpha()	              Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning
# capitalize() - Converts the first character to upper case
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# casefold() - Converts string into lower case
text = "HELLO WORLD"
print(text.casefold())  # Output: "hello world"

# center() - Returns a centered string
text = "hello"
print(text.center(20, "*"))  # Output: "***hello******"

# count() - Returns the number of times a specified value occurs in a string mane kono ekta letter koybar ache ekta line a
text = "hello world"
print(text.count("o"))  # Output: 2

# encode() - Returns an encoded version of the string
text = "hello"
print(text.encode())  # Output: b'hello' The result b'hello' means that "hello" is now represented as bytes, where each character in the string is translated into its corresponding byte value in UTF-8 encoding.

# endswith() - Returns true if the string ends with the specified value
text = "hello world"
print(text.endswith("world"))  # Output: True

# expandtabs() - Sets the tab size of the string
text = "hello\tworld"
print(text.expandtabs(4))  # Output: "hello   world"

# find() - Searches the string for a specified value and returns the position of where it was found
text = "hello world"
print(text.find("world"))  # Output: 6

# format() - Formats specified values in a string
text = "Hello, {}!"
print(text.format("John"))  # Output: "Hello, John!"

# format_map() - Formats specified values in a string
text = "Hello, {name}!"
print(text.format_map({"name": "John"}))  # Output: "Hello, John!"

# index() - Searches the string for a specified value and returns the position of where it was found
text = "hello world"
print(text.index("world"))  # Output: 6

# isalnum() - Returns True if all characters in the string are alphanumeric
text = "hello123"
print(text, text.isalnum())  # This prints both the string and the result in one line
 # Output: True

# isalpha() - Returns True if all characters in the string are in the alphabet
text = "hello"
print(text.isalpha())  # Output: True

# isascii() - Returns True if all characters in the string are ASCII characters
text = "hello"
print(text.isascii())  # Output: True

# isdecimal() - Returns True if all characters in the string are decimals
text = "12345"
print(text.isdecimal())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
text = "12345"
print(text.isdigit())  # Output: True

# isidentifier() - Returns True if the string is an identifier
text = "variable_name"
print(text.isidentifier())  # Output: True

# islower() - Returns True if all characters in the string are lowercase
text = "hello"
print(text.islower())  # Output: True

# isnumeric() - Returns True if all characters in the string are numeric
text = "12345"
print(text.isnumeric())  # Output: True

# isprintable() - Returns True if all characters in the string are printable
text = "hello"
print(text.isprintable())  # Output: True

# isspace() - Returns True if all characters in the string are whitespaces
text = "     "
print(text.isspace())  # Output: True

# istitle() - Returns True if the string follows the rules of a title
text = "Hello World"
print(text.istitle())  # Output: True

# isupper() - Returns True if all characters in the string are uppercase
text = "HELLO"
print(text.isupper())  # Output: True

# join() - Joins the elements of an iterable to the end of the string
text = "+"
print(text.join(["a ", " b ", " c"]))  # Output: "a-b-c"

# ljust() - Returns a left justified version of the string
text = "hello"
print(text.ljust(10, "*"))  # Output: "hello*****"

# lower() - Converts a string into lowercase
text = "HELLO"
print(text.lower())  # Output: "hello"

# lstrip() - Returns a left trim version of the string
text = "   hello"
print(text.lstrip())  # Output: "hello"

# maketrans() - Returns a translation table to be used in translations
trans = str.maketrans("abc", "123")
text = "aabbcc"
print(text.translate(trans))  # Output: "112233"

# partition() - Returns a tuple where the string is parted into three parts
text = "hello world"
print(text.partition(" "))  # Output: ('hello', ' ', 'world')

# replace() - Returns a string where a specified value is replaced with a specified value
text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

# rfind() - Searches the string for a specified value and returns the last position of where it was found
text = "hello world"
print(text.rfind("o"))  # Output: 7

# rindex() - Searches the string for a specified value and returns the last position of where it was found
text = "hello world"
print(text.rindex("o"))  # Output: 7

# rjust() - Returns a right justified version of the string
text = "hello"
print(text.rjust(10, "*"))  # Output: "*****hello"

# rpartition() - Returns a tuple where the string is parted into three parts
text = "hello world"
print(text.rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit() - Splits the string at the specified separator, and returns a list
text = "apple,banana,cherry"
print(text.rsplit(","))  # Output: ['apple', 'banana', 'cherry']

# rstrip() - Returns a right trim version of the string
text = "hello    "
print(text.rstrip())  # Output: "hello"

# split() - Splits the string at the specified separator, and returns a list
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

# splitlines() - Splits the string at line breaks and returns a list
text = "apple\nbanana\ncherry"
print(text.splitlines())  # Output: ['apple', 'banana', 'cherry']

# startswith() - Returns true if the string starts with the specified value
text = "hello world"
print(text.startswith("hello"))  # Output: True

# strip() - Returns a trimmed version of the string
text = "   hello world   "
print(text.strip())  # Output: "hello world"

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

# title() - Converts the first character of each word to upper case
text = "hello world"
print(text.title())  # Output: "Hello World"

# translate() - Returns a translated string
trans = str.maketrans("abc", "123")
text = "aabbcc"
print(text.translate(trans))  # Output: "112233"

# upper() - Converts a string into upper case
text = "hello"
print(text.upper())  # Output: "HELLO"

# zfill() - Fills the string with a specified number of 0 values at the beginning
text = "42"
print(text.zfill(5))  # Output: "00042"
# Example of maketrans() method
# The translation table is created using the maketrans() method
translation_table = str.maketrans("abc", "123")

text = "abc"
new_text = text.translate(translation_table)

print("Original text:", text)  # Output: abc
print("Translated text:", new_text)  # Output: 123

# Example of format_map() method
person = {"name": "John", "age": 30}
text = "My name is {name} and I am {age} years old.".format_map(person)

print(text)  # Output: My name is John and I am 30 years old.
