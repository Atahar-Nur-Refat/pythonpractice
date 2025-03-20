#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
x = lambda a,b,c,d,e,f, : a * b *c+d+e+f
print("the result is  ", x(2 ,3 ,4,5,6,7 ))

def myfunction(n):
    return lambda a : a * n
mydoubler=myfunction(2)
print("the result is now" ,mydoubler(11))
# use the same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)
mytripler = myfunc(4)

print("the result is now" ,mydoubler(11))
print("the result is now" ,mytripler(11))