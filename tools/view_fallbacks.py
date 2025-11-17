"""
tools/view_fallbacks.py

This script provides a human-readable view of the fallback log.

# Coming soon!
"""

import json
from pathlib import Path

# Define the path to your fallback log file
LOG_FILE = Path("fallback_log.jsonl")

def load_fallback_log():
    """
    Load and parse the fallback log file.
    """
    try:
        with open(LOG_FILE, 'r') as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        print(f"Log file {LOG_FILE} not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from log file.")
        return []

def display_fallbacks(fallbacks, filter=None):
    """
    Display fallback log entries in a human-readable format.
    """
    for entry in fallbacks:
        if filter is None or filter(entry):
            print(json.dumps(entry, indent=4)))

def filter_by_confidence(fallbacks, min_confidence=0.5):
    """
    Filter fallbacks by minimum confidence score.
    """
    return [entry for entry in fallbacks if entry.get('confidence_score', 0) >= min_confidence]

if __name__ == "__main__":
    # Load fallback log entries
    fallbacks = load_fallback_log()

    # Display all fallbacks
    display_fallbacks(fallbacks)

    # Example usage: Display fallbacks with confidence score >= 0.7
    display_fallbacks(fallbacks, filter=filter_by_confidence)

# Usage
# To use this script, run it from the command line:
# python tools/view_fallbacks.py
