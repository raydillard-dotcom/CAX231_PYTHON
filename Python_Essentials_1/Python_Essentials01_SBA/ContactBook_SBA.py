
def add_contact(contacts):
    """Prompt user for a new contact, check for duplicates, and store it."""
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    
    if not name:
        print("Error: Name cannot be empty.")
        return

    #Check for duplicate names (case-insensitive check)
    for existing_name in contacts:
        if existing_name.lower() == name.lower():
            print(f"Error: '{existing_name}' already exists in the contact book. Duplicate not added.")
            return

    phone = input("Enter phone number (digits and hyphens only, min 7 chars): ").strip()
    
    #Simple validation
    if not phone:
        print("Error: Phone number cannot be empty.")
        return

    contacts[name] = phone
    print(f"Success: '{name}' has been added to your contacts.")


def view_contacts(contacts):
    """Display all stored contacts in alphabetical order."""
    print("\n All Contacts")
    if not contacts:
        print("Your contact list is currently empty.")
        return

    print(f"{'Name':<20} | {'Phone Number'}")
    print("-" * 35)
    for name in sorted(contacts.keys()):
        print(f"{name:<20} | {contacts[name]}")


def search_contact(contacts):
    """Search for contacts by name or partial query."""
    print("\n Search Contacts ")
    if not contacts:
        print("Your contact list is empty. Nothing to search.")
        return

    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("Error: Search query cannot be empty.")
        return

    found = False
    print(f"\nSearch Results for '{query}':")
    print("-" * 35)
    
    for name, phone in contacts.items():
        if query in name.lower():
            print(f"{name}: {phone}")
            found = True

    if not found:
        print(f"No contacts found matching '{query}'.")


def delete_contact(contacts):
    """Delete a contact by name if it exists."""
    print("\n--- Delete Contact ---")
    if not contacts:
        print("Contact list is empty. No contacts to delete.")
        return

    name = input("Enter the name of the contact to delete: ").strip()
    
    matched_key = None
    for key in contacts:
        if key.lower() == name.lower():
            matched_key = key
            break

    if matched_key:
        del contacts[matched_key]
        print(f"Success: '{matched_key}' has been deleted from your contacts.")
    else:
        print(f"Error: '{name}' was not found in the contact book.")


def main():
    print("=== Contact Book Directory ===\n")
    
    #Initial dictionary containing contact names (keys) and phone numbers (values)
    phone_book = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9876"
    }
    
    print("Initial Contact Directory:")
    print(phone_book)  # Outputs: {'Alice': '555-1234', 'Bob': '555-5678', ...}
    
    #Look up and print Bob's phone number using his name as the key
    print("\n--- Looking Up a Contact ---")
    bobs_number = phone_book.get("Bob", "Not Found")
    print(f"Bob's phone number: {bobs_number}")
    
    #Update Alice's phone number to "555-0000"
    print("\n--- 2. Updating an Existing Contact ---")
    print(f"Alice's previous number: {phone_book['Alice']}")
    phone_book["Alice"] = "555-0000"
    print(f"Alice's updated number: {phone_book['Alice']}")
    
    #Add a new person "David" with the phone number "555-4321"
    print("\n--- 3. Adding a New Contact ---")
    phone_book["David"] = "555-4321"
    print("Successfully added David to the directory.")
    
    #Final display of the pre-configured dictionary using a loop
    print("\n--- Initial Setup Roster ---")
    for name, number in phone_book.items():
        print(f"{name}: {number}")

    #Interactive Console Menu Loop
    
    while True:
        print("\n==============================")
        print("        CONTACT BOOK MENU")
        print("================================")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("==============================")

        # Exception handling for menu choice conversion
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 5.")
            continue

        # Route user to the appropriate feature function
        if choice == 1:
            add_contact(phone_book)
        elif choice == 2:
            view_contacts(phone_book)
        elif choice == 3:
            search_contact(phone_book)
        elif choice == 4:
            delete_contact(phone_book)
        elif choice == 5:
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()