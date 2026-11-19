
def main():
    while True:
        #Prompt the user for input
        user_input = input("Please enter your age: ")

        try:
            #Attempt conversion to an integer
            age = int(user_input)

        except ValueError:
            #Print error and loop back to the top without breaking
            print("Error: That is not a valid number! Please try again.")
            continue

        #Display success message; exit the loop
        print(f"Success! Your age is: {age}")
        break


if __name__ == "__main__":
    main()
