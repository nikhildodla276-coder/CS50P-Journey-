"""
CS50P - Lecture 1: Functions & Variables
Specialist: Nikhil (Shadow Specialist)
Objective: Mastering user input and function modularity.
"""

def main():
    # Normalize input: strip whitespace and capitalize each word
    user_name = input("Enter your name: ").strip().title()
    execute_greeting(user_name)

def execute_greeting(name):
    # If name is empty, provide a default specialist identity
    if not name:
        name = "Shadow Specialist"
    print(f"System Authorized. Welcome, {name}.")

if __name__ == "__main__":
    main()