# ===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 11:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This Python program displays a menu with five options,
# allowing users to perform various computations (sum of odd numbers, sum of
# squares of even numbers, prime number check, multiplication table, and exit).
# The program repeats until the user selects the exit option.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ================================================================

def main():
    while True:
        # Display menu
        print("\n=================================================")
        print("Assignment 5: While Loop")
        print("=================================================")
        print("==> 1. Sum of odd numbers from 1 to N")
        print("==> 2. Sum of squares of even numbers from 1 to N")
        print("==> 3. Check if N (N >= 2) is prime")
        print("==> 4. Print the multiplication table of N")
        print("==> 5. Exit")
        print("=================================================")

        # Get user choice
        choice = input("\nYour choice (1-5): ").strip()

        if choice == "5":
            print(">>> End of While Loop <<<")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("\nInvalid selection! Please enter a number between 1 and 5")
            continue

        # Get user input for N
        try:
            N = int(input("Enter the value of N: "))
            if N <= 0:
                print("\nError: N must be a positive natural number!")
                continue
        except ValueError:
            print("\nError: Invalid numeric input! Please enter a positive integer")
            continue

        if choice == "1":
            # Sum of odd natural numbers
            sum_odd = 0
            i = 1
            print(f"Odd numbers from 1 to {N}:")
            while i <= N:
                print(i)
                sum_odd += i
                i += 2
            print(f"Sum of odd numbers from 1 to {N}: {sum_odd}")

        elif choice == "2":
            # Sum of squares of even natural numbers
            sum_squares = 0
            i = 2
            print(f"Even numbers from 1 to {N}:")
            while i <= N:
                print(i)
                sum_squares += i ** 2
                i += 2
            print(f"Sum of squares of even numbers from 1 to {N}: {sum_squares}")

        elif choice == "3":
            # Prime number check
            if N < 2:
                print(f"{N} is not a prime number")
            else:
                is_prime = True
                i = 2
                while i * i <= N:
                    if N % i == 0:
                        is_prime = False
                        break
                    i += 1
                if is_prime:
                    print(f"{N} is a prime number")
                else:
                    print(f"{N} is not a prime number")

        elif choice == "4":
            # Multiplication table
            print(f"Multiplication table of {N}:")
            i = 1
            while i <= 10:
                print(f"{N} x {i} = {N * i}")
                i += 1

if __name__ == "__main__":
    main()
