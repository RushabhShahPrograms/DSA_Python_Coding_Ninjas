'''
Staircase

A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13
'''

def staircase(n):
    # Create an array to store the number of ways for each step
    ways = [0] * (n + 1)

    # There is one way to climb zero steps (i.e., not climb at all)
    ways[0] = 1

    # There is one way to climb one step
    if n >= 1:
        ways[1] = 1

    # There are two ways to climb two steps (i.e., one step twice or two steps at once)
    if n >= 2:
        ways[2] = 2

    # For three or more steps, the number of ways is the sum of the number of ways for the previous three steps
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[n]

# Input: Number of steps N
N = int(input())

# Calculating and printing the number of possible ways using the recursive function
result = staircase(N)
print(result)