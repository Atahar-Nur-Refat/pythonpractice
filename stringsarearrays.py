# Get the character at position 1 (remember that the first character has the position 0)
a = "Hello_World!"
print(a[5])  #0th index calculation
for x in "500 banana":
  print(x)


a = "Hello, World!"
print(len(a)) #The len() function returns the length of a string
txt = "The best things in life are free!"
print("free" in txt)  #Check if "free" or any other word is present in the following text:
print("HEEEYYY" in txt)
"""Use it in an if statement:
Print only if "free" and other word is present:"""
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  """Use it in an if statement:
  Print only if "hello" or any other word is not present:"""
  txt = "The best things in life are free!"
  if "Hello" not in txt:
      print("Yes, 'Hello' is not present.")
