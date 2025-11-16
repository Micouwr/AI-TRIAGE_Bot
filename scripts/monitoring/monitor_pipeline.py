"""
monitor_pipeline.py

Governance-aligned pipeline monitor for AI Triage Bot.
Supports ISO/IEC 42001 Clause 5 (Accountability), Clause 6 (Risk Management), and Clause 8 (Auditability).
"""

import time
import logging
from functools import wraps
from pathlib import Path
import json

# Setup audit-friendly logging
LOG_FILE = Path("logs/monitoring.jsonl")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Configure logger to write JSONL
handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter('{"timestamp": "%(asctime)s", "stage": "%(stage)s", "status": "%(status)s", "details": "%(message)s"}')
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class PipelineMonitor:
    def __init__(self):
        self.stage_results = []

    def log_stage_result(self, stage_name, status, details=""):
        entry = {
            "stage": stage_name,
            "status": status,
            "details": details
        }
        self.stage_results.append(entry)
        logger.info(details, extra={"stage": stage_name, "status": status})

    def monitor_stage(self, stage_name):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    self.log_stage_result(stage_name, "success")
                    return result
                except Exception as e:
                    self.log_stage_result(stage_name, "failure", str(e))
                    return None
            return wrapper
        return decorator

    def generate_summary(self):
        print("\n--- Pipeline Summary ---")
        for entry in self.stage_results:
            print(f"{entry['stage']} | {entry['status']}")
        print("--- End Summary ---\n")

    def retry_failed_stages(self, stage_map):
        for entry in self.stage_results:
            if entry["status"] == "failure":
                stage_name = entry["stage"]
                if stage_name in stage_map:
                    print(f"Retrying stage: {stage_name}")
                    try:
                        stage_map[stage_name]()
                        self.log_stage_result(stage_name, "retry_success")
                    except Exception as e:
                        self.log_stage_result(stage_name, "retry_failure", str(e))

# Example usage
if __name__ == "__main__":
    monitor = PipelineMonitor()

    @monitor.monitor_stage("example_task")
    def example_task(should_fail=False):
        if should_fail:
            raise ValueError("This is a simulated failure.")
        return "Success"

    example_task()
    example_task(should_fail=True)
    monitor.generate_summary()