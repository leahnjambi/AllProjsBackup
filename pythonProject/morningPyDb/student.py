from database import Student
try:
    S_name = input("Enter Name\n")
    S_email = input("Enter the Email\n")
    S_gender = input("Enter Gender\n")
    S_age = input("Enter the Age\n")
    S_course = input("Enter course applied\n")
    Student.create(name = S_name, email = S_email, gender = S_gender, age = S_age, course = S_course)
    print("Student registration successful")

except:
    print("The data is not correct.Please try again later")