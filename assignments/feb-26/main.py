# =========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This Python program displays a menu with five options,
# allowing users to perform various computations:
#   - Displaying odd natural numbers from N1 to N2
#   - Computing the factorial of N
#   - Displaying a right-angled triangle of stars
#   - Displaying a centered triangle of stars
#   - Exiting the program
# The program continues running until the user selects the exit option.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# =========================================================================

def main():
    while True:
        # Display menu
        print("\n=========================================================")
        print("                 Assignment 6: For Loops")
        print("=========================================================")
        print("A. Display odd natural numbers from N1 to N2")
        print("B. Find the factorial of N using for loop")
        print("C. Display triangle of stars using for loop")
        print("D. Display centered triangle of stars using for loop")
        print("E. Exit")
        print("=========================================================")

        # Get user choice
        choice = input("\nOption: ").strip().upper()

        if choice == "E":
            print("\nExiting the program...")
            break

        if choice not in {"A", "B", "C", "D"}:
            print("\nInvalid option. Please enter a valid option.")
            continue

        if choice == "A":
            # Display odd numbers from N1 to N2
            print("\n==> Option A: Display odd natural numbers from N1 to N2 (include N1 and N2)")
            try:
                N1 = int(input("N1: "))
                N2 = int(input("N2: "))

                if N1 >= N2 or N1 < 1 or N2 < 1:
                    print("\nError: Ensure N1 < N2 and both are natural numbers!")
                    continue
            except ValueError:
                print("\nError: Invalid numeric input! Please enter natural numbers")
                continue

            print(f"\nDisplaying odd natural numbers from {N1} to {N2}:\n")
            for i in range(N1, N2 + 1):
                if i % 2 == 1:
                    print(i)

        elif choice == "B":
            # Compute the factorial of N
            print("\n==> Option B: Find factorial of N using for loop")
            try:
                N = int(input("Enter N: "))
                if N < 0:
                    print("\nError: N must be a non-negative integer!")
                    continue
            except ValueError:
                print("\nError: Invalid numeric input! Please enter a non-negative integer")
                continue

            factorial = 1
            for i in range(1, N + 1):
                factorial *= i

            print(f"Factorial of {N} is {factorial}")

        elif choice == "C":
            # Display Right Angled Triangle of Stars
            print("\n==> Option C: Display triangle of stars")
            try:
                rows = int(input("Enter num of rows (N): "))
                if rows < 1:
                    print("\nError: Number of rows must be a positive integer!")
                    continue
            except ValueError:
                print("\nError: Invalid numeric input! Please enter a positive integer")
                continue

            print("\nDisplaying triangle of stars with 7 rows:\n")
            for i in range(1, rows + 1):
                print((" " * (rows - i)) + ("*" * i))

        elif choice == "D":
            # Display Centered Triangle of Stars
            print("\n==> Option D: Display centered triangle of stars")
            try:
                rows = int(input("Enter num of rows: "))
                if rows < 1:
                    print("\nError: Number of rows must be a positive integer!")
                    continue
            except ValueError:
                print("\nError: Invalid numeric input! Please enter a positive integer")
                continue

            print("\nDisplaying centered triangle of stars with 7 rows:\n")
            for i in range(1, rows + 1):
                spaces = " " * (rows - i)
                stars = "*" * (2 * i - 1)
                print(spaces + stars)

if __name__ == "__main__":
    main()
