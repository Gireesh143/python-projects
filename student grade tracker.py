class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}")

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            print(f"Average grade for {self.name}: {average:.2f}")
        else:
            print(f"No grades available for {self.name}.")

student1 = Student("Bobby")
student1.add_grade(85)
student1.add_grade(90)
student1.calculate_average()

student2 = Student("Allen")
student2.add_grade(100)
student2.add_grade(90)
student2.calculate_average()
