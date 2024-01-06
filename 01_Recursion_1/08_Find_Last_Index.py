'''
Last Index Of Number Question

Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
last index or -1
Constraints :
1 <= N <= 10^3
Sample Input :
4
9 8 10 8
8
Sample Output :
3
'''
def last_index(arr, n, x):
    # Base case: If the array is empty, return -1
    if n == 0:
        return -1
    
    # Recursive case: Check the rest of the array
    smaller_output = last_index(arr[1:], n - 1, x)
    
    # If the element is present in the rest of the array, return the adjusted index
    if smaller_output != -1:
        return smaller_output + 1
    
    # If the current element is equal to x, return 0
    if arr[0] == x:
        return 0
    
    # Otherwise, return -1
    return -1

# Input: Size of the array
N = int(input())

# Input: Array elements
array_elements = list(map(int, input().split()))

# Input: Number to find
x = int(input())

# Checking if the size of the array matches the input length
if len(array_elements) == N:
    # Finding and printing the last index using the recursive function
    result = last_index(array_elements, N, x)
    print(result)
else:
    print("Please provide the correct number of array elements.")