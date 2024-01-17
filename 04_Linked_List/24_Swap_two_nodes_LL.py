'''
Swap two Nodes of LL

You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions.
Note :
Remember, the nodes themselves must be swapped and not the datas.

No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains two integer values 'i,' and 'j,' respectively. A single space will separate them.
 Remember/consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.
0 <= i < M
0 <= j < M

Time Limit: 1sec
Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3 4
Sample Output 1 :
3 4 5 6 2 1 9 
 Sample Input 2 :
2
10 20 30 40 -1
1 2
70 80 90 25 65 85 90 -1
0 6
 Sample Output 2 :
10 30 20 40 
90 80 90 25 65 85 70 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    if i == j:
        return head

    prev_i = None
    curr_i = head
    count_i = 0
    while curr_i is not None and count_i < i:
        prev_i = curr_i
        curr_i = curr_i.next
        count_i += 1

    prev_j = None
    curr_j = head
    count_j = 0
    while curr_j is not None and count_j < j:
        prev_j = curr_j
        curr_j = curr_j.next
        count_j += 1

    if curr_i is None or curr_j is None:
        return head

    if prev_i is not None:
        prev_i.next = curr_j
    else:
        head = curr_j

    if prev_j is not None:
        prev_j.next = curr_i
    else:
        head = curr_i

    temp = curr_i.next
    curr_i.next = curr_j.next
    curr_j.next = temp

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

    # Input values for i and j
    i, j = map(int, input().split())

    # Swap nodes at positions i and j and print the new head
    new_head = swap_nodes(head, i, j)
    while new_head is not None:
        print(new_head.data, end=" ")
        new_head = new_head.next
    print()