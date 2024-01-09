class Vehicle:
    def __init__(self,color):
        self.color = color
    
class Car(Vehicle):
    def __init__(self,color,numGears):
        self.numGears = numGears

c = Car("black",5)
print(c.color)

# Error

'''
line 10, in <module>
    print(c.color)
          ^^^^^^^
AttributeError: 'Car' object has no attribute 'color'
'''