thislist = ["orange", "mango", "kiwi", "pineapple", "banana","Zango"]
thislist.sort()#sort() method that will sort the list alphanumerically, ascending, by default:
print(thislist)#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#if you want a case-insensitive sort function, use str.lower as a key function
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)#To sort descending, use the keyword argument reverse = True:
print(thislist)
#also same for numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)#means it will provide output from opposite direction