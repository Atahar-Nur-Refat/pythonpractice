#The re module offers a set of functions that allows us to search a string for a match:

# Function: findall
# Description:
# - Returns a list containing all matches found in the string.
# - Useful for finding all occurrences of a pattern.
# Example:
# matches = re.findall("a", "banana")
# print(matches)  # Output: ['a', 'a', 'a']

# Function: search
# Description:
# - Returns a Match object if there is a match anywhere in the string.
# - It only returns the first match found.
# Example:
# match = re.search("world", "Hello world!")
# print(match.group())  # Output: "world"

# Function: split
# Description:
# - Returns a list where the string has been split at each match of the pattern.
# - This is useful for splitting a string based on a pattern or delimiter.
# Example:
# result = re.split("\s", "Hello World!")  # Split by space
# print(result)  # Output: ['Hello', 'World!']

# Function: sub
# Description:
# - Replaces one or many matches with a string.
# - Useful for replacing occurrences of a pattern with another string.
# Example:
# new_string = re.sub("world", "everyone", "Hello world!")
# print(new_string)  # Output: "Hello everyone!"

# Character Description and Example

# []     : Set of characters       "[a-m]"
# \      : Special sequence or escape  "\d"
# .      : Any character (except newline)   "he..o"
# ^      : Starts with             "^hello"
# $      : Ends with               "planet$"
# *      : Zero or more occurrences "he.*o"
# +      : One or more occurrences  "he.+o"
# ?      : Zero or one occurrences "he.?o"
# {}     : Exact number of occurrences "he.{2}o"
# |      : Either or               "falls|stays"
# ()     : Capture and group

# Special Sequences
# \A     : Match at the beginning of string   "\AThe"
# \b     : Match at the beginning/end of a word  r"\bain", r"ain\b"
# \B     : Match not at the beginning/end of a word  r"\Bain", r"ain\B"
# \d     : Match digits (0-9)                    "\d"
# \D     : Match non-digits                     "\D"
# \s     : Match whitespace character           "\s"
# \S     : Match non-whitespace character      "\S"
# \w     : Match word characters (a-z, 0-9, _) "\w"
# \W     : Match non-word characters           "\W"
# \Z     : Match at the end of the string      "Spain\Z"

# Sets
# [arn]   : Match 'a', 'r', or 'n'             "[arn]"
# [a-n]   : Match letters between a and n      "[a-n]"
# [^arn]  : Match any character except 'a', 'r', 'n'  "[^arn]"
# [0123]  : Match digits 0, 1, 2, or 3         "[0123]"
# [0-9]   : Match digits 0 to 9                "[0-9]"
# [0-5][0-9] : Match two digits between 00 and 59  "[0-5][0-9]"
# [a-zA-Z] : Match any letter, lowercase or uppercase  "[a-zA-Z]"
# [+]     : Match the + character               "[+]"
