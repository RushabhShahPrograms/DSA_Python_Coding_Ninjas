'''
Even after Odd LinkedList

For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format:
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space. 
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format:
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
1 4 5 2 -1
Sample Output 1 :
1 5 4 2 
Sample Input 2 :
2
1 11 3 6 8 0 9 -1
10 20 30 40 -1
Sample Output 2 :
1 11 3 9 6 8 0
10 20 30 40
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    if head is None or head.next is None:
        return head

    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None

    current = head

    while current is not None:
        if current.data % 2 != 0:  # odd
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        else:  # even
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current

        current = current.next

    if odd_tail is not None:
        odd_tail.next = even_head

    if even_tail is not None:
        even_tail.next = None

    return odd_head if odd_head is not None else even_head

# Function to take input for linked list
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

# Input the number of test cases
t = int(input())

for _ in range(t):
    # Take input for each linked list
    head = take_input()

    # Rearrange the elements and print the new head
    new_head = even_after_odd(head)
    while new_head is not None:
        print(new_head.data, end=" ")
        new_head = new_head.next
    print()