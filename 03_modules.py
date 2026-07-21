"""
03_modules.py

Topics covered:
- Standard Library modules
- Custom modules
- __name__ == "__main__"
"""

import math

from utils import slugify

# --------------------------------------------
# Importing from a Custom Module
# --------------------------------------------

print(slugify("Hello World From Modules"))

print("-" * 40)

# --------------------------------------------
# Using the Standard Library
# --------------------------------------------

print(math.sqrt(16))

print("-" * 40)

# --------------------------------------------
# Script Entry Point
# --------------------------------------------

# This block only runs when the file
# is executed directly

if __name__ == "__main__":
    print("Running directly")