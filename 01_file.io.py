"""
01_file_io.py

Topics covered:
- Reading a text file
- Writing to a text file
- Reading JSON files
- Reading CSV files
"""

import csv
import json

# --------------------------------------------
# Reading a Text File
# --------------------------------------------

with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents.splitlines())

print("-" * 40)

# --------------------------------------------
# Writing to a File
# --------------------------------------------

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.writelines([
        "Second line\n",
        "Third line\n"
    ])

print("File written successfully")

print("-" * 40)

# --------------------------------------------
# Reading JSON
# --------------------------------------------

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

print(data)

print("-" * 40)

# --------------------------------------------
# Reading CSV
# --------------------------------------------

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)