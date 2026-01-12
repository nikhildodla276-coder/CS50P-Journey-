def main():
    level = input("Internal Security Level: ")
    print(check_clearance(level))

def check_clearance(n):
    """
    Shadow Specialist Logic: Only levels 7 and above are 'Sovereign'.
    We handle strings to ensure the system doesn't crash on bad input.
    """
    try:
        n = int(n)
        if n >= 7:
            return "Sovereign"
        return "restricted"
    except ValueError:
        return "Invalid Input"

if __name__ == "__main__":
    main()
