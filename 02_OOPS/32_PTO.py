class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 5
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print("Zero Division Error Occured",end=" ")
except ZeroDenominatorError:
    print("Zero Denominator Error Occured",end=" ")
else:
    print("else works")

# else works