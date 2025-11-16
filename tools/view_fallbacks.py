# tools/view_fallbacks.py
import json

def view_fallback_log():
    """
    Reads and displays the fallback log in a human-readable format.
    """
    try:
        with open("fallback_log.json", "r") as f:
            for line in f:
                try:
                    log_entry = json.loads(line)
                    print("-" * 20)
                    print(f"Timestamp: {log_entry.get('timestamp')}")
                    print(f"Ticket: {log_entry.get('ticket')}")
                    print("Result:")
                    result = log_entry.get('result', {})
                    for key, value in result.items():
                        print(f"  {key}: {value}")
                    print("-" * 20)
                    print()
                except json.JSONDecodeError:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print("Fallback log not found. No fallbacks have been logged yet.")

if __name__ == "__main__":
    view_fallback_log()
