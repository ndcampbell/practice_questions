#given binary tree, create linkedlist of all depth levels


#assume I have a tree class and a linked list class

def ll_per_depth(node, depth, lls):
    if  node is None:
        return
    if not lls.get(depth):
        new_ll = LinkedList()
        lls[depth] = new_ll
    lls[depth].insert(node)
    ll_per_depth(node.left, depth+1,  lls)
    depth = ll_per_depth(node.right, depth+1,  lls)



