r"""List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:"""
fruits = ["apple","banana","cherry"]
newlist=[]
for x in fruits:
    if "a" in x:#only executes the one with a in it
       newlist.append(x)
print(newlist)
#With list comprehension you can do all that with only one line of code:

fruits=["apple","banana","cherry"]
newlist=[x for x in fruits if "a" in x ]
print(newlist)
newlist = [x for x in fruits if x != "apple"]#only accepts that are not apple
print(newlist)
newlist = [x for x in range(5)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)