"""
04_cli.py

Demonstrates building a simple command-line
application using argparse.
"""

import argparse

# --------------------------------------------
# Create the Argument Parser
# --------------------------------------------

parser = argparse.ArgumentParser(
    description="Resize an image."
)

# Required positional argument
parser.add_argument(
    "path",
    help="Path to the image."
)

# Optional argument
parser.add_argument(
    "--width",
    type=int,
    default=800,
    help="New width."
)

# Boolean flag
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Display extra information."
)

args = parser.parse_args()

# --------------------------------------------
# Display Parsed Arguments
# --------------------------------------------

if args.verbose:
    print(f"Resizing {args.path} to width {args.width}")