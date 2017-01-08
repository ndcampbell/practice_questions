import linkedlinked

def loop_start(head):
    slow = head
    fast = head.nextn
    while slow =! None and fast != None:
        slow = slow.nextn
        fast = fast.nextn.nextn
        if fast is slow:
            break
    slow = head
    while slow is not fast:
        slow = slow.nextn
        fast = fast.nextn
    return slow
