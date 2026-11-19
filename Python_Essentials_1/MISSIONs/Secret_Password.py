
# variables

guess = ""
wrong_attempts = 0
max_attempts = 3

# The loop keeps running WHILE the user’s guess is wrong AND has three attempts

while guess != "python123" and wrong_attempts < max_attempts:
    guess = input("Enter password: ")
    
    if guess == "python123":
        print("Access granted.")
    else:
        wrong_attempts += 1
        
        # Check if they just hit the limit
                                                
        if wrong_attempts >= max_attempts:
            print("Account locked. Try again later.")
        else:
            print(f"Incorrect password. You have {max_attempts - wrong_attempts} attempt(s) left.\n")