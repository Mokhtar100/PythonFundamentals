#Conditions in Python are used to make decisions in the program.
#If statement is used to make decisions in the program.

#simple if statement:
a=10
b=20
if(a>b):
    print("a is greater than b")


#################################################

#If-else statement:
c=10
d=20
if(c>d):
    print("c is greater than d")
else:
    print("d is greater than c")

#############################################

#if-elif-else statement:    
e=10
f=20
if(e==f):
    print("e and f are equal")
elif(f>e):
    print("f is greater than e")
else:
    print("e is greater than f")

################################################

#Nested if-else statement:
g=10
h=20
if(g>h):
    if(g==h):
        print("g and h are equal")
    else:
        print("g is greater than h")
else:
    print("h is greater than g")

#############################################
    
 #Logical operators in conditions:
 #and operator
i=10
j=20
k=30
l=40
if(i<j and j<k and k<l):
    print("All conditions are true")

#or operator
m=10
n=20
o=30
p=40
if(m<n or n<o or o<p):
    print("At least one condition is true")

#not operator
r=10
q=20
if(not(q<r)):
    print("q is less than r")

###############################################
    #if all: ---> returns true if all the conditions are true
s=10
t=20
u=30
v=40
if all([ s==10,t==20,u==30,v==40]):
    print("All conditions are true")

    #if any: ---> returns true if any of the conditions are true
w=10
x=20
y=30
z=40
if any([w==10,x==21,y==90,z==200]):
    print("At least one condition is true")


      
