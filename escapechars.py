#You will get an error if you use double quotes or single quotes inside a string that is surrounded by double or single quotes:

# txt = "We are the so-called "Vikings" from the north."

#To fix this problem, use the escape character \":
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."#\ opened first so closed first and " opened last so close last.
print(txt)

"""putting r before the comments symbol means 
to read the comments as raw text so that nothing goes wrong for ide in reading comments doesnt confuse 
them with code"""
r"""\n → New Line (Moves to a new line) putting r before the comments symbol means
\t → Tab (Adds a tab space)
\\ → Backslash (Prints a backslash \)
\' → Single Quote (Useful inside single-quoted strings)
\r → Carriage Return (Moves the cursor to the beginning of the line)
\b → Backspace (Deletes one character before it)
\f → Form Feed (Not commonly used; moves to the next page in printers)
\ooo → Octal value (Represents a character in octal)
\xhh → Hex value (Represents a character in hexadecimal)"""
txt = "We are the so-called \"Vikings\" \\from\\ the north."#\ opened first so closed first and " opened last so close last.
print(txt)
