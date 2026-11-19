
def check_age():
    # Enter your age
    user_input = input("Please enter your age: ")

    # Enter non-number error message
    try:
        age = int(user_input)
    except ValueError:
        print("❌❌❌ That's not a valid number! Please use a number. ❌❌❌")
        return

    # Club entry logic
    if age < 18:
        print("Please come back to the club when you're older.")
    elif 18 <= age <= 21:
        print("You can come in, but with a hand stamp - NO DRINKING!!!! 🚫🍷")
    else:
        print("WELCOME")

    # Final message
    message = "PLEASE DRINK RESPONSIBLY"
    print(message)

# Run the function
check_age()