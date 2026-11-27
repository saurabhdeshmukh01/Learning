import datetime
import threading
import time

class Employee:
    def __init__(self, emp_id, name, salary=0):
        self.emp_id = emp_id
        self.name = name
        self.salary = 0
        self.joining_date = datetime.date.today()
        self.set_salary(salary)

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        try:
            if salary <= 0:
                raise ValueError("Salary must be greater than 0.")
            self.salary = salary
        except ValueError as err:
            print(f"Error for {self.name}: {err}")

    def calculate_bonus(self):
        if self.salary >= 80000:
            return self.salary * 0.15
        elif self.salary >= 50000:
            return self.salary * 0.10
        else:
            return self.salary * 0.05

    def show_details(self):
        bonus = self.calculate_bonus()
        print(f"\nEmployee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Joining Date  : {self.joining_date}")
        print(f"Base Salary   : {self.get_salary()}")
        print(f"Annual Bonus  : {bonus}")
        print(f"Total Pay     : {self.get_salary() + bonus}")


def generate_payslip(emp):
    print(f"Generating payslip for {emp.name}...")
    time.sleep(2)
    emp.show_details()
    print("Payslip ready.")


# Creating employee object
e1 = Employee(201, "Ananya", 60000)

# Testing exception handling and setter
e1.set_salary(-5000)
e1.set_salary(85000)

# Running payslip generation in a separate thread
t1 = threading.Thread(target=generate_payslip, args=(e1,))
t1.start()
t1.join()