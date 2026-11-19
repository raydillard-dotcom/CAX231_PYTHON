
# Function Definitions

def greet_user(name=""):
    """
    Greets a user by name. If no name is provided (defaults to an empty string),
    it prints a generic welcome message.
    """
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Welcome! Two my world of Python programming! Thank you for stopping by!")


def add_two_numbers(a, b):
    """
    Takes two numbers (a and b), calculates their sum,
    and returns the result.
    """
    return a + b


def is_even(num):
    """
    Determines if a number is even. Returns True if even, 
    or False otherwise.
    """
    return num % 2 == 0


# Main Execution Block

if __name__ == "__main__":
    
    #Greet user
    print("*** Demonstrating greet_user() ***")
    greet_user("Mrs. Kelly")  #Provided name
    greet_user()         # Without a name (uses default parameter value)

    
    #Add two numbers
    print("\n*** Demonstrating add_two_numbers() ***")
    
    #Storing the returned value in a variable
    sum_result = add_two_numbers(12, 18)
    print(f"The sum of 12 and 18 is: {sum_result}")
    
    #Using the returned value directly in an expression
    expression_result = add_two_numbers(5, 5) * 3
    print(f"The sum of 5 and 5, multiplied by 3, is: {expression_result}")

    
    #Demonstrate even number check
    print("\n*** Demonstrating is_even() ***")
    
    number_one = 4
    number_two = 7
    
    #Storing and printing results in a descriptive way
    even_status_one = is_even(number_one)
    even_status_two = is_even(number_two)
    
    print(f"{number_one} is even: {even_status_one}")
    print(f"{number_two} is even: {even_status_two}")