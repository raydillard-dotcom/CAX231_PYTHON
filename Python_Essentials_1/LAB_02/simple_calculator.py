print("Simple Python Calculator")

# Ask the user to input two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
    # Exit early if the number input is invalid
    exit()

#  Ask the user to choose an operation

operation = input("Choose an operation (+, -, *, /): ").strip()

# Step 3 and 4: Perform the operation 

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Handle division by zero gracefully
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:

    # Handle operation error
    print(f"Error: '{operation}' is not a valid operation. Please use +, -, *, or /.")
