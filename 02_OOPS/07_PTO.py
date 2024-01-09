class Student:
    def __init__(self,name,age):
        self.name = "Rohan"
        self.age = 20
    
    def print_student_details():
        print(self.name,end=" ")
        print(self.age)
    
s = Student("Parikh",25)
s.print_student_details()

#Error

'''
line 11, in <module>
    s.print_student_details()
TypeError: Student.print_student_details() takes 0 positional arguments but 1 was given
'''