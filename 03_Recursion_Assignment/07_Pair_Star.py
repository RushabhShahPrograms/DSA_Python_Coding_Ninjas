'''
Pair star

Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a
'''

def pair_star(s):
    if len(s)<=1:
        return s
    
    if s[0] == s[1]:
        return s[0] + '*' + pair_star(s[1:])
    else:
        return s[0] + pair_star(s[1:])

S = input()

result = pair_star(S)
print(result)