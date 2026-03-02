# ==========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program allows users to enter the number of students,
#                      then for each student, prompts for the name and GPA (0 <= GPA <= 4.0),
#                      storing them in lists, and finally prints the maximum and average GPA.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ==========================================================================


def displayMyInfo():
    """Displays programmer information in a box of stars."""
    print("========================================")
    print("=       Rayhan Noufal Arayilakath      =")
    print("=           rayhan@purdue.edu          =")
    print("=            CNIT 155 Lab 08           =")
    print("========================================")
    # Print a decorative header containing the my name, email, and lab information


def main():
    """Main function controlling program execution."""
    displayMyInfo()

    # Prompt the user for the number of students
    n = int(input("Number of students: "))

    # Create two empty lists for storing names and GPAs
    names = []  # Will store all entered names
    gpas = []  # Will store all corresponding GPAs

    # Loop through each student to get their name and GPA
    for i in range(n):
        print(f"==> Student {i + 1} / {n}")  # Print a header for each student
        name = input("Name: ")  # Prompt user to enter student's name

        # Keep asking for a valid GPA in the range [0, 4.0]
        while True:
            gpa = float(input("GPA: "))
            if gpa < 0 or gpa > 4.0:
                print("Invalid GPA. Please enter a value between 0.0 and 4.0.")
            else:
                break

        names.append(name)  # Add valid name to the names list
        gpas.append(gpa)  # Add valid GPA to the gpas list

    # Print the list header exactly as shown
    print("\n------------LIST------------")
    print("NAME                GPA")

    # Print each student's info from the lists
    for i in range(n):
        print(f"{names[i]}{' ' * (20 - len(names[i]))}{gpas[i]}")

    # Find the maximum GPA using a loop (no built-in max function)
    max_gpa = gpas[0]
    for i in range(1, n):
        if gpas[i] > max_gpa:
            max_gpa = gpas[i]

    # Compute the sum of all GPAs using a loop (no built-in sum function)
    total = 0
    for g in gpas:
        total += g

    # Calculate the average GPA
    avg_gpa = total / n

    # Print max GPA and average GPA with two decimal places (for the average)
    print("----------------------------")
    print(f"max GPA: {max_gpa}")
    print(f"average GPA: {avg_gpa:.2f}")


# Standard Python convention to run main only if this script is executed directly
if __name__ == "__main__":
    main()
