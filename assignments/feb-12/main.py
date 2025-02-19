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

import math  # Import the math library for exponential and logarithmic functions


def main():
    # Display header
    print("==============================================================")
    print("*                       Ray Arayilakath                      *")
    print("*                        Assignment 04                       *")
    print("==============================================================\n")

    # Display the radioactive materials menu along with an exit option
    print(">>>>> Radioactive Decay Simulation Menu <<<<<")
    print(">> a. Uranium-233")
    print(">> b. Radium-226")
    print(">> c. Carbon-14")
    print(">> d. Polonium-210")
    print(">> e. Exit\n")

    # Define a constant safe level value
    SAFE_LEVEL = 1

    # Initialize variables for material name and decay constant
    material_name = ""
    decay_constant = 0

    # Prompt the user to enter their selection
    choice = input("Enter your choice: ").strip().lower()  # Get input and normalize it
    print()

    # Define a dictionary for material names and decay constants so we can map user
    # choices (a, b, c, d) to (material_name, decay_constant)
    decay_data = {
        "a": ("Uranium-233", 4.35e-6),
        "b": ("Radium-226", 4.33e-4),
        "c": ("Carbon-14", 1.21e-4),
        "d": ("Polonium-210", 1.83),
    }

    # Check user choice for exit or invalid selection
    if choice == "e":
        # If 'e', exit the program
        print("Exiting program...")
        return
    elif choice not in decay_data:
        # Invalid selection
        print("Invalid selection! Exiting program...")
        return

    material_name, decay_constant = decay_data[choice]

    # Ask for initial amount (grams)
    try:
        initial_amount = float(
            input(f"Enter initial amount of {material_name} (grams): ")
        )
    except ValueError:
        print("Error: Invalid numeric input! Exiting program...")
        return

    # Ask for time elapsed (years)
    try:
        time_elapsed = float(input("Enter time elapsed (years): "))
    except ValueError:
        print("Error: Invalid numeric input! Exiting program...")
        return

    print()

    # Validate that initial_amount > 0 and time_elapsed >= 0
    if initial_amount <= 0:
        print("Error: Initial amount must be positive! Exiting program...")
        return

    if time_elapsed < 0:
        print("Error: Time elapsed cannot be negative! Exiting program...")
        return

    # Calculate the remaining amount using the formula: N_t = N0 * e^(-lambda * T)
    remaining_amount = initial_amount * math.exp(-decay_constant * time_elapsed)

    # Calculate the half-life using the formula: T1/2 = -ln(0.5)/lambda
    half_life = -math.log(0.5) / decay_constant

    # Calculate the activity using the formula: R = lambda * N0 * e^(-lambda * T)
    activity = (
        decay_constant * initial_amount * math.exp(-decay_constant * time_elapsed)
    )

    # Display the computed results with two decimal places for all numerical values
    print(f"----- {material_name} Decay Simulation Results -----")
    print(f"- Initial amount: {initial_amount:.2f} g")
    print(f"- Time elapsed: {time_elapsed:.2f} year(s)")
    print(f"- Remaining amount: {remaining_amount:.2f} g")
    print(f"- Half-life: {half_life:.2f} year(s)")
    print(f"- Activity: {activity:.2f} decay(s) per year")
    print()

    # Compare the remaining amount to the safe level and display the appropriate message
    if remaining_amount < SAFE_LEVEL:
        print("Safe level reached!")
    else:
        print("Safe level NOT reached!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
