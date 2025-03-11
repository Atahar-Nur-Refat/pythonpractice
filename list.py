#list has 0th indexing system
thislist = ["apple , bana ,a jkdasl ,a, ask ,as,ask"]
print("The list length is ",len(thislist),"and the items are "    +str(thislist))
mylist = ["apple", "banana", "cherry"]
print(type(mylist))#datatype of list which is defined as objects with the data type 'list'
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1,list2,list3) #List items can be of any data type Such as string, int and boolean data types


#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#Use [] for regular list creation.
# Use list() when you need to convert tuples, sets, strings, or other iterables into a list.
# Converting a tuple to a list
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
print(mylist)  # ['apple', 'banana', 'cherry']

# Converting a string to a list (each letter becomes an element)
word = "hello"
char_list = list(word)
print(char_list)  # ['h', 'e', 'l', 'l', 'o']
#changing and accessing specific list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#Return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["x", "y"]#Change the values "banana" and "cherry" with the values x and y
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = [1, 2, 3, 4, 5]
thislist[1:4] = [10, 20]
print(thislist)
thislist = [1, 2, 3, 4, 5]
thislist[1:4] = [10, 20, 30, 40]  # More elements than original slice
print(thislist)#expandng the list
#Shrinking the List
thislist = [1, 2, 3, 4, 5]
thislist[1:4] = [10]  # Fewer elements than original slice
print(thislist)

