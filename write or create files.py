f = open("demofile.txt", "a")
f.write("\n Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

# Open (or create) 'myfile.txt' in exclusive creation mode ('x')
# - Fails if file already exists
f = open("myfile.txt", "x")  # Creates a new empty file
f.close()                   # Always close the file after creation

# Open (or create) 'myfile.txt' in write mode ('w')
# - Creates the file if it doesn't exist
# - Overwrites content if it already exists
f = open("myfile.txt", "w")
f.close()                   # Close the file after opening
import os
os.remove("myfile.txt")
#check if exists or not
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")