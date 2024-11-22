# Temel sınıf Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Ad: {self.name}, Yaş: {self.age}"

# Person sınıfından türetilen Student sınıfı
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}, Öğrenci Numarası: {self.student_id}"

# Person sınıfından türetilen Teacher sınıfı
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Ders: {self.subject}"

# Test kısmı
if __name__ == "__main__":
    # Bir öğrenci oluştur
    student = Student("Ali", 20, "23580158")
    print(student.display_info())
    
    # Bir öğretmen oluştur
    teacher = Teacher("Ayşe", 35, "Matematik")
    print(teacher.display_info())
