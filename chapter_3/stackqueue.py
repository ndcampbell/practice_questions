class Node():
    def __init__(self, data=None, nextn=None):
        self.data = data
        self.nextn = nextn

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    def peek(self):
        return self.head

    def is_empty(self):
        if  self.head == None:
            return True
        return False

    def print_all(self):
        node = self.head
        while node.nextn != None:
            print(node.data, end=" ")
            node = node.nextn
        print(node.data)

class Stack(LinkedList):
    def __init__(self, head=None):
        self.head = head

    def push(self, node):
        if self.head == None:
            self.head = node
        else:
            node.nextn = self.head
            self.head = node

    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.nextn = self.head
            self.head = node

    def pop(self):
        old = self.head
        if self.head != None:
            self.head = self.head.nextn
        return old

class Queue(LinkedList):
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def enqueue_node(self, node):
        if self.head == None:
            self.head = node
        elif self.tail == None:
            self.tail = node
            self.head.nextn = self.tail
        else:
            self.tail.nextn = node
            self.tail = node

    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        elif self.tail == None:
            self.tail = node
            self.head.nextn = self.tail
        else:
            self.tail.nextn = node
            self.tail = node

    def dequeue(self):
        old = self.head
        self.head = self.head.nextn
        return old

if __name__ == "__main__":

    print("-------Stack Example!----------")
    stack =  Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_all()
    print("peek: %d" % stack.peek().data)
    print("pop: %d" % stack.pop().data)
    stack.print_all()

    print("-------Queue Example!----------")
    queue =  Queue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print_all()
    print("peek: %d" % queue.peek().data)
    print("dequeue: %d" % queue.dequeue().data)
    queue.print_all()


