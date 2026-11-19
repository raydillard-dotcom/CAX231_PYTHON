
def safe_divide(a, b):
    """
    Divides two numbers. If the divisor (b) is zero, it explicitly 
    raises a ValueError with a custom error message.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("=== 1 & 2 & 3. Custom Exception & Finally Block Demo ===")
    
    # Test cases: normal division and division by zero
    test_cases = [
        (10, 2),
        (5, 0),  # This will trigger the ValueError
        (8, 4)
    ]
    
    for numerator, denominator in test_cases:
        print(f"\nAttempting to divide {numerator} by {denominator}...")
        try:
            # Call safe_divide which might raise a ValueError
            result = safe_divide(numerator, denominator)
            print(f"Success! Result: {result}")
        
        except ValueError as e:
            # Catch the specific ValueError raised by safe_divide()
            print(f"Error caught: {e}")
            
        finally:
            # This block always runs regardless of whether an exception occurred or not
            print("Division operation completed.")

    print("\n=== 4. Generic Exception Demo ===")
    
    #Intentionally attempting an unsafe operation: converting an invalid string to an integer
    invalid_string_input = "hello_world"
    
    try:
        print(f"Attempting to convert '{invalid_string_input}' to an integer...")
        converted_value = int(invalid_string_input)
        print(f"Converted value: {converted_value}")
        
    except Exception as e:
        #Catch any generic exception and print a message
        print(f"Caught a generic exception: {type(e).__name__} -> {e}")

if __name__ == "__main__":
    main()