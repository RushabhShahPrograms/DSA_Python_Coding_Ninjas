'''
Sum Of Nodes

For a given Binary Tree of integers, find and return the sum of all the nodes data.
Example:
                        10
                      /      \
                    20      30
                   /    \
                 40    50

When we sum up all the nodes data together, [10, 20, 30, 40 50] we get 150. Hence, the output will be 150.
 Input Format:
The first and the only line of input will contain the nodes data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
Output Format:
The first and the only line of output prints the sum of all the nodes data present in the binary tree.
Note:
You are not required to print anything explicitly. It has already been taken care of.
Constraints:
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec
Sample Input 1:
2 3 4 6 -1 -1 -1 -1 -1
Sample Output 1:
 15
Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output 2:
 28
'''

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

def build_tree(nodes):
    if len(nodes) == 0:
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue:
        current = queue.pop(0)
        if i<len(nodes) and nodes[i] != '-1':
            current.left = TreeNode(int(nodes[i]))
            queue.append(current.left)
        i += 1
        if i<len(nodes) and nodes[i] != '-1':
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

nodes_data = input().split()
root = build_tree(nodes_data)
print(sum_of_nodes(root))