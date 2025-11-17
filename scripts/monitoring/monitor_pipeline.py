"""
monitor_pipeline.py

A simple pipeline monitor for the AI Triage Bot Prototype aligned with ISO/IEC 42001 standards.
"""

import time
import logging
from functools import wraps

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class PipelineMonitor:
    def __init__(self):
        self.stage_results = []

    def log_stage_result(self, stage_name, status, details=""):
        self.stage_results.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "stage": stage_name,
            "status": status,
            "details": details
        })
        logging.info(f"Stage {stage_name} - {status}: {details}")

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
            print(f"{entry['timestamp']} | {entry['stage']} | {entry['status']}")
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

    @monitor.monitor_stage("load_data")
    def load_data():
        time.sleep(1)
        return {"data": [1, 2, 3]}

    @monitor.monitor_stage("process_data")
    def process_data():
        raise ValueError("Simulated processing error")

    @monitor.monitor_stage("save_results")
    def save_results():
        time.sleep(1)
        return True

    load_data()
    process_data()
    save_results()

    monitor.generate_summary()
    monitor.retry_failed_stages({
        "process_data": process_data
    })
