'''
First Index of Number

The task is to find and return the first index of an integer x in an array of length N. If x is not present, return -1. This should be done recursively. Indexing in the array starts from 0.

The input format is as follows:

Line 1 contains an integer N (the size of array)
Line 2 contains N integers which are elements of the array separated by spaces
Line 3 contains integer x
The output format requires returning the first index or -1.

The constraints are given as (1 <= N <= 10^3).
'''

def first_index(arr, n, x):
    # Base case: If the array is empty, return -1
    if n == 0:
        return -1
    
    # If the current element is equal to x, return the current index
    if arr[0] == x:
        return 0
    
    # Recursive case: Check the rest of the array
    smaller_output = first_index(arr[1:], n - 1, x)
    
    # If the element is not present in the rest of the array, return -1
    if smaller_output == -1:
        return -1
    
    # Otherwise, return the index adjusted by 1 (since we reduced the array size)
    return smaller_output + 1

# Input: Size of the array
N = int(input())

# Input: Array elements
array_elements = list(map(int, input().split()))

# Input: Number to find
x = int(input())

# Checking if the size of the array matches the input length
if len(array_elements) == N:
    # Finding and printing the first index using the recursive function
    result = first_index(array_elements, N, x)
    print(result)
else:
    print("Please provide the correct number of array elements.")