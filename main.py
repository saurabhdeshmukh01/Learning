import datetime
import threading
import time
import grade  # Q7: Import the grade.py module

class Student:
    # Q1: Constructor with Roll No, Name, and initial Marks
    def __init__(self, roll_no, name, marks=0):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 0  # Private attribute for encapsulation
        # Q6: Use datetime module to store admission date
        self.admission_date = datetime.date.today()
        self.set_marks(marks)

    # Q3: Getter for Marks
    def get_marks(self):
        return self.__marks

    # Q3 & Q5: Setter for Marks with Exception Handling
    def set_marks(self, marks):
        try:
            # Validate marks via the grade module before setting
            grade.calculate_grade(marks)
            self.__marks = marks
        except ValueError as e:
            print(f"Error for {self.name}: {e}")

    # Q4 & Q7: Method to get grade using the imported grade module
    def get_grade(self):
        return grade.calculate_grade(self.__marks)

    # Q2: Display student details
    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Roll No        : {self.roll_no}")
        print(f"Name           : {self.name}")
        print(f"Admission Date : {self.admission_date}")
        print(f"Marks          : {self.get_marks()}")
        print(f"Grade          : {self.get_grade()}")


# Q8: Function to simulate report generation using sleep()
def generate_report(student):
    print(f"\nGenerating report for {student.name}...")
    time.sleep(2)  # Simulates processing delay
    student.display_details()
    print("Report generation complete!")


# --- Main Execution ---
if __name__ == "__main__":
    # Q2: Create Student object
    student1 = Student(101, "Saurabh", 88)

    # Demonstrate Setter & Exception Handling (Q3 & Q5)
    student1.set_marks(105)  # Triggers ValueError
    student1.set_marks(92)   # Valid update

    # Q8: Create and run thread using start() and join()
    report_thread = threading.Thread(target=generate_report, args=(student1,))
    report_thread.start()
    report_thread.join()

    print("\nMain program finished.")