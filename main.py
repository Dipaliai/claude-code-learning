"""
Student Grade Calculator
A simple program to calculate student grades.

This program has INTENTIONAL BUGS for learning purposes!
Your job is to find and fix them using Claude Code.
"""

from utils import get_grades, display_grades


def calculate_average(grades):
    """
    Calculate the average grade.
    
    Args:
        grades (list): List of grade numbers
        
    Returns:
        float: The average grade
        
    BUG #1 IS HIDDEN IN THIS FUNCTION!
    """
    if not grades:
        return 0
    
    total = sum(grades)
    # TODO: Fix this bug - the formula is wrong!
    # The formula should be: total / number of grades
    # But something is wrong with the order of operations
    return total / len(grades) * 100


def get_letter_grade(average):
    """
    Convert a numeric average to a letter grade.
    
    Args:
        average (float): The numeric average (0-100)
        
    Returns:
        str: The letter grade (A, B, C, D, F)
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def print_report(student_name, grades, average):
    """
    Print a formatted grade report.
    
    Args:
        student_name (str): Name of the student
        grades (list): List of grades
        average (float): The average grade
    """
    print("\n" + "="*50)
    print("📊 GRADE REPORT")
    print("="*50)
    print(f"Student: {student_name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {get_letter_grade(average)}")
    print("="*50 + "\n")


def main():
    """
    Main function to run the grade calculator.
    """
    print("\n🎓 Welcome to the Student Grade Calculator!")
    print("-" * 50)
    
    # Get student name
    student_name = input("Enter student name: ").strip()
    
    # Get grades from user
    grades = get_grades()
    
    if not grades:
        print("❌ No valid grades entered. Exiting.")
        return
    
    # Display grades
    display_grades(grades)
    
    # Calculate average
    average = calculate_average(grades)
    
    # Print report
    print_report(student_name, grades, average)


if __name__ == "__main__":
    main()
