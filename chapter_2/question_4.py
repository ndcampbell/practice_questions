import linkedlist

def partition_list(head, partition):
    node = head
    while  node.nextn != None:
        print(node.nextn.data)
        if node.nextn.data < partition:
            curnode = node.nextn
            if curnode.nextn != None:
                node.nextn = node.nextn.nextn
            curnode.nextn = head
        node = node.nextn


if __name__ == "__main__":
    ll = linkedlist.LinkedList()
#    ll.insert(2)
    ll.insert(10)
    ll.insert(1)
    ll.insert(4)
    ll.insert(12)
    ll.insert(6)
    ll.print_all()

    partition_list(ll.head, 7)
    ll.print_all()

