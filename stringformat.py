
"""cant combine string and number together
like this
we need to use another format for this
the code below is wrong
age = 36
txt = "My name is John, I am " + age
print(txt)
But we can combine strings and numbers by using f-strings or the format() method!"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)

"""To specify a string as an f-string, 
simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations."""

# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 53} dollars"#2nd bracket here is called placeholder it should be used
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" #Display the price with 2 decimals(variable name:.a number and f for float)
print(txt)