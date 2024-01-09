class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_student_details(self):
        print(self.name,end=" ")
        print(self.age)

s = Student("Rohan",60)
s.print_student_details()


#Rohan 60