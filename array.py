# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Adds the elements of a list (or any iterable) to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the first item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
print(cars)
x = cars[0]
print(x)
cars[0]="Toyota"# 0 number index is modified
print(cars)
print("the length is ",len(cars))
for x in cars:
    print(x)
 #Add one more element to the cars array added to the last

cars.append("Honda")
print(cars)
cars.pop(2)#delete the 3rd element
print(cars)
#use remove for direct item name usage not index number
cars.remove("Toyota")
print(cars)
