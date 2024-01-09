class Vehicle:
    def __init__(self,color):
        self.color = color
    def print(self):
        print(c.color,end=" ")
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
    def print(self):
        self.print()
        print(c.numGears)
c = Car("black",5)
c.print()

# Recursion Error

'''
line 11, in print
    self.print()
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''