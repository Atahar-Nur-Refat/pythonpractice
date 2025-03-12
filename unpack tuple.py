fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #the process called unpacking

print(green)
print(yellow)
print(red)
#in case we add * in the last value
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits#the last variable will hold the rest

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits   # green = 'apple' → First element
                                 # red = 'cherry' → Last element
                                 # *tropic = ['mango', 'papaya', 'pineapple'] → All elements between first and last go into tropic as a list.
print(green)
print(tropic)
print(red)
