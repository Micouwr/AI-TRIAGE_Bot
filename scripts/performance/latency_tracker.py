"""
latency_tracker.py

Measures and logs function latency with thresholds for performance governance.
Aligns with ISO/IEC 42001: Clause 6 (Risk Management), Clause 8 (Auditability).
"""

import time
import json
from functools import wraps
from pathlib import Path

LOG_FILE = Path("monitoring/pipeline_health.txt")

def _log(event):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")

def track_latency(name: str, warn_ms: int = 500, error_ms: int = 2000):
    """
    Decorator to measure latency and log with thresholds.
    - name: label for the function being tracked
    - warn_ms: latency threshold for warning (milliseconds)
    - error_ms: latency threshold for error (milliseconds)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                status = "ok"
                return result
            finally:
                elapsed_ms = int((time.time() - start) * 1000)
                if elapsed_ms >= error_ms:
                    status = "error"
                elif elapsed_ms >= warn_ms:
                    status = "warn"
                event = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "component": name,
                    "metric": "latency_ms",
                    "value": elapsed_ms,
                    "status": status,
                    "thresholds": {"warn_ms": warn_ms, "error_ms": error_ms}
                }
                _log(event)
        return wrapper
    return decorator

# Example usage
if __name__ == "__main__":
    @track_latency(name="classify_ticket", warn_ms=300, error_ms=1500)
    def classify_ticket():
        time.sleep(0.4)  # simulate work
        return {"type": "routing", "confidence": 0.82}

    classify_ticket()