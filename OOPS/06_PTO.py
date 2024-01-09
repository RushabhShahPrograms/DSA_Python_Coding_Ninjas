class Student:
    def __init__(self,name,age):
        self.name = "Rohan"
        self.age = 20

    def print_student_details():
        print(self.name,end = " ")
        print(self.age)

s = Student()
s.print_student_details()

# Error

'''
line 10, in <module>
    s = Student()
        ^^^^^^^^^
TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'age'
'''