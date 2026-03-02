# ==========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 11:30am
# Purdue Email: rayhan@purdue.edu
# Program Description: This Python program displays a menu with four options
#                      and asks the user to select one of the options. Depending
#                      on the user’s choice, the program performs various computations.
#                      The menu is displayed repeatedly until the user chooses Exit.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ==========================================================================


def main():
    option = 0  # Variable to store user choice

    while option != 4:  # Loop until the user chooses to exit
        # Display the menu
        print("-------------------------------------------------")
        print("        InLab 06 For Loop Menu:")
        print("-------------------------------------------------")
        print("1. Display and add all even natural numbers from 1 to N")
        print("2. Display the multiplication table of N")
        print("3. Print a triangle of numbers up to N")
        print("4. Exit")
        print("-------------------------------------------------")

        # Get user choice
        option = int(input("Select an option (1-4): "))

        if option == 1:
            N = int(input("Enter a natural number N: "))
            print(f"Even numbers from 1 to {N}:")
            sum_even = 0
            for i in range(1, N + 1):
                if i % 2 == 0:
                    print(i)
                    sum_even += i
            print(f"Sum of even numbers = {sum_even}\n")

        elif option == 2:
            N = int(input("Enter a natural number N: "))
            print(f"Multiplication table of {N}:")
            for i in range(1, 11):
                print(f"{N} x {i} = {N * i}")
            print()

        elif option == 3:
            N = int(input("Enter a natural number N: "))
            print(f"Inverted triangle with {N} rows:")
            for i in range(N, 0, -1):
                print(" ".join(str(j) for j in range(1, i + 1)))
            print()

        elif option == 4:
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
