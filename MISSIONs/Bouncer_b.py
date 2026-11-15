
def check_age():
    user_input = input("Please enter your age: ")
    
    try:
        age = int(user_input)  # <-- This line MUST be indented!
    except ValueError:
        print("❌ That's not a valid number!")
        return

    if age < 18:
        print("Please come back to the club when you're older.")
        return
    elif 18 <= age <= 21: 
        print("You can come in, but with a hand stamp - NO DRINKING!!!! 🚫🍷")
    else:
        print("WELCOME")

    message = "PLEASE DRINK RESPONSIBLY"
    print(message)

check_age()14