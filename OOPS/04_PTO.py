class Student:
    name = "Parikh"
    def store_details(self):
        self.age = 60
    def print_details(self):
        print(self.name, end=" ")
        print(self.age)

s = Student()
s.store_details()
s.print_details()

# Parikh 60