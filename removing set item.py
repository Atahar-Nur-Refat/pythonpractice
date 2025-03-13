#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")#If the item to remove does not exist, remove() will raise an error.
#also can be removed by using discard()
print(thisset)
#Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)(this will raise an error as the set has already been deleted