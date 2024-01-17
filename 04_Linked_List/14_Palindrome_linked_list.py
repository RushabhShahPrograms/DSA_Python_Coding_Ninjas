'''
Palindrome LinkedList

You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
 Output format :
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
9 2 3 3 2 9 -1
Sample Output 1 :
true
Sample Input 2 :
2
0 2 3 2 5 -1
-1
Sample Output 2 :
false
true
Explanation for the Sample Input 2 :
For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.

For the second query, the list is empty. An empty list is always a palindrome , hence the output is 'true'.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    # Function to reverse a linked list
    def reverse_list(node):
        prev = None
        current = node
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Function to compare two linked lists
    def compare_lists(list1, list2):
        while list1 is not None and list2 is not None:
            if list1.data != list2.data:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    if head is None or head.next is None:
        return True

    # Find the middle of the linked list
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half_head = reverse_list(slow.next)

    # Compare the first half and reversed second half
    result = compare_lists(head, second_half_head)

    # Restore the original linked list
    slow.next = reverse_list(second_half_head)

    return result

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
    # Take input for each test case
    head = take_input()

    # Check if the linked list is a palindrome
    result = is_palindrome(head)

    # Print the result
    print(result)