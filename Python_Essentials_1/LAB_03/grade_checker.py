def check_grade():
    # Ask the user to input a numeric grade
    grade = float(input("Enter your numeric grade: "))
    # Use an if-elif-else structure to convert to a letter grade

    if grade >= 100:
        letter = "A+"
    elif grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"

    # Print the letter grade
    print(f"Your grade is: {letter}")

    # Final message using a conditional expression
    message = "Congratulations on a great job!" if letter in ["A+", "A", "B", "C"] else "Keep practicing and try again!"
    print(message)

if __name__ == "__main__":
    check_grade()