try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ValueError:
    print("Exception occured")

# ZeroDivisionError
    
'''
line 4, in <module>
    c = a/b
        ~^~
ZeroDivisionError: division by zero
'''