
def main():
    print("=== Contact Book Directory ===\n")
    
    #Initial dictionary containing contact names (keys) and phone numbers (values)
    phone_book = {
            "Alice": "555-1234",
            "Bob": "555-5678",
            "Charlie": "555-9876"
            }
    
    #Displaying the raw dictionary object as requested
    print("Initial Contact Directory:")
    print(phone_book)  # Outputs: {'Alice': '555-1234', 'Bob': '555-5678', ...}
    
    #Look up and print Bob's phone number using his name as the key
    print("\n--- 1. Looking Up a Contact ---")
    #Using .get() is a safer practice to prevent crashes if a key doesn't exist
    bobs_number = phone_book.get("Bob")
    print(f"Bob's phone number: {bobs_number}")
    
    #Update Alice's phone number to "555-0000"
    print("\nUpdating an Existing Contact")
    print(f"Alice's previous number: {phone_book['Alice']}")
    phone_book["Alice"] = "555-0000"
    print(f"Alice's updated number: {phone_book['Alice']}")
    
    #Add a new person "David" with the phone number "555-4321"
    print("\n ++ Adding a New Contact ++ ")
    phone_book["David"] = "555-4321"
    print("Successfully added David to the directory.")
    
    #Final display of the updated directory using a loop for clean formatting
    print("\n Final Contact Roster ")
    for name, number in phone_book.items():
        print(f"{name}: {number}")


if __name__ == "__main__":
    main()