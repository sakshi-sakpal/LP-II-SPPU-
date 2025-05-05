from collections import deque

# Tree Node definition
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# BFS function for a tree
def bfs_tree(root):
    if root is None:
        return

    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        print(current.value, end=' ')
        
        for child in current.children:
            queue.append(child)

# Build a sample tree
#         A
#       / | \
#      B  C  D
#        / \
#       E   F

root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

root.children.extend([b, c, d])
c.children.extend([e, f])

# Run BFS on tree
print("BFS traversal of the tree:")
bfs_tree(root)
