# ===============================================================
# Name & Lab Section: Rayhan Noufal Arayilakath, Thursday 9:30 AM
# Purdue Email: rayhan@purdue.edu
# Program Description: This program calculates the temperature given an input in Fahrenheit.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
# ================================================================


def main():
    # Define the output string for the header
    output = """
\t================================================
\t*             CNIT155 Assignment 02            *
\t*                                              *
\t*             Conversion Calculator            *
\t================================================
    """

    # Print the output string to the console using the print() function
    print(output)

    # Prompt the user to enter their name
    name = input("==> Enter your name: ")

    print(f"Hello, {name}!\n")

    # Prompt the user to enter the number of pounds to convert
    print("==> 1. Pounds to Kilograms conversion")
    pounds = float(input("Enter the number of pounds to convert: "))

    # Calculate kilograms from the number of pounds
    kilograms = pounds / 2.2046

    print(
        f"The weight entered in pounds is {pounds:.2f} lbs and it is {kilograms:.2f} kg"
    )

    # Prompt the user to enter the temperature in celsius to convert
    print("\n==> 2. Celsius to Fahrenheit conversion")
    celsius = float(input("Enter the Celsius temperature to convert: "))

    # Calculate fahrenheit from celsius
    fahrenheit = (celsius * 9 / 5) + 32

    print(
        f"The temperature entered in Celsius is {celsius:.2f} C and it is {fahrenheit:.2f} F"
    )

    # Prompt the user to enter the number of miles to convert
    print("\n==> 3. Miles to Kilometers conversion")
    miles = float(input("Enter the distance in miles to convert: "))

    # Calculate kilometers from the number of miles
    kilometers = miles * 1.609344

    print(
        f"The distance entered in miles is {miles:.2f} mi and it is {kilometers:.2f} km"
    )

    # Prompt the user to enter the number of yards to convert
    print("\n==> 4. Yards to Meters conversion")
    yards = float(input("Enter the distance in yards to convert: "))

    # Calculate meters from the number of yards
    meters = yards * 0.9144

    print(
        f"The distance entered in yards is {yards:.2f} yards and it is {meters:.2f} m."
    )

    # Prompt the user to enter their height in feed and inches
    print("\n==> 5. Feet and Inches to Centimeters")
    print("What is your height in feet and inches?")
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))

    # Calculate centimeters from feet and inches
    centimeters = (feet * 30.48) + (inches * 2.54)

    print(
        f"The entered height is {feet} feet {inches} inches and it is {centimeters:.2f} cm"
    )


if __name__ == "__main__":
    main()
