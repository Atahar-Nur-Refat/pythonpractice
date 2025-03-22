import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match! The line is :",x.group())
else:
  print("No match")

#finds how many times ai is in the line and prints it that many times
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found:
import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#using re.search which prints the location od first space with 0th indexing
txt = "The rain in Spain"
x = re.search(r"\s", txt)  # Use raw string to avoid warning

print("The first white-space character is located in position:", x.start())
#if no matches found then it will print none
txt = "TheraininSpain"
x = re.search(r"\s", txt)#no match example
print(x)

txt = "The rain in Spain"
x = re.search("Portugal", txt)#no match example
print(x)
#Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)
#Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)#only split after the the first white space
print(x)
# the sub() function replaces all the empty space if i use with my chosen word
txt = "The rain in Spain"
x = re.sub(r"\s", " 5 ", txt)
print(x)
#Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())#span shows the position of the s in 0th indexing which is 12 and 16 is the number where word spain ends
#and output shows 17 because its the number after finally ending of the whole word
print(x.string) #used to Print the string passed into the function which means
# it will print everything that is before Word spain as we searched for the word S which is at Spain
print(x.group())#prints the first word with Capital S in the words. if nothing found it will print none