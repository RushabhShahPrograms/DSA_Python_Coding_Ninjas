'''
Minimum bracket Reversal

For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.
Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
Input Format :
The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
The only line of output will print the number of reversals required to balance the whole expression. Prints -1, otherwise.
Note:
You don't have to print anything. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1sec
Sample Input 1:
{{{
Sample Output 1:
-1
Sample Input 2:
{{{{}}
Sample Output 2:
1
'''
def min_bracket_reversals(expression):
    n = len(expression)

    # Check if the length of the expression is odd (since even length is necessary for balance)
    if n % 2 != 0:
        return -1

    stack = []

    for char in expression:
        if char == '{':
            stack.append(char)
        else:
            # If '}' is encountered and the stack is not empty, pop the corresponding '{'
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)

    # The remaining elements in the stack will contain unbalanced brackets
    unbalanced_opening = 0
    unbalanced_closing = 0

    for char in stack:
        if char == '{':
            unbalanced_opening += 1
        else:
            unbalanced_closing += 1

    # The number of reversals required is half of the unbalanced brackets
    return (unbalanced_opening + 1) // 2 + (unbalanced_closing + 1) // 2

# Driver code
if __name__ == "__main__":
    expression = input()
    result = min_bracket_reversals(expression)
    print(result)