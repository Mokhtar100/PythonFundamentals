# LOOPs Types:
#-------------------
# 1. For loop
for i in range(5):
    print(i)
#-------------------
# 2. While loop
count = 0
while count < 5:
    print(count)
    count += 1
#-------------------
# 3. Nested loop
for i in range(3):
    for j in range(3):
        print(i, j)
#-------------------
x=0
while x<5:
    y=0
    while y<3:
        print(x,y)
        y+=1
    x+=1                
#-------------------
# 4. Break statement
for i in range(5):
    if i == 3:
        break
    print(i)
#-------------------
# 5. Continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)
#-------------------
# 6. Pass statement
for i in range(5):
    if i == 3:
        pass
    print(i)
#-------------------
# 7. infinite loop
while True:
    print("Hello")
#-------------------
# 8. while with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % (count)) 
