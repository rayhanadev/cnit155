#===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Friday 7:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program calculates the temperature given an input in Fahrenheit.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#================================================================

def main():
    print("Hello World!")
    print("This is my first Python program!\n")

    # Prompt the user for the temperature in Fahrenheit
    # This is a floating-point number, which means it can have decimal places.
    fahrenheit = float(input("Enter today's temperature in Fahrenheit (°F): "))

    # Calculate the temperature in Celsius
    # The formula to convert Fahrenheit to Celsius is:
    # Celsius = (Fahrenheit - 32) * 5/9

    celsius = (fahrenheit - 32) * 5/9

    # Print the temperature in Celsius to the console
    print(f"Today's temperature in Celsius is {celsius:.2f}°C")

    # Output the data type of the variable fahrenheit
    print(f"The data type of the input variable is {type(fahrenheit)}")


if __name__ == "__main__":
    main()
