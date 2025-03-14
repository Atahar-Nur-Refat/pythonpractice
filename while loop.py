#Print i as long as i is less than 6:

i = 1

while i <= 5:  # Runs while i is less than 6
    print("hello")
    print(i ,"\n")
    i += 1
#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1
  # doesnt print and Continue to the next iteration if i is 3:
print("\n")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print('\n')
#Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")#i value is increasing and at one case it will cross 6