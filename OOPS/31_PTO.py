class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print("Zero Division Error Occured",end=" ")
except ZeroDenominatorError:
    print("Zero Denominator Error Occured",end=" ")
else:
    print("else works")

# Zero Division Error Occured