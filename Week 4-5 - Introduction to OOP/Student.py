class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        total = sum(self.grades)
        count = len(self.grades)
        return total / count

student1 = Student("Ahmet", 20)

student1.add_grade(85)
student1.add_grade(90)

print(f"Student Name = {student1.name}")
print(f"Student Age = {student1.age}")
print(f"Student Grades = {student1.grades}")

avg = student1.calculate_average()
print(f"Grade Average = {avg:.2f}")