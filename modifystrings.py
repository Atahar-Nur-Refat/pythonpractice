"""The upper() method returns the string in upper case meaning
it will return every letter in capital letter"""
a = "Hello, World!"
print(a.upper())
"""The lower() method returns the string in upper case meaning
it will return every letter in small letter"""
a = "Hello, World!"
print(a.lower())
"""The strip() method removes any whitespace from the beginning or the end """
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:here declared first so i means h is replaced by j
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] generally separates comma space and full stops