class Student:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def putdata(self):
        print("Name: "+self.name+", Email: "+self.email)

class PhDguide:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.students = []

    def putdata(self):
        print(f"Guide Name: {self.name}, Guide Email: {self.email}")
        print("Students under this guide:")
        for student in self.students:
            student.putdata()

    def add(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def remove(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Removed student: {student.name}")
        else:
            print(f"Student {student.name} not found under this guide.")

student1 = Student("Rachon", "rachon@girgit.com")
student2 = Student("Vijar", "Vijar@yooha.com")

guide = PhDguide("Dr. VPN", "vpn@gmaal.com")

guide.add(student1)
print()
guide.add(student2)
print()

guide.putdata()
print()

guide.remove(student1)

guide.putdata()