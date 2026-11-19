

#CALCULATOR
def add(a, b):
    """The sum of a and b."""
    return a + b

def subtract(a, b):
    """The difference between a and b."""
    return a - b

def multiply(a, b):
    """The product of a and b."""
    return a * b

def divide(a, b):
    """The quotient of a and b. Handles division by zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def calculate(a, b, op):
    """
    Takes two numbers and an operator string, and delegates the 
    computation to the appropriate helper function.
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return f"Error: '{op}' is not a valid operation."

def main():
    print(" Python Calculator ")
    
    # Handle whole numberinput gracefully during conversion
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Input Error: Please enter valid numbers only.")
        return

    #Get the operation symbol
    op = input("Enter operation (+, -, *, /): ").strip()

    #Calculation errors
    try:
        result = calculate(num1, num2, op)
        print(f"Result: {num1} {op} {num2} = {result}")
    except ZeroDivisionError as e:
        print(f"Math Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()