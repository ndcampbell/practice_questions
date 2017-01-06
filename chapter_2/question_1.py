import linkedlist

# Remove Dups: remove dups from an unsorted linked list

# O(n) time, O(n) space due to buffer
# logic: Keep track of dups in a dict and delete if > 1
def remove_dups(n):
    prev = None
    dups = {}
    while n != None:
        if n.data in dups:
            if n.nextn != None:
                prev.nextn = n.nextn
            else:
                prev.nextn = None
        else:
            dups[n.data] = 1
        prev = n
        n = n.nextn

# O(n^2) time, O(1) space
def remove_dups_nobuffer(n):
    while n != None:
        runner = n
        while runner.nextn != None:
            if runner.nextn.data == n.data:
                runner.nextn = runner.nextn.nextn
            else:
                runner = runner.nextn
        n = n.nextn

if __name__ == "__main__":
    ll = linkedlist.LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    ll.print_all()
    remove_dups_nobuffer(ll.head)
    ll.print_all()
