'''
Reverse LL (Recursive)

Given a singly linked list of integers, reverse it using recursion and return the head to the modified list. You have to do this in O(N) time complexity where N is the size of the linked list.
 Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^4
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 -1
Sample Output 1 :
8 7 6 5 4 3 2 1
Sample Input 2 :
2
10 -1
10 20 30 40 50 -1
Sample Output 2 :
10 
50 40 30 20 10 
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head
    
    rest_reversed = reverse_linked_list_recursive(head.next)

    head.next.next = head
    head.next = None

    return rest_reversed

def take_input():
    elements = list(map(int, input().split()))
    head = None
    tail = None

    for data in elements:
        if data == -1:
            break

        new_node = Node(data)

        if head is None:
            head = new_node
            tail = head
        else:
            tail.next = new_node
            tail = new_node
    return head

t = int(input())

for _ in range(t):
    head = take_input()
    new_head = reverse_linked_list_recursive(head)

    while new_head is not None:
        print(new_head.data,end=" ")
        new_head = new_head.next
    print()