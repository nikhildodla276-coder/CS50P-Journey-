"""
Mission: Day 5 - Library Mastery
Specialist: Shadow Specialist
Logic: Using sys for CLI input and random for data simulation.
"""
import sys
import random

def main():
    # 1. The Shield: Validate command line input
    if len(sys.argv) < 2:
        sys.exit("Usage: python market_analyzer.py [Project_Name]")

    project = sys.argv[1]
    
    # 2. The Library Logic: Simulating a success probability
    success_rate = random.randint(1, 100)

    print(f"--- Analysis for: {project} ---")
    print(f"Calculated Success Probability: {success_rate}%")

    if success_rate > 70:
        print("Verdict: High-value target. Execute immediately.")
    else:
        print("Verdict: High risk. Re-evaluate system parameters.")

if __name__ == "__main__":
    main()
