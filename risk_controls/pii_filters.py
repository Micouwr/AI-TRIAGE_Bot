import re

def contains_pii(text):
    """
    Detects Personally Identifiable Information (PII) in the given text.

    Args:
        text (str): The text to search for PII.

    Returns:
        bool: True if PII is found, False otherwise.
    """
    patterns = [
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
        r"\b\d{16}\b",             # Credit Card
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  # Email
        r"\b\d{5}(?:-\d{4})?\b",    # ZIP
        r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}" # Phone Number
    ]
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False
