from database import Student

students = Student.select()
for student in students:
    print(student.name, student.email, student.gender, student.age, student.course)