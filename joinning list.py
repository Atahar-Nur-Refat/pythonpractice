list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)#normal joining method
#can also be joined using append and for
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list1:
  list2.append(x)

print(list2)
#also can be used extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
