# There are 5 types of operators in python:
    # 1. Arithmetic operators
    # 2. Assignment operators
    # 3. Comparison operators
    # 4.Logical operators
    # 5. Identity operators

# 1. Arithmetic operators: + , - , * , / , % , ** , //
# example:
print(10 + 10)   # = 20
print(10 - 10)   # = 0
print(10 * 10)   # = 100
print(10 / 10)   # = 1.0
print(10 % 10)   # = 0
print(10 ** 10)  # = 10,000,000,000  => 10^10
print(10 // 10)  # = 1 => floor(10/10)
  
#####################################################

# 2. Assignment operators: =
# example:
a = 10
print(a) # = 10

######################################################

# 3. Comparison operators: == , != , > , < , >= , <=
# example:
print(10 == 10)  # = True
print(10 != 10)  # = False
print(10 > 10)   # = False
print(10 < 10)   # = False
print(10 >= 10)  # = True
print(10 <= 10)  # = True

#####################################################

# 4. Logical operators: and, or, not
a = True
b = False

# and operator
result = a and b
print(result)  # False

# or operator
result = a or b
print(result)  # True

# not operator
result = not a
print(result)  # False

###############################################

# 5. Identity operators: is, is not
# Identity operators: is, is not
a = 20
b = 10

# is operator
result = a is b
print(result)  # True

# is not operator
result = a is not b
print(result)  # False

#################################################

# Note: is operator and is not operator are used to compare the identity of two variables
# Note: == operator and != operator are used to compare the values of two variables

#################################################
# operator precedence:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. == != > < >= <=
# 6. and
# 7. or
# 8. not

#example:
(4+2**2)/2+(4*3+6/2) #==>19
# 1---->(4+4)/2+(12+3)
# 2---->8/2+15
# 3---->4+15
# 4---->19