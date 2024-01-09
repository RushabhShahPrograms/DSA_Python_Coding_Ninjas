'''
Check Number in Array

Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
'true' or 'false'
Constraints :
1 <= N <= 10^3
Sample Input 1 :
3
9 8 10
8
Sample Output 1 :
true
Sample Input 2 :
3
9 8 10
2
Sample Output 2 :
false
'''

def is_number_present(arr, n, x):
    # Base case: If the array is empty, return False
    if n == 0:
        return False
    
    # If the current element is equal to x, return True
    if arr[n - 1] == x:
        return True
    
    # Recursive case: Check the rest of the array
    return is_number_present(arr, n - 1, x)

# Input: Size of the array
N = int(input())

# Input: Array elements
array_elements = list(map(int, input().split()))

# Input: Number to check
x = int(input())

# Checking if the size of the array matches the input length
if len(array_elements) == N:
    # Checking and printing if the number is present using the recursive function
    result = is_number_present(array_elements, N, x)
    print(result)
else:
    print("Please provide the correct number of array elements.")