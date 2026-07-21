# ============================================
# Python Basics => 01_Hello Branch 
# ============================================


# --------------------------------------------
# Printing
# --------------------------------------------
print("Hello, world!")
print("-" * 40)

# --------------------------------------------
# Variables & Data Types
# --------------------------------------------
name = "Ada"                 # str
age = 42                     # int
height = 1.7                 # float
is_active = True             # bool

values_list = [1, 2, 3]      # list (mutable, ordered)
values_tuple = (1, 2, 3)     # tuple (immutable, ordered)
values_dict = {"a": 1}       # dictionary (key-value pairs)
values_set = {1, 2, 3}       # set (unique, unordered)

# --------------------------------------------
# Formatted Strings (f-strings)
# --------------------------------------------
print(f"{name} is {age} years old.")
print("-" * 40)

# --------------------------------------------
# Multiple Assignment & Swapping
# --------------------------------------------
x, y = 1, 2

# Swap values
x, y = y, x

# --------------------------------------------
# Conditional Statements (if / elif / else)
# --------------------------------------------
score = 65

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)
print("-" * 40)

# --------------------------------------------
# Match Statement (Python 3.10+)
# Best for matching exact values
# --------------------------------------------
day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Almost weekend")
    case _:
        print("Another day")
print("-" * 40)

# Match with guards (possible, but if/elif is clearer)
match score:
    case _ if score >= 90:
        grade = "A"
    case _ if score >= 80:
        grade = "B"
    case _:
        grade = "C"

# --------------------------------------------
# For Loops
# --------------------------------------------

# Loop over a range
for i in range(5):
    print(i)      # 0, 1, 2, 3, 4
print("-" * 40)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)      # 0, 2, 4, 6, 8
print("-" * 40)

# Loop through a collection
for item in ["a", "b", "c"]:
    print(item)
print("-" * 40)

# --------------------------------------------
# While Loop
# --------------------------------------------
n = 0

while n < 3:
    print(n)
    n += 1
print("-" * 40)

# --------------------------------------------
# List Comprehensions
# --------------------------------------------

# Squares
squares = [x**2 for x in range(10)]

# Equivalent loop:
"""
squares = []

for x in range(10):
    squares.append(x**2)
"""

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Equivalent loop:
"""
evens = []

for x in range(20):
    if x % 2 == 0:
        evens.append(x)
"""

# --------------------------------------------
# Functions
# --------------------------------------------

# Function with type hints and a default parameter
def greet(name: str, excited: bool = False) -> str:
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"

print(greet("Ada"))
print(greet("Grace", excited=True))

print("-" * 40)

# *args and **kwargs
def total(*numbers: int, **options) -> int:
    result = sum(numbers)

    if options.get("double"):
        result *= 2

    return result

print(total(1, 2, 3))
print(total(1, 2, 3, double=True))

print("-" * 40)

# Lambda (anonymous function)
square = lambda x: x * x

print(square(5))

# Equivalent function:
"""
def square(x):
    return x * x
"""

print("-" * 40)

# --------------------------------------------
# Data Structures
# --------------------------------------------

# list  -> ordered, mutable, duplicates allowed
# tuple -> ordered, immutable
# dict  -> key-value mapping
# set   -> unordered, unique values

user = {
    "name": "Ada",
    "age": 36,
    "langs": ["Python", "JavaScript"],
}

# Add a new key
user["email"] = "ada@example.com"

# Safe lookup with a default value
print(user.get("phone", "N/A"))

print("-" * 40)

# Iterate over key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

print("-" * 40)

# Dictionary comprehension
lengths = {
    key: len(str(value))
    for key, value in user.items()
}

print(lengths)

#Why langs is 24 
"""
len() counts every character in that string, including:
[
]
quotes '
comma ,
spaces
the letters in "Python"
the letters in "JavaScript"
"""