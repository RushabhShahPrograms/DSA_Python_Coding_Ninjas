'''
Preorder Binary Tree

For a given Binary Tree of integers, print the pre-order traversal.
Input Format:
The first and the only line of input will contain the nodes data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
Output Format:
The only line of output prints the pre-order traversal of the given binary tree.
Constraints:
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec
 Sample Input 1:
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Ouptut 1:
5 6 2 3 9 10 
 Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Ouptut 2:
1 2 4 5 3 6 7 
'''
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def build_tree(nodes):
    if len(nodes) == 0:
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue:
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] != '-1':
            current.left = TreeNode(int(nodes[i]))
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] != '-1':
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root



nodes_data = input().split()
root = build_tree(nodes_data)
preorder_traversal(root)