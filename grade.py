def calculate_grade(marks):
    # Q5: Handle invalid marks using Exception Handling
    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks! Marks must be between 0 and 100.")
    
    # Q4: Calculate Grade using methods/functions
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"