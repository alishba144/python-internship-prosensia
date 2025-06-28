"""
Student Record System
Python Internship - Day 4 | ProSensia
Author: Alishba Malik

Description:
A simple Python program to manage student records using:
- Tuples for storing immutable student IDs
- Sets for managing unique course names
"""

# ----------------- Student Data -----------------

def get_student_ids():
    """
    Returns a tuple of formatted student IDs (immutable).
    Format: Std-01, Std-02, ...
    """
    return tuple(f"Std-{str(i).zfill(2)}" for i in range(1, 6))  # Generates Std-01 to Std-05

def display_student_ids(student_ids):
    """
    Displays all student IDs.
    """
    print("\nRegistered Student IDs:")
    for sid in student_ids:
        print(f"- {sid}")

# ----------------- Course Management -----------------

def initialize_courses():
    """
    Initializes a set of unique course names.
    """
    return {"Python", "AI", "ML", "Data Structures", "OOP"}

def add_courses(course_set, course_list):
    """
    Adds multiple new courses to the set.
    Ignores duplicates.
    """
    for course in course_list:
        if course not in course_set:
            course_set.add(course)

def remove_courses(course_set, course_list):
    """
    Removes specified courses from the set, if they exist.
    """
    for course in course_list:
        course_set.discard(course)  # avoids error if course doesn't exist

def display_courses(course_set):
    """
    Displays all current courses in alphabetical order.
    """
    print("\nAvailable Courses:")
    for course in sorted(course_set):
        print(f"- {course}")

# ----------------- Main Program -----------------

def main():
    print("Student Record System")

    # Display student IDs
    student_ids = get_student_ids()
    display_student_ids(student_ids)

    # Initialize course set
    courses = initialize_courses()

    # Add new courses
    new_courses = ["Cyber Security", "Cloud Computing", "Python", "Web Development"]
    add_courses(courses, new_courses)

    # Remove some courses
    courses_to_remove = ["AI", "OOP", "Blockchain"]
    remove_courses(courses, courses_to_remove)

    # Display final course list
    display_courses(courses)

# ----------------- Run Program -----------------

if __name__ == "__main__":
    main()

