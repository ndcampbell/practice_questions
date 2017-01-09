import stackqueue

#Stack of plates

#now implement the ability to pop from a specific index

class SetOfStacks():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.stacks = [stackqueue.Stack()]
        self.i = 0
        self.cur_length = 0

    def push(self, data):
        if self.cur_length < self.maxsize:
            self.stacks[self.i].push(data)
            self.cur_length += 1
        else:
            newstack = stackqueue.Stack()
            newstack.push(data)
            self.stacks.append(newstack)
            self.cur_length = 1
            self.i += 1

    def pop(self):
        popped = self.stacks[self.i].pop()
        self.cur_length -= 1
        if self.cur_length == 0:
            del self.stacks[self.i]
            self.i -= 1
        return popped

    def print_all(self):
        for stack in self.stacks:
            print("New Stack")
            stack.print_all()


if __name__ == "__main__":
    sos = SetOfStacks(3)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    sos.push(4)
    sos.push(5)
    sos.push(6)
    sos.push(7)
    sos.push(8)
    sos.push(9)
    sos.print_all()
    sos.pop()
    sos.pop()
    sos.pop()
    sos.pop()
    sos.print_all()
    sos.push(5)
    sos.print_all()





