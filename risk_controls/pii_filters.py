# risk_controls/pii_filters.py
import re

# Pre-compile regex patterns for efficiency. This avoids recompiling them on every call.
PII_PATTERNS = [
    # Social Security Number (SSN) - US format
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    
    # Credit Card Number (16 digits, no formatting)
    re.compile(r"\b\d{16}\b"),
    
    # Credit Card Number (formatted with hyphens or spaces) - Fixed word boundary issue
    re.compile(r"\b(?:\d{4}[- ]){3}\d{4}(?=\s|[.,;!?]|$)"),
    
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
    
    Supports ISO/IEC 42001:2023 Clause 6.1 (Risk Management - data protection).
    
    Args:
        text (str): The text to search for PII.
    
    Returns:
        bool: True if any PII pattern is found, False otherwise.
    """
    if not isinstance(text, str):
        return False
    
    # Check for SSN, emails, and phone numbers (indices 0, 3, 4)
    for i in [0, 3, 4]:
        if PII_PATTERNS[i].search(text):
            return True
    
    # Check for credit cards (indices 1, 2) with Luhn validation
    for i in [1, 2]:
        match = PII_PATTERNS[i].search(text)
        if match and _luhn_check(match.group(0)):
            return True
    
    return False
