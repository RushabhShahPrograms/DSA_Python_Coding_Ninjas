'''
You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).
 Note:
Change in the input array/list itself. You don't need to return or print the elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains the value of 'D' by which the array/list needs to be rotated.
Output Format :
For each test case, print the rotated array/list in a row separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^4
0 <= N <= 10^6
0 <= D <= N
Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2
Sample Input 2:
2
7
1 2 3 4 5 6 7
0
4
1 2 3 4
2
Sample Output 2:
1 2 3 4 5 6 7
3 4 1 2
'''
def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # To handle cases where d is greater than the size of the array

    # Rotate the array in-place using slicing
    arr[:] = arr[d:] + arr[:d]

# Input the number of test cases
t = int(input())

for _ in range(t):
    # Input size of the array
    n = int(input())

    # Input array elements
    array_elements = list(map(int, input().split()))

    # Input the value of 'D'
    d = int(input())

    # Rotate the array and print the result
    rotate_array(array_elements, d)
    print(*array_elements)
