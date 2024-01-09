class Vehicle:
    def __init__(self,color):
        self.color = color
    def print(self):
        print(c.color,end = " ")
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
    def print(self):
        print(c.color,end = " ")
        print(c.numGears)
c = Car("black",5)
c.print()

# black 5