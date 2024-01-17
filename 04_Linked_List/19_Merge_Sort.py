'''
Code: Merge Sort

 Given a singly linked list of integers, sort it using 'Merge Sort.'
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

def merge_sort(head):
    if head is None or head.next is None:
        return head

    # Find the middle of the linked list
    mid = find_middle(head)

    # Split the linked list into two halves
    second_half = mid.next
    mid.next = None

    # Recursively sort the two halves
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(second_half)

    # Merge the sorted halves
    sorted_list = merge(left_sorted, right_sorted)

    return sorted_list

def find_middle(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    merged_head = None
    current = None

    while left is not None and right is not None:
        if left.data <= right.data:
            if merged_head is None:
                merged_head = left
                current = merged_head
            else:
                current.next = left
                current = current.next
            left = left.next
        else:
            if merged_head is None:
                merged_head = right
                current = merged_head
            else:
                current.next = right
                current = current.next
            right = right.next

    # If any list has remaining elements, append them
    if left is not None:
        if merged_head is None:
            merged_head = left
        else:
            current.next = left

    if right is not None:
        if merged_head is None:
            merged_head = right
        else:
            current.next = right

    return merged_head

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

    # Sort the linked list using merge sort
    sorted_head = merge_sort(head)

    # Print the resulting sorted list
    while sorted_head is not None:
        print(sorted_head.data, end=" ")
        sorted_head = sorted_head.next
    print()