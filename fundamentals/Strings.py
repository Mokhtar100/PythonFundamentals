# Strings in Python
# Strings are used to store text
# Strings are surrounded by single or double quotation marks
# Strings are immutable
# Strings are case sensitive
# Strings are indexed starting from 0
# Strings are ordered
# Strings are iterable
# Strings are sequences of characters
# example:
my_string = "Hello, World!"
print(my_string)

# Strings are immutable:
# my_string = "Hello, World!"
# my_string[0] = "H"  # TypeError: 'str' object does not support item assignment

# Strings are ordered:
# my_string[0]  # 'H'

# Strings are iterable:
# for char in my_string:
#     print(char)

# Strings are sequences of characters:
# len(my_string)  # 13  # length of the string
# ----------------------------------------------------

# built-in functions:
# len() # returns the length of the string
# str() # returns the string representation of the object
# repr() # returns the string representation of the object
# print() # prints the string
# capatilize() # capitalizes the first character of the string
# lower() # converts the string to lowercase
# upper() # converts the string to uppercase
# title() # converts the first character of each word to uppercase
# swapcase() # swaps the case of the string
# count() # returns the number of occurrences of a substring in the string
# find() # returns the index of the first occurrence of a substring in the string
# rfind() # returns the index of the last occurrence of a substring in the string   
# index() # returns the index of the first occurrence of a substring in the string
# rindex() # returns the index of the last occurrence of a substring in the string
# startswith() # returns True if the string starts with the specified prefix
# endswith() # returns True if the string ends with the specified suffix
# split() # splits the string into a list of substrings
# join() # joins the elements of an iterable into a string
# replace() # replaces all occurrences of a substring with another substring
# strip() # removes leading and trailing whitespaces from the string
# --------------------------------------------------
# example:
my_string = "Hello, World!"

# length of the string:
length = len(my_string)
print(length)

# str():
my_string = "Hello, World!"
my_string = str(my_string)

# repr():
my_string = "Hello, World!"
my_string = repr(my_string)

# capitalize():
my_string = "hello, world!"
my_string = my_string.capitalize()

# lower():
my_string = "HELLO, WORLD!"
my_string = my_string.lower()

# upper():
my_string = "hello, world!"
my_string = my_string.upper()

# title():
my_string = "hello, world!"
my_string = my_string.title()

# swapcase():
my_string = "Hello, World!"
my_string = my_string.swapcase()

# count():
my_string = "Hello, World!"
my_string = my_string.count("l")

# find():
my_string = "Hello, World!"
my_string = my_string.find("l")

# rfind():
my_string = "Hello, World!"
my_string = my_string.rfind("l")

# index():
my_string = "Hello, World!"
my_string = my_string.index("l")

# rindex():
my_string = "Hello, World!"
my_string = my_string.rindex("l")

# startswith():
my_string = "Hello, World!"
my_string = my_string.startswith("H")

# endswith():
my_string = "Hello, World!"
my_string = my_string.endswith("World!")

# split():
my_string = "Hello, World!"
my_string = my_string.split(",")

# join():
my_string = "Hello"
my_string = "".join(my_string)

# replace():
my_string = "Hello, World!"
my_string = my_string.replace("World", "Universe")

# strip():
my_string = "   Hello, World!   "
my_string = my_string.strip()


