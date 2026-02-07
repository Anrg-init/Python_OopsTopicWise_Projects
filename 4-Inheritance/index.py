#Role managment system oops project uisng concepts of inheritance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} logged in")

    def logout(self):
        print(f"{self.name} logged out")


class Admin(User):
    def __init__(self, name, email, permissions):
        super().__init__(name, email)
        self.permissions = permissions

    def login(self):
        super().login()
        print("Admin security check passed")

    def create_user(self, username):
        print(f"Admin created user: {username}")


class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_material(self):
        print(f"{self.name} uploaded {self.subject} material")



class Student(User):
    def __init__(self, name, email, roll_no):
        super().__init__(name, email)
        self.roll_no = roll_no

    def view_material(self):
        print(f"{self.name} is viewing study material")



admin = Admin("Anurag", "admin@mail.com", "ALL")
teacher = Teacher("Ravi", "teacher@mail.com", "Math")
student = Student("Aman", "student@mail.com", 101)

admin.login()
admin.create_user("NewStudent")

teacher.login()
teacher.upload_material()

student.login()
student.view_material()
student.logout()
