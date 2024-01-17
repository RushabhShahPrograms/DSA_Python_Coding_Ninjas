'''
Delete every N nodes

You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= P <= 10^5
Where P is the size of the singly linked list.
0 <= M <= 10^5
0 <= N <= 10^5 

Time Limit: 1sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 -1
2 2
Sample Output 1 :
1 2 5 6
Sample Input 2 :
2
10 20 30 40 50 60 -1
0 1
1 2 3 4 5 6 7 8 -1
2 3
Sample Output 2 :
1 2 6 7
Explanation of Sample Input 2 :
For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_m_after_n(head, m, n):
    if head is None or m == 0:
        return None

    current = head

    while current is not None:
        # Traverse M nodes
        for _ in range(m - 1):
            if current is None:
                break
            current = current.next

        if current is None:
            break

        # Delete N nodes
        temp = current.next
        for _ in range(n):
            if temp is None:
                break
            temp = temp.next

        current.next = temp

        current = temp

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

    # Input values for M and N
    m, n = map(int, input().split())

    # Delete N nodes after every M nodes and print the new head
    new_head = delete_m_after_n(head, m, n)
    while new_head is not None:
        print(new_head.data, end=" ")
        new_head = new_head.next
    print()