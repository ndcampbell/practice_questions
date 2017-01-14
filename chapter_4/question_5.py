#check if binary tree is BST

def is_bst(root, minv, maxv):
    if root == None:
        return
    if (minv != None and root.data <= minv):
       return False
    if (maxv != None and root.data > maxv):
        return False

    if not is_bst(root.left, root.data, maxv) or not is_bst(root.right, minv, root.data):
        return False
    return True
