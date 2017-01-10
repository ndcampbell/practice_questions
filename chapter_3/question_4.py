import stackqueue
# Implement a queue using two stacks

class MyQueue():
    def __init__(self):
        self.normstack = stackqueue.Stack()
        self.revstack = stackqueue.Stack()

    def insert(self, data):
        self.normstack.push(data)

    def pop(self):
        if self.revstack.head == None:
            while self.normstack.head != None:
                curnode = self.normstack.pop()
                self.revstack.push(curnode.data)
        return self.revstack.pop()

if __name__ == "__main__":
    myqueue = MyQueue()
    myqueue.insert(1)
    myqueue.insert(2)
    myqueue.insert(3)
    myqueue.insert(4)
    myqueue.normstack.print_all()
    print(myqueue.pop().data)
    print(myqueue.pop().data)
    print(myqueue.pop().data)
    myqueue.revstack.print_all()
    myqueue.insert(5)
    myqueue.insert(5)
    myqueue.insert(5)
    myqueue.normstack.print_all()

