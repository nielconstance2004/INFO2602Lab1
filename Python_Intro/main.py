# PYTHON SYNTAX 1

# Initialization and assignment
x = 10  # Initialization
x = 23  # Assignment
y #declaration
z = (x + y) / x + (78 % 3)  # Usual mathematical operations supported

name = "bobby"  # string
age = 12  # integer
height = 6.5  # float
hasDate = False  # boolean
comp = 7j  # complex

# Using f-strings for interpolation
print(f"Name: {name}, Age: {age}, Height: {height}, Has Date: {hasDate}, Complex: {comp}")

# Reading input
name = input("Enter name: ")
print(name)

# Type casting to convert types
intHeight = int(height)  # 6
strHeight = str(height)  # '6.5'
floatHeight = float(intHeight)  # 6.0
ageType = type(age)
print(f"intHeight: {intHeight}, strHeight: {strHeight}, floatHeight: {floatHeight}, ageType: {ageType}")

# Correct if-else structure
if 3 > 5:
    print("more")
else:
    print("less")

# Single-line if-else (correct usage)
if 3 > 5:
    print("more")
else:
    print("less")

# elif === else if
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70:
    print("A")
elif mark > 60:
    print("B")
elif mark > 50:
    print("C")
else:
    print("F")

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("This is run when the loop condition is no longer met")

# Iterating an iterable such as a list
names_list = ["bob", "sally", "john"]
for j in names_list:
    print(j)

# Iterating between custom range and increment
for i in range(0, 10, 2):
    print(i)

# Basic function
def add(a, b):
    return a + b

def printPerson(name, age, height):
    print(name, age, height)

# You can specify arguments in any order if they are named
printPerson(age=12, name='bob', height=5)

# Default arguments are used when they are not given in the function call
def sayHello(fname, lname='Smith'):
    print('Hello ' + fname + ' ' + lname)

sayHello('John')
sayHello('Bill', 'Young')

# PYTHON SYNTAX 2

items_list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(items_list)
# Negative indexing can access elements starting from the end
print(list2[-1])

# Select a subset of a list
print(list2[2:4])

# Gets the length of a list
print(len(list2))

# Add items to list
items_list.append('item4')

# Remove item from list
item4 = items_list.pop()

# Copy list
list3 = list2.copy()

# List comprehension, lets you create new lists from existing lists
num = [1, 2, 3, 4]
doubled = [n * 2 for n in num]
print(doubled)  # [2, 4, 6, 8]
odd = [n for n in num if n % 2 == 1]
print(odd)  # [1, 3]

# Unpacking a list, lets you create variables from items in the list
num = [1, 2, 3, 4]
first, second, *rest = num
print(first)
print(second)
print(rest)

# Joining lists
num2 = [5, 6]
num3 = num + num2
print(num3)  # [1, 2, 3, 4, 5, 6]

# Copying lists
num4 = num2.copy()

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple[0])  # 'apple'

data = [20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
    myset.add(num)

print(myset)  # {0, 1, 2, 3, 32, 42, 10, 20}
num_unique = len(myset)

mydict = {
    "name": "bob",
    "age": 34
}

print(mydict)

# Accessing a key
print(mydict['age'])

# Adding a new key and value
mydict['height'] = 7

# Iterating keys
for key in mydict:
    print(key)

# Iterating values
for key in mydict:
    print(mydict[key])

# Check for a key
if 'weight' in mydict:
    print(mydict['weight'])
else:
    print('no weight property!')

# Parent class
class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def sayHello(self):
        print("Hello! I'm a person, my name is", self.name)

# Child class inherits from Person
class Student(Person):

    # super() is the reference to the parent class Person so
    # we call Person's constructor here to set the Person
    # properties of the student instance
    def __init__(self, stid, name, height, weight):
        super().__init__(name, height, weight)
        self.stid = stid

    # Override method of parent
    def sayHello(self):
        print("Hello! I'm a student, my name is", self.name)

bob = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello()
sally.sayHello()

print(bob.name)
