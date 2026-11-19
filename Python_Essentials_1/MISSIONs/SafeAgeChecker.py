
def main():
    while True:
        # Step 1: Prompt (or re-prompt) the user for input
        user_input = input("Please enter your age: ")

        try:
            # Step 2: Attempt conversion to an integer
            age = int(user_input)

        except ValueError:
            #Print error and loop back to the top without breaking
            print("Error: That is not a valid number! Please try again.")
            continue

        # Display success message; exit the loop
        print(f"Success! Your age is: {age}")
        break


if __name__ == "__main__":
    main()