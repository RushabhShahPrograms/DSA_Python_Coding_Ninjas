'''
Sum Of Array

Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :
Sum

Constraints :
1 <= N <= 10^3

Sample Input 1 :
3
9 8 9

Sample Output 1 :
26

Sample Input 2 :
3
4 2 1

Sample Output 2 :
7
'''

def sum_of_array(arr, n):
    # Base case: If the array is empty, return 0
    if n == 0:
        return 0
    
    # Recursive case: Sum the current element with the sum of the rest of the array
    return arr[n - 1] + sum_of_array(arr, n - 1)

# Input: Size of the array
N = int(input())

# Input: Array elements
array_elements = list(map(int, input().split()))

# Checking if the size of the array matches the input length
if len(array_elements) == N:
    # Calculating and printing the sum using the recursive function
    result = sum_of_array(array_elements, N)
    print(result)
else:
    print("Please provide the correct number of array elements.")
