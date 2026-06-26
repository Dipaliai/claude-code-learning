"""
Utility functions for the Grade Calculator.
This file contains helper functions.

BUG #2 IS HIDDEN IN THIS FILE!
"""


def get_grades():
    """
    Get grades from user input.
    
    Should accept multiple grades (0-100) from the user.
    User enters grades one by one, pressing Enter after each.
    Type 'done' when finished.
    
    Returns:
        list: List of valid grades
        
    BUG #2 IS HERE - MISSING INPUT VALIDATION!
    The function should check if grades are valid (0-100)
    and if at least one grade was entered.
    """
    grades = []
    
    print("\nEnter grades one by one (0-100).")
    print("Type 'done' when finished.\n")
    
    while True:
        user_input = input("Enter grade (or 'done'): ").strip()
        
        # Check if user wants to stop
        if user_input.lower() == "done":
            break
        
        try:
            # Convert input to float
            grade = float(user_input)
            
            # TODO: Fix this bug - ADD VALIDATION HERE!
            # Check if grade is between 0 and 100
            # If not, show error and ask again
            # If yes, add to grades list
            
            # Currently it just adds ANY number without checking!
            grades.append(grade)
            print(f"✅ Grade {grade} added")
            
        except ValueError:
            # This is fine - it handles non-numeric input
            print("❌ Please enter a valid number!")
            continue
    
    return grades


def display_grades(grades):
    """
    Display grades in a nice format.
    
    Args:
        grades (list): List of grades to display
    """
    if not grades:
        print("No grades to display.")
        return
    
    print("\n📝 Grades entered:")
    for i, grade in enumerate(grades, 1):
        print(f"   {i}. {grade}")
