'''
Remove X

Given a string, compute recursively a new string where all 'x' chars have been removed.
Input format :
String S
Output format :
Modified String
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string S. 
Sample Input 1 :
xaxb
Sample Output 1:
ab
Sample Input 2 :
abc
Sample Output 2:
abc
Sample Input 3 :
xx
Sample Output 3:

'''

def remove_x(s):
    # Base case: If the string is empty, return an empty string
    if not s:
        return ""

    # Recursive case:
    # If the first character is 'x', skip it; otherwise, concatenate it with the result of the rest of the string
    if s[0] == 'x':
        return remove_x(s[1:])
    else:
        return s[0] + remove_x(s[1:])

# Input: String
input_string = input()

# Calculating and printing the modified string using the recursive function
result = remove_x(input_string)
print(result)