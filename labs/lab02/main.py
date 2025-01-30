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
    # Define some variables to replace the placeholders in the output string
    name = "Rayhan Noufal Arayilakath"
    email = "rayhan@purdue.edu"

    # Define the output string, using the variables above to replace the placeholders
    output = f"""
===================================
* Name: {name} *
* Email: {email}        *
* CNIT15500 - InLab02             *
===================================
    """

    # Print the output string to the console using the print() function
    print(output)

    # Prompt the user to enter the number of students in CNIT 15501
    num_students = int(input("Enter the number of students in CNIT 155: "))

    # Print the number of students to the console and the data type of the number of students
    print(f"The number of students in CNIT 155 is {num_students}")
    print(f"The data type of the number of students is {type(num_students)}\n")

    # Prompt the user to enter the price of a textbook
    textbook_price = float(input("Enter the price of a textbook: "))

    # Prompt the user to enter the quantity of textbooks
    textbook_quantity = int(input("Enter the quantity of textbooks: "))

    # Calculate the total price of the textbooks and print it to the console
    total_price = textbook_price * textbook_quantity
    plural = "s" if textbook_quantity != 1 else ""

    print(
        f"The total price of {textbook_quantity} textbook{plural} is ${total_price:.2f}"
    )
    print(f"The data type of price is {type(total_price)}\n")

    # Prompt the user for the length of the base of a triangle and the height of the triangle
    base = int(input("Enter the length of the base of the triangle(int): "))
    height = int(input("Enter the height of the triangle(int): "))

    # Calculate the area of the triangle and print it to the console
    area = 0.5 * base * height

    print(
        f"The area of the triangle with base {base} and height {height} is {area:.2f}"
    )
    print(f"The data type of area is {type(area)}\n")

    # Prompt the user to enter the distance in miles and the duration in hours
    distance = float(input("Enter the distance in miles travelled by the car: "))
    duration = float(input("Enter the time in hours spent traveling: "))

    # Calculate the speed of the car and print it to the console
    speed = distance / duration

    print(
        f"To travel {distance:.1f} miles in {duration:.1f} hours, the average speed of the car is {speed:.2f} mph"
    )
    print(f"The data type of speed is {type(speed)}")


if __name__ == "__main__":
    main()
