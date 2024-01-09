class ZeroDenominatorError(Exception):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print('Zero Division Error Occured')

# Error - ZeroDenominatorError