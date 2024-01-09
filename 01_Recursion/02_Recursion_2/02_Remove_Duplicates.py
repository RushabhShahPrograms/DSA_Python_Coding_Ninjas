'''
Remove Duplicates Recursively

Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string
Sample Input 1 :
aabccba
Sample Output 1 :
abcba
Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz
'''

def remove_duplicates(s):
    # Base case: If the string is empty or has only one character, return the string as is
    if len(s) <= 1:
        return s
    
    # Recursive case:
    # If the first character is the same as the second one, skip it; otherwise, concatenate it with the result of the rest of the string
    if s[0] == s[1]:
        return remove_duplicates(s[1:])
    else:
        return s[0] + remove_duplicates(s[1:])

# Input: String
input_string = input()

# Calculating and printing the modified string with consecutive duplicates removed using the recursive function
result = remove_duplicates(input_string)
print(result)