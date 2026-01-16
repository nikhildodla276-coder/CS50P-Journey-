"""
Project: Secure Memory Vault (Error Handling)
Identity: Shadow Specialist
Goal: Day 2 of 3 - Building Unbreakable Data Pipelines.
"""

import json
import os

def load_agent_data(filename):
    # Defensive Check: Does the file even exist?
    if not os.path.exists(filename):
        print(f"Alert: {filename} not found. Initializing new system...")
        return None

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Critical Error: File corrupted. Data integrity compromised.")
        return None
    except Exception as e:
        print(f"Unexpected System Error: {e}")
        return None
    finally:
        print("System Audit: File access attempt complete.")

def main():
    filename = "agent_state.json"
    data = load_agent_data(filename)

    if data:
        print(f"Welcome back, {data.get('identity', 'Specialist')}.")
        # Update deep work log
        data["last_audit"] = "2026-01-16"
        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    else:
        print("System Recovery: Please run the Day 11 script to regenerate memory.")

if __name__ == "__main__":
    main()
