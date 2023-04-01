from database import  Employee

employees = Employee.select()
for employee in employees:
    print(employee.name, employee.gender, employee.age, employee.career, employee.department, employee.salary)