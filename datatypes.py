# Define each variable
x = "Hello World"
print(type(x))  # <class 'str'>

x = 20
print(type(x))  # <class 'int'>

x = 20.5
print(type(x))  # <class 'float'>

x = 1j
print(type(x))  # <class 'complex'>

x = ["apple", "banana", "cherry"]
print(type(x))  # <class 'list'>

x = ("apple", "banana", "cherry")
print(type(x))  # <class 'tuple'>

x = range(6)
print(type(x))  # <class 'range'>

x = {"name": "John", "age": 36}
print(type(x))  # <class 'dict'>

x = {"apple", "banana", "cherry"}
print(type(x))  # <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(type(x))  # <class 'frozenset'>

x = True
print(type(x))  # <class 'bool'>

x = b"Hello"
print(type(x))  # <class 'bytes'>

x = bytearray(5)
print(type(x))  # <class 'bytearray'>

x = memoryview(bytes(5))
print(type(x))  # <class 'memoryview'>

x = None
print(type(x))  # <class 'NoneType'>
