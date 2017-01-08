class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, node):
        if self.head == None:
            self.head = node
        else:
            node.nextn = self.head
            self.head = node

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.nextn = self.head
            self.head = node

    def print_all(self):
        node = self.head
        while node.nextn != None:
            print(node.data, end=" ")
            node = node.nextn
        print(node.data)

class Node():
    def __init__(self, data=None, nextn=None):
        self.data = data
        self.nextn = nextn


if __name__ == "__main__":

    ll = LinkedList()
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_all()

