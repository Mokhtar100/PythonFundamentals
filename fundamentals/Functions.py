# Functions in Python
# Functions are used to perform specific tasks
# Functions are defined using the-->(def) keyword
# example:
def greet(): 
    print("Hello") 
greet() #calling the function
# ------------------------------------------------

#Functions can have parameters
def greet(name): 
    print("Hello " + name) 
greet("John")
# ------------------------------------------------

#Functions can have multiple parameters 
def greet(name, age): 
    print("Hello " + name + ", you are " + age) 
greet("John", "36")

def max(num1, num2, num3): 
    if (num1 >= num2) and (num1 >= num3): 
        largest = num1 
    elif (num2 >= num1) and (num2 >= num3): 
        largest = num2 
    else: 
        largest = num3 
    return largest

a=input()
b=input()
c=input()
print(max(a, b, c))
# -----------------------------------------------------------------

# formal of arguments
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable-Length Arguments

# 1.Positional Arguments
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8
# ------------------------------------------------

# 2.Keyword Arguments
def multiply(a, b):
    return a * b

result = multiply(a=4, b=2)
print(result)  # Output: 8
# ------------------------------------------------
# 3.Default Arguments
def power(base, exponent=2):
    return base ** exponent

result = power(3)
print(result)  # Output: 9

result = power(2, 3)
print(result)  # Output: 8
# -----------------------------------------------
# 4.Variable-Length Arguments
# *args and **kwargs
def sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum(1, 2, 3, 4, 5)
print(result)  # Output: 15
# ------------------------------------------------

# Anonymous Functions
# lambda function
double = lambda x: x * 2
result = double(5)
print(result)  # Output: 10

# ------------------------------------------------

# Recursion
# A function that calls itself

def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

# ------------------------------------------------

# Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # 5! = 5 * 4 * 3 * 2 * 1 # Output: 120 # 5*4*3*2*1

