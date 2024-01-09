class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    
    def print_student_details(self):
        print(self.__name,end=" ")
        print(self.age)

s = Student("Rohan",20)
s.print_student_details()

# Rohan 20