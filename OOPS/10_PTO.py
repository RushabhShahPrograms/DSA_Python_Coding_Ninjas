class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def print_student_details():
        print(self.__name,end = " ")
        print(self.age)

s.Student("Rohan",20)
print(s.name)

# Error

'''
line 11, in <module>
    s.print_student_details()
TypeError: Student.print_student_details() takes 0 positional arguments but 1 was given
'''