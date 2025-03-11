thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")#If there are more than one item with the specified value, the remove() method removes the first occurrence
print(thislist)
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#del keyword also does the same
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#can also delete whole list
thislist = ["apple", "banana", "cherry"]
del thislist
#clear empties the whole list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
