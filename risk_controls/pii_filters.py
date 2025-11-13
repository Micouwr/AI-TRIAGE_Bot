import re

def contains_pii(text):
    patterns = [
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
        r"\b\d{16}\b",             # Credit Card
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  # Email
        r"\b\d{5}(?:-\d{4})?\b"    # ZIP
    ]
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False
