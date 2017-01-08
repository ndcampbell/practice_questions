import linkedlist

def sumlist_recursive(head1, head2, newlist, carry):
    val = carry
    if head1 != None:
        val += head1.data
    if head2 != None:
        val += head2.data

    if val >= 10:
        digit =  val % 10
        carry = 1
    else:
        digit = val
        carry = 0
    if head1 == None and head2 ==None:
        pass
    elif head1.nextn != None and head2.nextn != None:
        sumlist_recursive(head1.nextn, head2.nextn, newlist, carry)
    elif head1.nextn == None and head2.nextn == None and carry != 0:
        sumlist_recursive(None, None, newlist, carry)


    newlist.insert(digit)

if __name__ == "__main__":
    ll1 = linkedlist.LinkedList()
    ll2 = linkedlist.LinkedList()
    ll1.insert(8)
    ll1.insert(1)
    ll1.insert(7)
    ll1.print_all()
    ll2.insert(2)
    ll2.insert(9)
    ll2.insert(5)
    ll2.print_all()
    newll = linkedlist.LinkedList()
    sumlist_recursive(ll1.head, ll2.head, newll, 0)
    newll.print_all()


