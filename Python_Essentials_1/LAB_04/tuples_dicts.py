
#Create a tuple have list of the twelve months
def main():
    
    months = (
        "January", "February", "March", "April", 
        "May", "June", "July", "August", 
        "September", "October", "November", "December"
    )
    
    #Print the first and last month using index 0 and index -1
    print(" Tuple Basics ")
    print(f"First month (index 0): {months[0]}")
    print(f"Last month (index -1): {months[-1]}")
    
    #Attempt to modify the tuple to demonstrate immutability
    print("\n Tuple Immutability Test ")
    try:
        months[0] = "NewMonth"
    except TypeError as e:
        print(f"Tuples are immutable, error: {e}")
        
    #Create a dictionary with student names and grades
    print("\n=== 4 - 7. Dictionary Operations ===")
    students = {
        "Alice": 90,
        "Bob": 85,
        "Charlie": 92,
        "Diana": 88
    }
    
    #Add a new student and grade, then print all entries
    students["Evan"] = 95
    print("Added a new student (Evan: 95). Current dictionary:")
    print(students)
    
    #Update one of the existing students' grades, then print the updated entry
    students["Bob"] = 89
    print(f"Updated Bob's grade. New entry -> Bob: {students['Bob']}")
    
    #Use a loop to print out each student's name and grade in a formatted way
    print("\n--- Final Student Roster ---")
    for name, grade in students.items():
        print(f"{name}: {grade}")


if __name__ == "__main__":
    main()
