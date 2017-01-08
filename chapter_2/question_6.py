import linkedlist

#Now try it using a stack!


def is_palindrome(ll):
    head = ll.head
    newll = linkedlist.LinkedList()
    while head != None:
        data = head.data
        newll.insert(data)
        head = head.nextn

    head = ll.head
    newhead = newll.head
    while head != None:
        if head.data == newhead.data:
            head = head.nextn
            newhead = newhead.nextn
        else:
            print("Not a Palindrome")
            return False

    print("Is a Palindrome")
    return True


if __name__ == "__main__":
    ll = linkedlist.LinkedList()
    ll.insert('m')
    ll.insert('a')
    ll.insert('d')
    ll.insert('o')
    ll.insert('m')
    ll.print_all()
    is_palindrome(ll)

