#A variable created inside a function is available inside that function:

def myfunc():
  x = 300 #example of a local scope
  print(x)

myfunc()
#The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
#global variable A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope (inside the function):
#The function will print the local x, and then the code will print the global x:

x = 300#global variable

def myfunc():
  x = 200#local variable
  print(x)

myfunc()

print(x)