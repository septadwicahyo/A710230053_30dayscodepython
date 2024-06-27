# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")

# Class Student yang merupakan subclass dari Person
class Student(Person):
    def __init__(self, nama, umur, student_id, major, jurusan):
        super().__init__(nama, umur)  # Memperbaiki penggunaan super().__init__
        self.student_id = student_id
        self.major = major
        self.jurusan = jurusan

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Major: {self.major}, Jurusan: {self.jurusan}")

# Class Teacher yang merupakan subclass dari Person
class Teacher(Person):
    def __init__(self, nama, umur, employee_id, subject, pelajaran):
        super().__init__(nama, umur)  # Tetap benar pada penggunaan super().__init__
        self.employee_id = employee_id
        self.subject = subject
        self.pelajaran = pelajaran

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}, Subject: {self.subject}, Pelajaran: {self.pelajaran}")

# Membuat objek baru dari kelas Student dan Teacher
student = Student("Upin", 24, "S67890", "Pendidikan Teknik Informatika", "Teknik Informatika")
teacher = Teacher("Ipin", 22, "T12345", "Kalkulus", "Matematika")

# Menampilkan informasi student dan teacher
student.display()
teacher.display()
