from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fun1(self):
        print("function of class A called")

    @abstractmethod
    def fun2(self):
        pass

class B(A):
    def fun1(self):
        super().fun1()
    def fun2(self):
        print("function 2 called")

o = B()
o.fun1()

# function of class A called