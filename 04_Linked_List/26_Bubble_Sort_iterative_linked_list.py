'''
Bubble Sort (Iterative) LinkedList

Given a singly linked list of integers, sort it using 'Bubble Sort.'
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
10 9 8 7 6 5 4 3 -1
Sample Output 1 :
 3 4 5 6 7 8 9 10 
 Sample Output 2 :
2
-1
10 -5 9 90 5 67 1 89 -1
Sample Output 2 :
-5 1 5 9 10 67 89 90 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linkedlist(head):
    if head is None or head.next is None:
        return head

    # Get the length of the linked list
    length = 0
    temp = head
    while temp is not None:
        length += 1
        temp = temp.next

    # Perform Bubble Sort
    for i in range(length - 1):
        current = head
        prev = None

        for j in range(length - i - 1):
            next_node = current.next

            if current.data > next_node.data:
                if prev is None:
                    head = next_node
                else:
                    prev.next = next_node

                current.next = next_node.next
                next_node.next = current

                current, next_node = next_node, current

            prev = current
            current = current.next

    return head

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

    # Sort the linked list using Bubble Sort
    new_head = bubble_sort_linkedlist(head)

    # Print the sorted linked list
    while new_head is not None:
        print(new_head.data, end=" ")
        new_head = new_head.next
    print()