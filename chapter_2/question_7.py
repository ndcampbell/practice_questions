import linkedlist

def get_intersection(head1, head2):
    len1 = 0
    len2 = 0
    tmp1 = head1
    tmp2 = head2
    while head1 != None and head2 != None:
        if head1 != None:
            if head1.nextn == None:
                head1last = head1
            len1 += 1
            head1 = head1.nextn
            print(head1)
        if head2 != None:
            if head2.nextn == None:
                head2last = head2
            len2 += 1
            head2 = head2.nextn
            print(head2)
    if head2last is not head1last:
        return False
    lendif = len1 - len2
    if lendif < 0:
        biggest = tmp2
        smallest = tmp1
    else:
        biggest = tmp1
        smallest = tmp2

    headstart = 0
    smalli = 0
    while biggest != None and smallest !=None:
        if headstart < abs(lendif):
            headstart += 1
            biggest = biggest.nextn
        else:
            if biggest is smallest:
                return headstart, smalli
            headstart += 1
            smalli += 1
            biggest = biggest.nextn
            smallest = smallest.nextn


if __name__ == "__main__":
    ll1 = linkedlist.LinkedList()
    ll2 = linkedlist.LinkedList()
    shared_node = linkedlist.Node(data=9)
    ll1.insert(1)
    ll1.insert(8)
    ll1.insert_node(shared_node)
    ll1.insert(4)
    ll1.insert(4)
    ll2.insert(2)
    ll2.insert_node(shared_node)
    ll2.insert(3)
    ll1.print_all()
    ll2.print_all()
    print(get_intersection(ll1.head, ll2.head))

