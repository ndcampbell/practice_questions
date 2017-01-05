#Just code to practice BST traverals.

#visits left branch, then current node, then right branch. Visits nodes in ascending order
def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node)
    inOrder(node.right)

#visits current node first, before traversing. Root is always first node visited
def preOrder(node):
    if node == None:
        return
    print(node)
    preOrder(node.left)
    preOrder(node.right)

#post order visits current node after child node. root is always last node visited
def postOrder(node):
    if node == None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node)

# min-heap notes: complete binary tree, each node is smaller than its children. Root is the minimum element in the tree.
