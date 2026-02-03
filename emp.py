class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee ID   :", self.emp_id)
        print("Name          :", self.name)
        print("Department    :", self.department)
        print("Salary        :", self.salary)
        print("---------------------------")


# Main program
n = int(input("Enter number of employees: "))

employees = []

for i in range(n):
    print("\nEnter details for Employee", i + 1)
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    emp = Employee(emp_id, name, department, salary)
    employees.append(emp)

print("\n--- Employee Details ---")
for emp in employees:
    emp.display()
