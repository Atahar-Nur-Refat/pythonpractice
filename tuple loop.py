# Define a tuple with three fruit names
thistuple = ("apple", "banana", "cherry")

# Start a for loop to iterate through each item in the tuple
for x in thistuple:
    # Print each item (fruit) in the tuple one by one
    print(x)
# Define a tuple with three fruit names
thistuple = ("apple", "banana", "cherry")

# Start a for loop with range() to iterate through the indices of the tuple
for i in range(len(thistuple)):
    # Print each item by accessing it using the index (i)
    print(thistuple[i])
    #using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1