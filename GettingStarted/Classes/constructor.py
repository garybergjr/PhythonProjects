students = []

# class Student:
#     def add_student(self, name, student_id=332):
#         student = {"name": name, "student_id": student_id}
#         students.append(student)

class Student:
    def __init__(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "Student"

mark = Student("Mark")

print(mark)

print(students)