from database import Employee
try:
    E_name = input("Enter Name\n")
    E_gender = input("The gender\n")
    E_age = input("Enter Age\n")
    E_career = input("Enter the Career done\n")
    E_department = input("Enter Department\n")
    E_salary = input("Employee salary\n")
    Employee.create(name=E_name, department=E_department, salary=E_salary)
    print("The employee entrance successfully")

except:
    print("Please try again later")