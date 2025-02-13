# ===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This Python program takes the user’s input and calculates
# the side area, bottom area, and volume of a pool.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ================================================================

import math  # Import math library for calculations

def main():
    # Print banner
    print("==================================================")
    print("*                   Purdue Pete                  *")
    print("*                  Assignment 03                 *")
    print("==================================================\n")

    # Prompt user for pool depth inputs
    D1 = float(input("Depth 1 (D1): "))
    D2 = float(input("Depth 2 (D2): "))

    # Check if D2 is greater than D1
    if D2 > D1:
        # Prompt user for width and length inputs
        W = float(input("Width (W): "))
        L = float(input("Length (L): "))

        print("\nCalculating...\n")

        # Calculate the side area
        side_area = ((D1 + D2) * L) / 2

        # Calculate the bottom area using hypotenuse formula
        hypotenuse = math.sqrt(L**2 + (D2 - D1)**2)  # Hypotenuse of the slanted bottom
        bottom_area = hypotenuse * W

        # Calculate the volume of the pool
        volume = side_area * W

        # Display the results with the exact output format
        print(f"Side area of the pool = (D1 + D2) x L / 2 = {side_area:.2f}")
        print(f"Bottom area of the pool = Hyp x W = {bottom_area:.2f}")
        print(f"Volume of the pool = Side area of the pool x W = {volume:.2f}")

    else:
        # Display error message if D2 is not greater than D1
        print("Invalid input: D2 must be greater than D1")
        print("Exiting program...")

# Run the program
if __name__ == "__main__":
    main()
