# risk_controls/pii_filters.py
import re

# Pre-compile regex patterns for efficiency. This avoids recompiling them on every call.
# Each entry pairs a PII type label with its pattern so detection and redaction
# stay consistent with each other.
PII_PATTERNS = [
    # Social Security Number (SSN) - US format
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),

    # Credit Card Number (16 digits, no formatting)
    ("card", re.compile(r"\b\d{16}\b")),

    # Credit Card Number (formatted with hyphens or spaces) - Fixed word boundary issue
    ("card", re.compile(r"\b(?:\d{4}[- ]){3}\d{4}(?=\s|[.,;!?]|$)")),

    # Email Address
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")),

    # Phone Number (matches various US formats)
    ("phone", re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")),
]

REDACTION_TOKENS = {
    "ssn": "[REDACTED_SSN]",
    "card": "[REDACTED_CARD]",
    "email": "[REDACTED_EMAIL]",
    "phone": "[REDACTED_PHONE]",
}

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
    return len(detect_pii_types(text)) > 0


def detect_pii_types(text: str) -> list:
    """
    Returns the sorted list of PII type labels found in the text, e.g. ["email", "ssn"].
    Credit card matches are validated with the Luhn algorithm, mirroring contains_pii.
    """
    if not isinstance(text, str) or not text:
        return []

    found = set()
    for label, pattern in PII_PATTERNS:
        for match in pattern.finditer(text):
            if label == "card" and not _luhn_check(match.group(0)):
                continue
            found.add(label)
    return sorted(found)


def redact_pii(text: str) -> str:
    """
    Replaces detected PII in the text with redaction tokens such as [REDACTED_SSN].
    Used before writing tickets to the fallback log so personal information is
    never stored in log files. Non-string input is returned unchanged.
    """
    if not isinstance(text, str):
        return text

    redacted = text
    for label, pattern in PII_PATTERNS:
        def _replace(match, label=label):
            if label == "card" and not _luhn_check(match.group(0)):
                return match.group(0)
            return REDACTION_TOKENS[label]
        redacted = pattern.sub(_replace, redacted)
    return redacted
