# Lists in Python
# Lists are used to store multiple items in a single variable
# Lists are ordered, changeable, and allow duplicate values
# Lists are enclosed in square brackets []
# Lists are mutable
# Lists are iterable
# Lists are sequences of values
# example:
my_list = [1, 2, 3, 4, 5]
print(my_list)

# built-in functions:
# 1. len() # returns the length of the list
# 2. append() # adds an item to the end of the list
# 3. extend() # adds multiple items to the end of the list
# 4. insert() # adds an item at a specified index
# 5. remove() # removes the first item with the specified value
# 6. pop() # removes the item at the specified index
# 7. clear() # removes all the items from the list
# 8. index() # returns the index of the first occurrence of the specified value
# 9. count() # returns the number of occurrences of the specified value
# 10. reverse() # reverses the order of the list
# 11. sort() # sorts the list
# 12. copy() # returns a copy of the list

# 1. len():
my_list = [1, 2, 3, 4, 5]
length = len(my_list)

# 2. append():
my_list = [1, 2, 3, 4, 5]
my_list.append(6)

# 3. extend():
my_list = [1, 2, 3, 4, 5]
my_list.extend([6, 7, 8])

# 4. insert():
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)

# 5. remove():
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)

# 6. pop():
my_list = [1, 2, 3, 4, 5]
my_list.pop()

# 7. clear():
my_list = [1, 2, 3, 4, 5]
my_list.clear()

# 8. index():
my_list = [1, 2, 3, 4, 5]
my_list.index(3)

# 9. count():
my_list = [1, 2, 3, 4, 5]
my_list.count(3)

# 10. reverse():
my_list = [1, 2, 3, 4, 5]
my_list.reverse()

# 11. sort():
my_list = [132, 122, 322, 41, 52]
my_list.sort()

# 12. copy():   
my_list = [1, 2, 3, 4, 5]
my_list_copy = my_list.copy()


