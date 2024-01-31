# Dictionaries in Python. 
# Dictionaries are used to store data values in key:value pairs.
# Dictionaries are enclosed in curly brackets {}
# Dictionaries are mutable
# Dictionaries are iterable 
# Dictionaries are sequences of values
# example:
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)

# Accessing values:
# ---------------------------------
name = my_dict["name"]
age = my_dict["age"]
city = my_dict["city"]

print(name)  # Output: John
print(age)   # Output: 30
print(city)  # Output: New York

# built-in functions:
# 1. len() # returns the length of the dictionary
# 2. keys() # returns a list of the dictionary's keys
# 3. values() # returns a list of the dictionary's values
# 4. items() # returns a list of the dictionary's key-value pairs
# 5. get() # returns the value of the specified key
# 6. copy() # returns a copy of the dictionary
# 7. clear() # removes all the items from the dictionary
# 8. pop() # removes the item with the specified key
# 9. popitem() # removes the last item from the dictionary
# 10. update() # updates the dictionary with the specified key-value pairs

# 1. len():
my_dict = {"name": "John", "age": 30, "city": "New York"}
length = len(my_dict)

# 2. keys():    
my_dict = {"name": "John", "age": 30, "city": "New York"}
keys = my_dict.keys()

# 3. values():
my_dict = {"name": "John", "age": 30, "city": "New York"}
values = my_dict.values()

# 4. items():
my_dict = {"name": "John", "age": 30, "city": "New York"}
items = my_dict.items()

# 5. get():
my_dict = {"name": "John", "age": 30, "city": "New York"}
value = my_dict.get("name")

# 6. copy():
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict_copy = my_dict.copy()

# 7. clear():
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict.clear()

# 8. pop():
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict.pop("name")

# 9. popitem():
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict.popitem()

# 10. update():
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict.update({"name": "Jane", "age": 25})



