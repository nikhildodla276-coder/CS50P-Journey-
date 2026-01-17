"""
Project: Secure Memory Vault (Error Handling)
Identity: Shadow Specialist
Goal: Day 13 of 348 - Building Unbreakable Data Pipelines
"""
import json
import os

def load_agent_data(filename):
    # Defensive Check: Does the file even exist in the system?
    if not os.path.exists(filename):
        print(f"Alert: {filename} not found. System bypass initiated.")
        return None

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Critical Error: File corrupted. Data integrity compromised.")
        return None
    except Exception as e:
        print(f"System Error: Unexpected interruption - {e}")
        return None
    finally:
        print("System Check Complete: File handle operation finished.")

if __name__ == "__main__":
    # Test the logic with a non-existent file to see the defense work
    load_agent_data("shadow_config.json")
