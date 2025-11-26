# risk_controls/pii_filters.py
import re

# Pre-compile regex patterns for efficiency. This avoids recompiling them on every call.
PII_PATTERNS = [
    # Social Security Number (SSN) - US format
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    
    # Credit Card Number (formatted in groups of 4) - More specific to avoid false positives
    re.compile(r"\b(?:\d{4}[- ]){3}\d{4}\b"),
    
    # Email Address
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
    
    # Phone Number (matches various US formats)
    re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"),
]

# Secondary validation: Credit card Luhn algorithm check
def _luhn_check(card_number: str) -> bool:
    """
    Validates a credit card number using the Luhn algorithm.
    Reduces false positives from random 13-16 digit sequences.
    """
    # Remove spaces and hyphens
    digits = [int(d) for d in card_number if d.isdigit()]
    
    if len(digits) < 13 or len(digits) > 19:
        return False
    
    # Luhn algorithm
    checksum = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0


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
    
    # Check for SSN, formatted credit cards, emails, and phone numbers
    for i, pattern in enumerate(PII_PATTERNS):
        match = pattern.search(text)
        if match:
            # For credit card patterns (index 1), validate with Luhn algorithm
            if i == 1:
                if _luhn_check(match.group(0)):
                    return True
                # If Luhn fails, continue checking other patterns
            else:
                return True
    
    return False
