# ===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This Python program displays a menu with two options and asks the user to
#                      select one of the options. Depending on the user’s choice, the program
#                      takes the user’s input and calculates simple interest and compound interest.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ================================================================

import math

def main():
    # Display the menu
        print("""
============ INTEREST CALCULATOR ============
a. Simple Interest Calculator
b. Compount Interest Calculator
c. Exit
=============================================""")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == 'a':
            print("\nSimple Interest Calculator")
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter interest rate in %: "))
            time = float(input("Enter time period in years: "))

            # Calculate simple interest
            simple_interest = (principal * rate * time) / 100
            final_amount = principal + simple_interest

            print(f"Final amount in simple interest is ${final_amount:.2f}")

        elif choice == 'b':
            print("\nCompound Interest Calculator")
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter interest rate in %: "))
            time = float(input("Enter time period in years: "))
            n = int(input("Enter number of times per year: "))

            # Calculate compound interest
            final_amount = principal * math.pow((1 + (rate / (100 * n))), (n * time))
            compound_interest = final_amount - principal

            print(f"Final amount in compound interest is ${final_amount:.2f}")

        elif choice == 'c':
            print("Thank you for using INTEREST CALCULATOR!")
            exit()

        else:
            print("Invalid input. Please choose between a, b, or c.")


if __name__ == "__main__":
    main()
