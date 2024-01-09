'''
String to Integer

Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
Input format :
Numeric string S (string, Eg. "1234")
Output format :
Corresponding integer N (int, Eg. 1234)
Constraints :
0 <= |S| <= 9
where |S| represents length of string S.
Sample Input 1 :
00001231
Sample Output 1 :
1231
Sample Input 2 :
12567
Sample Output 2 :
12567
'''

def string_to_integer(s):
    if not s:
        return 0
    
    return int(s[0]) * 10 ** (len(s)-1) + string_to_integer(s[1:])

S = input()

result = string_to_integer(S)
print(result)