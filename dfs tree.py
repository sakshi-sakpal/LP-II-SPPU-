# Tree Node definition using class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# DFS function to traverse the tree
def dfs_tree(node):
    if node is None:
        return
    
    print(node.value, end=' ')  # Process current node

    for child in node.children:
        dfs_tree(child)  # Recursively visit children

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

# Run DFS on tree
print("DFS traversal of the tree:")
dfs_tree(root)
