"""
utils.py

A simple helper module used by
03_modules.py.
"""

def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    return text.lower().replace(" ", "-")