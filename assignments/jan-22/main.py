#=========================================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Friday 7:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program outputs text to the console.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=========================================================================

def main():
    # Define some variables to replace the placeholders in the output string
    name = "Rayhan Noufal Arayilakath"
    email = "rayhan@purdue.edu"

    # Define the output string, using the variables above to replace the placeholders
    output = f"""
\t================================================
\t*        Name: {name}       *
\t*           Email: {email}           *
\t*             CNIT155-Assignment 01            *
\t================================================

\t CCCCCCCCC         IIIIIIIIII         IIIIIIIIII
\tCC                     II                 II
\tCC                     II                 II
\tCC                     II                 II
\tCC                     II                 II
\tCC                     II                 II
\t CCCCCCCCC         IIIIIIIIII             II



\t    11              555555555          555555555
\t  1111             55                 55
\t    11             55                 55
\t    11             5555555555         5555555555
\t    11                     55                 55
\t    11                     55                 55
\t1111111111         555555555          555555555
    """

    # Print the output string to the console using the print() function
    print(output)


# This line calls the main() function when the program is run
# from the command line. This is the standard way to start a Python program.
if __name__ == "__main__":
    main()
