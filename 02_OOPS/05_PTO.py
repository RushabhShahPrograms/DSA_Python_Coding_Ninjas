class Student:
    name = "Parikh"
    def store_details(self):
        self.age = 60
    def print_age(self):
        print(self.age)

s = Student()
s.store_details()
s1 = Student()
s1.print_age()

# Error
'''
line 6, in print_age
    print(self.age)
          ^^^^^^^^
AttributeError: 'Student' object has no attribute 'age'
'''