import linkedlist

#Delete a node in the middle of a list. You only have access to that node


# Since you can not access head, you can just copy the value from the next node into current node and then delete next node.
def delete_middle(node):
    if node is None or node.nextn is None:
        return
    node.data = node.nextn.data
    node.nextn = node.nextn.nextn

if __name__ == "__main__":
    ll = linkedlist.LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_all()
    delete_middle(ll.head.nextn.nextn)
    ll.print_all()
