'''
kReverse

Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
Example :
Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5
 Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains a single integer depicting the value of 'k'.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.
0 <= k <= M

Time Limit:  1sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 9 10 -1
4
Sample Output 1 :
4 3 2 1 8 7 6 5 10 9
Sample Input 2 :
2
1 2 3 4 5 -1
0
10 20 30 40 -1
4
Sample Output 2 :
1 2 3 4 5 
40 30 20 10 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()


def reverse_linked_list(head, k):
    current = head
    previous = None
    count = 0

    while current is not None and count < k:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        count += 1

    if next_node is not None:
        head.next = reverse_linked_list(next_node, k)

    return previous


def user_defined_format(test_cases, linked_list_data, k):
    linked_list = None
    for data in linked_list_data[:-1]: # exclude the -1 at the end
        node = Node(data)
        node.next = linked_list
        linked_list = node

    result = reverse_linked_list(linked_list, k)
    print_linked_list(result)


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        linked_list_data = list(map(int, input().split()))
        k = int(input())
        user_defined_format(test_cases, linked_list_data, k)