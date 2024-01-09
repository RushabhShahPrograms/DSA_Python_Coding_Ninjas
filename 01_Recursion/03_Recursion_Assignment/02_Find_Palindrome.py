'''
Check Palindrome (recursive)

Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false
'''

def is_palindrome(s):
    if len(s)<=1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

input_string = input()
result = is_palindrome(input_string)
print(result)