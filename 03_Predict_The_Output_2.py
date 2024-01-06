def printNumbers(n):
    if(n<0):
        return
    print(n,end=" ")
    printNumbers(n-2)
num=5
printNumbers(num)

# 5 3 1