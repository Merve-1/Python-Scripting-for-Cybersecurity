"""
02_exceptions.py

Topics covered:
- try
- except
- else
- finally
- raise
"""

# --------------------------------------------
# Handling Exceptions
# --------------------------------------------

try:
    value = int(input("Enter a number: "))
    result = 100 / value

except ValueError:
    print("That wasn't a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print(f"Result: {result}")

finally:
    print("Program finished")

print("-" * 40)

# --------------------------------------------
# Raising Your Own Exception
# --------------------------------------------

def set_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be negative")

set_age(20)