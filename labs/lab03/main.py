# ===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program works with the math library to calculate various measurements of a cone.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ================================================================

import math


def main():
    # Define the header string
    output = """
==================================================
          Properties of a Truncated Code
==================================================
    """

    # Print the output string to the console using the print() function
    print(output)

    # Prompt the user to enter the various input values
    r1 = float(input("=>radius 1 (r1): "))
    r2 = float(input("=>radius 2 (r2): "))
    h = float(input("=>height (h): "))
    s = float(input("=>slant height (s): "))

    print("\nCalculating...")

    # Perform calculations for truncated cone
    volume = (1 / 3) * math.pi * h * (math.pow(r1, 2) + math.pow(r2, 2) + (r1 * r2))
    lateral_area = s * math.pi * (r1 + r2)
    total_surface_area = lateral_area + (math.pi * (math.pow(r1, 2) + math.pow(r2, 2)))

    # Print the results of the calculations
    print(f"\nVolume = {volume:.2f}")
    print(f"Lateral Area = {lateral_area:.2f}")
    print(f"Total surface area = {total_surface_area:.2f}")


if __name__ == "__main__":
    main()
