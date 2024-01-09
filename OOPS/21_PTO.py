from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

o = A()
o.fun1()

# Error

'''
line 12, in <module>
    o = A()
        ^^^
TypeError: Can't instantiate abstract class A with abstract methods fun1, fun2
'''