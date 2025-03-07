#first 3 will tell me true or false which is boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)
#this is more of a detailed version of boolean and condition

a = 300
b = 100
if a > b :
  print("a is greater than b")
else:
  print("a is not greater than b")
class myclass():
  def __len__(self):
    return 0 #if zero then it will output false and anytging other than zero it will be true

myobj = myclass()

print(bool(myobj))
#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

