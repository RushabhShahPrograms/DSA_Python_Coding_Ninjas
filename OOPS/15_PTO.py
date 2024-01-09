class Vehicle:
    def __init__(self,color):
        self.__color = color
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
    def printCar(self):
        print(c.__color,end=" ")
        print(c.numGears)

c = Car("black",5)
c.printCar()

# Error

'''
line 9, in printCar
    print(c.__color,end=" ")
          ^^^^^^^^^
AttributeError: 'Car' object has no attribute '_Car__color'
'''