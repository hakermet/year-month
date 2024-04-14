class SchoolMember:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
class Teacher(SchoolMember):
    def __init__(self,firstname,lastname,salary):
        super().__init__(firstname,lastname)
        self.salary=salary
    def tell(self):
        return f"Ім'я: {self.firstname}, Прізвище: {self.lastname}, Зарплата: {self.salary} грн"
class Student(SchoolMember):
    def __init__(self,firstname,lastname,average):
        super().__init__(firstname,lastname)
        self.average=average
    def tell(self):
        return f"Ім'я: {self.firstname}, Прізвище: {self.lastname}, Середнє: {sum(self.average)/len(self.average)}"

teacher = Teacher("Тарас", "Басюк", 30000)
student = Student("Олександр", "Кругліков", [9, 9, 10])

print(teacher.tell())
print(student.tell())