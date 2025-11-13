# tests/test_router.py

from bot_engine.router import classify_ticket
import json

def run_tests():
    test_cases = [
        "Please reset my password ASAP.",
        "Can you explain this invoice?",
        "My ZIP is 40202 and my SSN is 123-45-6789.",
        "I need help with something."
    ]

    for i, text in enumerate(test_cases, 1):
        result = classify_ticket(text)
        print(f"\nTest Case {i}:")
        print(f"Input: {text}")
        print(f"Output: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    run_tests()
