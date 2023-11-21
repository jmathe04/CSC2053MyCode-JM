print("hello world!")

# this is a comment

'''
This is a line
This is another line
'''

x = 10
print(x)
y = 10.5
x = "hello"
print(x)

# math operators
x = 100
y = 10
result = x//y # FLOOR division
result = int(x/y)
print(result)

# built in functions
min_val = min(10,1)
print(min_val)
raised = pow(2,4)
raised = 2**4 #two the power of 4 instead of carrot
print(raised)

# if statements
if x < 10:
    x+=10
    y=15
print("this will execute outside of if statment")

if x < 0:
    x += 1
elif x > 0:
    x -= 1
else:
    x=100

if x < 0 and y < 0:
    x += 1

    y +=1

if x < 0 or y < 0:
    x += 1
    y += 1

# loops

count=0

while count < 10:
    count += 1
    print(count)

alist = [1,2,3,4,5]
for value in alist:
    print(value, end = " ")


for i in range(0, len(alist), 1):
    print("i is", i, "and the value is", alist[i])

for i in range(len(alist)- 1, -1):
    print("i is", i, "and the value is", alist[i])

for i, val in enumerate(alist):
    print("i is", i, "and value is", val)

# functions

def add_numbers(x,y):
    return x + y

def say_hello(name = "friend"):
    print("hello", name)

say_hello("Bob")
result = add_numbers(2,4)
print(result)
say_hello()

# Strings

fname = "Jeremiah"
lname = "Mathew"
full_name = (fname + " " + lname)
print(full_name)

f_initial = fname[0]
print(f_initial)
last_char = lname[-1]
print(last_char)

# String Slicing

course  = "Platform Computing"
platform = course[0:8]
computing = course[9:18]
print(platform,computing)