import stackqueue

# Implement a min function for a stack that has 0(1) time.

#Idea: Use another stack

class MinStack(stackqueue.Stack):
    def __init__(self, head=None):
        super().__init__(head=head)
        self.minstack = stackqueue.Stack()

    def minnode(self):
        return self.minstack.head

    def push(self, data):
        node = stackqueue.Node(data)
        if self.head == None:
            self.head = node
        else:
            node.nextn = self.head
            self.head = node

        if self.minnode() == None:
            self.minstack.push(data)
        elif data < self.minnode().data:
            self.minstack.push(data)

    def pop(self):
        old = self.head
        self.head = self.head.nextn
        if old.data == self.minnode().data:
            self.minstack.pop()
        return old

if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(8)
    print(minstack.minnode().data)
    minstack.push(10)
    print(minstack.minnode().data)
    minstack.push(4)
    print(minstack.minnode().data)
    minstack.push(11)
    print(minstack.minnode().data)
    minstack.push(1)
    print(minstack.minnode().data)
    minstack.pop()
    print(minstack.minnode().data)
    minstack.pop()
    print(minstack.minnode().data)
    minstack.pop()


