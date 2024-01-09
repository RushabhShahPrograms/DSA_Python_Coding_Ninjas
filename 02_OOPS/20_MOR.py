# Method Resolution Order of C

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class C(B,A,Y): pass

# C>B>Z>A>X>Y