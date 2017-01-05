# Remove Dups: remove dups from an unsorted linked list

#example of a node class
class Node():
    def __init__(self, nextn=None, value=None):
        self.nextn = nextn #next is a reserved word in python
        self.value = value

# O(n) time, O(n) space due to buffer
def remove_dups(n):
    prev = None
    dups = {}
    while n != None:
        if n.value in dups:
            prev.nextn = n.nextn
        else:
            dups[n.value] = 1
        prev = n

# O(n^2) time, O(1) space
def remove_dups_nobuffer(n):
    cur = n
    while cur != None:
        runner = cur
        while runner.nextn != None:
            if runner.nextn.value == cur.value:
                runner.nextn = runner.nextn.nextn
            else:
                runner = runner.nextn
        cur = cur.nextn
