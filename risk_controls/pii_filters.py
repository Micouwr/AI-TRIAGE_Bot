import re

# Pre-compile regex patterns for efficiency. This avoids recompiling them on every call.
PII_PATTERNS = [
    # Social Security Number (SSN)
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),

    # Credit Card Number (13-16 digits, standalone number)
    re.compile(r"\b\d{13,16}\b"),

    # Credit Card Number (formatted in groups of 4)
    re.compile(r"\b(?:\d{4}[- ]){3}\d{4}\b"),

    # Email Address
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),

    # Phone Number (matches various US formats)
    re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
]

def contains_pii(text: str) -> bool:
    """
    Detects Personally Identifiable Information (PII) in the given text using pre-compiled regexes.

    Args:
        text (str): The text to search for PII.

    Returns:
        bool: True if any PII pattern is found, False otherwise.
    """
    if not isinstance(text, str):
        return False

    for pattern in PII_PATTERNS:
        if pattern.search(text):
            return True
    return False
