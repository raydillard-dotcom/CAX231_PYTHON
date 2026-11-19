
def run_list_operations():
    # Create a list 
    numbers = [42, 15, 8, 99, 23]
    
    # Print the original list
    print("Original list:")
    print(numbers)
    print("-" * 30)

    # Use the built-in sorted() function to print
    print("Sorted list (using sorted() - original remains unchanged):")
    sorted_version = sorted(numbers)
    print(sorted_version)
    print("Original list checked again (untouched):")
    print(numbers)
    print("-" * 30)

    # Use the list's .sort() method 
    print("Sorted list in place (using .sort()):")
    numbers.sort()
    print(numbers)
    print("-" * 30)

    # Add a new element to the list
    print("Updated list after appending 77:")
    numbers.append(77)
    print(numbers)
    print("-" * 30)

    # Remove an element from the list
    
    print("List after removing 15:")
    if 15 in numbers:
        numbers.remove(15)
    print(numbers)
    print("-" * 30)

    # Use the reverse() method to reverse the list
    print("Reversed list (using .reverse()):")
    numbers.reverse()
    print(numbers)
    print("-" * 30)

if __name__ == "__main__":
    run_list_operations()