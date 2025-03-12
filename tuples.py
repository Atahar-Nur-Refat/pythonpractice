thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)#Tuple items are ordered, unchangeable, and allow duplicate values and 0th indexing
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))#length determination

thistuple = ("apple",)#can be tuple as it has two items including a comma
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")#acnt be tuple with only one item
print(type(thistuple))
#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "goal")
print(tuple1)
#accessing tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#5 not included just like previous ones
#This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])#4 not included
#counting start from back and -1 not included here (-4 is orange -3 is kiwi -2 is melon)(-1 is mango which is not included)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#checking if an item is available in tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print("no its not in there")