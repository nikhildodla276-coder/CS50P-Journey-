"""
Project: Intelligence Archive (File I/O Foundation)
Identity: Shadow Specialist
Goal: Moving from volatile RAM to permanent Disk storage.
"""

import sys

def main():
    # 1. Capture data from CLI (Week 1 skill)
    if len(sys.argv) < 2:
        sys.exit("Usage: python intelligence_archive.py [Log_Message]")

    log_entry = sys.argv[1]

    # 2. File I/O Logic: 'a' means Append (Don't delete old data)
    # Using 'with' ensures the file closes automatically (Professional Standard)
    try:
        with open("mission_log.txt", "a") as file:
            file.write(f"{log_entry}\n")
        print("Success: Intelligence archived to mission_log.txt")
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    main()
