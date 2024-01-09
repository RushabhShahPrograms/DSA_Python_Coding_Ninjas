class Vehicle:
    def __init__(self,color):
        self.color = color
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
c = Car("black",5)
print(c.color)

# black