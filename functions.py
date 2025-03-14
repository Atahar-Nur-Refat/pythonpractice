def onemy_function():
  print("Hello from a function")#print thhis message when the function is called
onemy_function()
def twomyfunction(name):# here name is parameter inside the function
    print(name,"Nur")
twomyfunction('Atahar')#here Atahar is the argument which is passed to the defined function
#This function expects 2 arguments, and gets 2 arguments:
def threemyfunction(fname,lname):
    print(fname," ",lname)
threemyfunction("Atahar","Refat")#If you try to call the function with 1 or 3 arguments, you will get an error
threemyfunction("ANR","LASTONE")#must have to call the function with 2 arguments as ive declared two
print('\n')
def fourmyfunction(*kids):#have to add a asterisk if argument number is unsure
  print("The youngest child is " , kids[0])#if not any number is declared then all of the name will be printed

fourmyfunction("Emil", "Tobias", "Linus")
print('\n')
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter
def fivefunction(child3, child2, child1):
  print("The childs are" , child1 , child2, child3)
#basically it means serial or order doesnt matter
fivefunction(child3 = "Emil", child1 = "Tobias", child2 = "Linus")
print('\n')

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def sixfunction(**kid):
  print("His first and last name is " , kid["fname"], kid["lname"])

sixfunction(fname = "Tobias", lname = "Refsnes")

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def sevenfunction(country = "Bangladesh"):
  print("I am from " + country)

sevenfunction("Sweden")
sevenfunction("India")
sevenfunction()#called without argument so prints default value Bangladesh
sevenfunction("Brazil")
#You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
#if you send a List as an argument, it will still be a List when it reaches the function:
def eightfunction(food):
 for x in food:
  print(x)
fruits=["apple","banana","cherry"]
eightfunction(fruits)
#using return function
def ninefunction(x):
    return 5 * x#for return must use print
print(ninefunction(3))
print(ninefunction(4))
print(ninefunction(5))
#function definitions cannot be empty,
# but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
#only positional argument
#To specify that a function can have only positional arguments, add , / after the arguments:
def tenfunction(x, /):
  print(x)

tenfunction(3)#if i use keyword argument like x =20 in the called function it will be error but if i use x = something without the / then ok
#same way to get only keyword argument i need to use this below method and positional argument will give me error
# but if i use without the * then ok
def elevenfunction(*, x):
  print(x)
elevenfunction(x = 20)
#Combine Positional-Only and Keyword-Only
def twelvefunction(a, b, /, *, c, d):#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
  print(a + b + c + d)
twelvefunction(5, 6, c = 7, d = 8)
#recursion example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
