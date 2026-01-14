"""
Project: CSV Data Integration
Identity: Shadow Specialist
Goal: Learning to store tabular data (Prerequisite for AI Data Analysis).
"""

import csv
import os

def main():
    # File check to add headers only if file is new
    file_exists = os.path.isfile("daily_metrics.csv")

    # Data to log (Simulating your lifestyle algorithm)
    entry = {
        "date": "2026-01-14",
        "deep_work_hours": 3.5,
        "gym_status": "Success",
        "logic_mastery": "Day 10: CSV Handling"
    }

    try:
        with open("daily_metrics.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=entry.keys())
            
            if not file_exists:
                writer.writeheader()  # Professional touch: adding column names
            
            writer.writerow(entry)
        print("Metric Logged: daily_metrics.csv updated.")
    except Exception as e:
        print(f"I/O Error: {e}")

if __name__ == "__main__":
    main()
