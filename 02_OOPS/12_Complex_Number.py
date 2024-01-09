'''
Complex Number

A ComplexNumber class contains two data members : one is the real part (R) and the other is imaginary (I) (both integers).
Implement the Complex numbers class that contains following functions -
1. constructor
You need to create the appropriate constructor.
2. plus -
This function adds two given complex numbers and updates the first complex number.
e.g.
if C1 = 4 + i5 and C2 = 3 +i1
C1.plus(C2) results in: 
C1 = 7 + i6 and C2 = 3 + i1
3. multiply -
This function multiplies two given complex numbers and updates the first complex number.
e.g.
if C1 = 4 + i5 and C2 = 1 + i2
C1.multiply(C2) results in: 
C1 = -6 + i13 and C2 = 1 + i2
4. print -
This function prints the given complex number in the following format :
a + ib
Note : There is space before and after '+' (plus sign) and no space between 'i' (iota symbol) and b.
Input Format :
Line 1 : Two integers - real and imaginary part of 1st complex number
Line 2 : Two integers - real and imaginary part of 2nd complex number
Line 3 : An integer representing choice (1 or 2) (1 represents plus function will be called and 2 represents multiply function will be called)
Output format :
Check details of 'print' function given above.
Sample Input 1 :
4 5
6 7
1
Sample Output 1 :
10 + i12
Sample Input 2 :
4 5
6 7
2
Sample Output 2 :
-11 + i58
'''

class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def plus(self, other):
        self.real += other.real
        self.imaginary += other.imaginary

    def multiply(self, other):
        temp_real = (self.real * other.real) - (self.imaginary * other.imaginary)
        temp_imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        self.real = temp_real
        self.imaginary = temp_imaginary

    def print_complex_number(self):
        print(f"{self.real} + i{self.imaginary}")

# Input
real1, imaginary1 = map(int, input().split())
real2, imaginary2 = map(int, input().split())
choice = int(input())

# Creating ComplexNumber objects
complex_number1 = ComplexNumber(real1, imaginary1)
complex_number2 = ComplexNumber(real2, imaginary2)

# Performing the operation based on choice
if choice == 1:
    complex_number1.plus(complex_number2)
elif choice == 2:
    complex_number1.multiply(complex_number2)

# Output
complex_number1.print_complex_number()