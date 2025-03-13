#in set the outut will be in unordered or will not be in serial
thisset = {"apple", "banana", "cherry", "apple"}
#in set duplicate values will be ignored
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False}
#True and are same so any one will be printed same for 0 and false
print(thisset)
#loop through sets and print value
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#Check if "banana" is present in the set or not :will print true or false

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

