# Binary Tree node

1. A node in Binary Trees can have how many children?

Ans. **0 or 1 or 2**

# Input Binary Tree

2. Consider the below code

```python
def takeInput():
    print("Enter root data")
    rootData = int(input())
    if(rootData == -1){
        return None
    }
    root = BinaryTreeNode(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root
```

What will be the input (excluding -1) to above code to construct this tree?

Ans. **2 7 2 6 5 11 5 9 4**

# Binary Tree Levelwise

3. Print given tree level wise

0: 1,2
1: 3,4
2: 5,6
3: 7,8
4: 9,10
5: 11,12
6: 13,14
7:
8:
9:
10:
11:
12:
13:
14:

Ans. **0 1 2 3 4 5 6 7 8 9 10 11 12 13 14**

# Height of Tree

4. The maximum and minimum number of nodes in a binary tree of height 6 are

A tree with zero node has height 0 A tree with one node has height 1

Ans. **63 and 6, respectively**