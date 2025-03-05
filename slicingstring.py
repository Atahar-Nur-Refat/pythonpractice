
"""b[2:4] means:
Start at index 2, which is 'l' (the 3rd character).
Stop at index 4, which means it will stop before index 4, so it will stop at 'l' (the 4th character), excluding it.
So, the characters that are actually printed are:
Index 2: 'l'
Index 3: 'l' starting index always counts for all kinds of slicing
and ending index always excluded and doesn't count"""

b = "Hello, World!"
print(b[2:10])
#Get the characters from the start to position 6 (not included):
b = "Hello, World!"
print(b[:6])
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
"""negative indexing a pichon theke gona suru hobe 
ekhane 1th indexing mane 1 theke gona suru hobe and same vabe ending index is excluded
negative indexing means counting from the backwards and start from 1 which is called
1th indexing  """
b = "Hello, World!"
print(b[-6:-4])