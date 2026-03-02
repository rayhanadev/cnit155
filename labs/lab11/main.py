# ==========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program prompts users to enter their daily step count for the past week (7 days),
#                      validates the input to ensure positive numbers, converts steps to miles (2000 steps = 1 mile),
#                      and displays the miles walked for each day.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ==========================================================================


def displayMyInfo():
    """Displays programmer information in a box of stars."""
    print("========================================")
    print("=       Steps to Miles Calculator     =")
    print("=              Lab 11                 =")
    print("=      Rayhan Noufal Arayilakath      =")
    print("========================================")
    # Print a decorative header containing the my name, email, and lab information


def main():
    """Main function controlling program execution."""
    displayMyInfo()

    # Create a list for steps each day
    steps = []
    
    print("Enter the number of steps for the past week (7 days):")

    # Prompt user for steps for the past week (7 days)
    for day in range(7):
        while True:
            try:
                # Request steps for each day
                step_input = input(f"Day {day + 1}: ")
                
                # Check if input is a valid number and positive
                steps_taken = int(step_input)
                if steps_taken < 0:
                    raise ValueError("Please enter a valid number of steps.")
                
                # Append the valid number of steps
                steps.append(steps_taken)
                break  # Exit the while loop when valid input is received

            except ValueError:
                print("ValueError: Please enter a valid number of steps.")

    # Convert steps to miles (assumption: 2000 steps = 1 mile)
    miles = [steps_taken / 2000.0 for steps_taken in steps]

    # Print the miles walked for each day
    print("\n-> The number of miles you walked in the past week:")
    for i in range(7):
        print(f"Day {i + 1}: {miles[i]:.2f} miles")

    # Calculate average miles
    avg_miles = sum(miles) / len(miles)

    # Print the average miles
    print(f"\n-> Average miles walked in the past week: {avg_miles:.2f} miles")


# Standard Python convention to run main only if this script is executed directly
if __name__ == "__main__":
    main()
