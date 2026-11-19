
def get_average_grade(grades_tuple):
    """
    Takes a tuple of numeric grades, calculates and returns the average.

    """
    try:
        # sum() adds all numbers in the tuple; len() counts them
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
    
        print(f"Warning: Encountered an empty grade tuple.")
        return None


def main():
    #Define a dictionary mapping course names to tuples of grades
    course_grades = {
        "Math": (88, 92, 79, 95),
        "Science": (85, 90, 78),
        "History": (91, 84, 89, 93, 87),
        "Art": (100, 98, 95), 
    }

    print("Processing Course Grades \n")

    #Use a loop to iterate over the dictionary items
    for course, grades in course_grades.items():
        
        avg = get_average_grade(grades)
        
        #Handle any None values when printing the results
        if avg is not None:
            print(f"The average grade for {course} is {avg:.1f}")
        else:
            print(f"The average grade for {course} could not be calculated (no grades available).\n")


if __name__ == "__main__":
    main()