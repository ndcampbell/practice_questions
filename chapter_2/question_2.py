import linkedlist

# Return kth to last: implement an arguement to find kth to last element in singly linked list

#Uses a runner pointer that starts at k position from the front. When runner pointer (p2) is at the end of the list, p1 will be the kth value from the end
# O(n) time, O(1) space
def kth_last(head, k):
    p1 = head
    p2 = head

    for i in range(k):
        p2 = p2.nextn

    while p2 != None:
        p1 = p1.nextn
        p2 = p2.nextn
    return p1

#recursive attempt. O(n) time and O(n) space
knode = None
def recurs_k(node, k):
    global knode
    if node.nextn == None:
        return 0
    end = recurs_k(node.nextn, k)
    if end == k:
        knode = node

if __name__ == "__main__":
    ll = linkedlist.LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_all()
    foundnode = kth_last(ll.head, 2)
    print(foundnode.data)
