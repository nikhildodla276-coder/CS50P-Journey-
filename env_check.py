import sys
import os

def system_diagnostic():
    print("--- Shadow Specialist System Diagnostic ---")
    try:
        # Check Python Version (The Nervous System)
        version = sys.version.split()[0]
        print(f"[SUCCESS] Python Engine: v{version}")
        
        # Check Current Directory (The Navigation Logic)
        path = os.getcwd()
        print(f"[SUCCESS] Active Path: {path}")
        
        print("\nStatus: Trinity Foundation Initialized. Ready for SQL Integration.")
    except Exception as e:
        print(f"[ERROR] System Mismatch: {e}")

if __name__ == "__main__":
    system_diagnostic()
