"""
Project: Market Priority Engine (Day 7 - Week 1 Completion)
Logic: Using the 'statistics' and 'sys' libraries to analyze goal feasibility.
Identity: Shadow Specialist
"""

import sys
import statistics
import random

def main():
    # 1. Specialist Defense: Ensure goal is provided via CLI
    if len(sys.argv) < 2:
        sys.exit("Error: Target Goal required. Usage: python market_priority_engine.py [GoalName]")

    goal_name = sys.argv[1]

    # 2. Data Simulation: 7 Days of 'Efficiency Scores' (0-100)
    # This represents your first week's performance
    weekly_scores = [85, 90, 75, 88, 92, 80, 95] 

    # 3. Logic: Using the statistics library to find the Mean (Average)
    avg_efficiency = statistics.mean(weekly_scores)
    consistency_deviation = statistics.stdev(weekly_scores)

    print(f"--- SHADOW SYSTEM AUDIT: {goal_name} ---")
    print(f"Weekly Average Efficiency: {avg_efficiency:.2f}%")
    print(f"Consistency Deviation: {consistency_deviation:.2f} (Lower is better)")
    
    # 4. Strategic Decision Logic
    if avg_efficiency > 80 and consistency_deviation < 10:
        print("Status: ALPHA - System is Stable. Proceed to Unit Testing.")
    else:
        print("Status: BETA - Variance Detected. Recalibrate Routine.")

if __name__ == "__main__":
    main()
