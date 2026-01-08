"""
Project: Sovereign Internship Filter (v1.0)
Specialist: Nikhil (The Shadow Specialist)
Objective: Using sys.argv to filter dictionaries for high-value roles.
"""
import sys

def main():
    # 1. The Shield: Ensure user provided a salary input
    if len(sys.argv) < 2:
        print("Usage: python internship_filter.py [min_salary]")
        sys.exit(1)

    # 2. The Conversion: Try to turn the input into a number
    try:
        min_salary = int(sys.argv[1])
    except ValueError:
        print("Error: Please enter a numeric value for the salary.")
        sys.exit(1)

    # 3. The Database: A List of Dictionaries
    jobs = [
        {"name": "Sovereign AI", "pay": 65000, "type": "Remote"},
        {"name": "Global Tech", "pay": 45000, "type": "Hybrid"},
        {"name": "Local SlaveCorp", "pay": 15000, "type": "On-site"},
        {"name": "Euro-Botics", "pay": 55000, "type": "Remote"},
        {"name": "Cyber-Agent Inc", "pay": 30000, "type": "Remote"},
    ]

    # 4. The Engine: Loop and Filter
    print(f"\n--- Searching for jobs paying >= ₹{min_salary} ---\n")
    found = False
    for job in jobs:
        if job["pay"] >= min_salary:
            print(f"✅ MATCH: {job['name']} | Pay: ₹{job['pay']} | {job['type']}")
            found = True
    
    if not found:
        print("No roles found matching your Sovereign Standard.")

if __name__ == "__main__":
    main()
