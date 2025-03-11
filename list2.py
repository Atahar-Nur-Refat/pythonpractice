thislist = ["apple", "banana", "cherry"]
thislist.append("orange")#used to add more item to the list in the end and only takes one item.for multiple use append again
print(thislist)

"""To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#will replace the given number item and shift the existing one to next
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)#adds element of another list to another in here thislist are added to tropical
print(tropical)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)#can also extend from tuples of sets
print(thislist)