# for with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Using the range() function:

for x in range(6):#follows 0 indexing by default
  print(x)
print('\n')
#Using the start parameter:

for x in range(2, 6):

  print(x)
  print('\n')
#The range() function defaults to increment the sequence by 1
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):#start from 2 and stops at 29 as max limit is 30 and increase by  3
  print(x)
#Print all numbers from 0 to 5, and print a message when the loop has ended:
print('\n')
for x in range(6):
  print(x)
else:

  print("Finally finished!")
  print('\n')
 #nested loop Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)#here first red printed then the inner most loop circulates then the less inner loop then the less and it continues
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass