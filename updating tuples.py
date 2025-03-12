#tuples cant be altered so it needs to be converted into list to do that
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#for adding items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
#adding one tuple to another tuple
thistuple = ("apple", "banana", "cherry")
y = ("grape",)#has to use a comma to make it more than one item
thistuple += y #z=thistuple+y
               #print(z) also can be done by this
print(thistuple)
#same way remove and deletion not possible we need to convert to list first
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
