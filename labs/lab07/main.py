#==========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program prompts the user to input three sides of a triangle,
#                      validates whether these sides can form a triangle, and, if valid,
#                      computes the area using Heron’s formula. The program repeats
#                      until the user chooses to exit.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#==========================================================================

import math  # Import math module for square root function

def displayMyInfo():
    """Displays programmer information in a box of stars."""
    print("****************************************")
    print("*       Rayhan Noufal Arayilakath      *")
    print("*           rayhan@purdue.edu          *")
    print("*            CNIT 155 Lab 07           *")
    print("****************************************")
    # Print a decorative header containing the my name, email, and lab information

def validate(a, b, c):
    """Checks if the given three sides form a valid triangle."""
    print("\nValidating the triangle...\n")
    #  Check if the sum of any two sides is greater than the third side
    if a + b > c and a + c > b and b + c > a:
        print("This is a valid triangle.")
        return True
    else:
        print("This is not a valid triangle. Please enter different numbers.\n")
        return False

def computeArea(a, b, c):
    """Computes and returns the area of a valid triangle using Heron's formula."""
    s = (a + b + c) / 2
    # Calculate the semi-perimeter of the triangle, which is needed for Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def main():
    displayMyInfo()

    """Main function controlling program execution."""
    while True:

        # Keep asking for valid triangle sides
        while True:
            try:
                a = float(input("Enter the 1st side of the triangle: "))
                b = float(input("Enter the 2nd side of the triangle: "))
                c = float(input("Enter the 3rd side of the triangle: "))

                if validate(a, b, c):
                    break  # Exit the loop if the triangle is valid
            except ValueError:
                print("Invalid input. Please enter numeric values.\n")

        area = computeArea(a, b, c)
        print(f"The area of the triangle is: {area:.2f}\n")

        invalid = False
        # A flag to track whether the previous input was invalid for formatting output properly

        # Ask user if they want to continue
        while True:
            msg = "Do you want to continue? (y/n): " if not invalid else "Invalid option. Do you want to continue? (y/n, case insensitive): "
            repeat = input(msg).strip()
            if repeat.lower() in ["y", "n"]:
                break
            else:
                invalid = True

        if repeat.lower() == "n":
            # If the user inputs 'n' (case insensitive), terminate the program
            print("End of the program.")
            break  # Exit the main loop

if __name__ == "__main__":
    # Standard Python convention to ensure main() runs only when this script is executed directly
    main()
