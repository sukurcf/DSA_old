class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def print_linked_list(self):
        current = self.head
        st = ""
        while current:
            st += str(current.data) + " ---> "
            current = current.next
        print(st)

    def insert_at_index(self, index, data):
        previous = None
        current = self.head
        if index == 0:
            self.head = Node(data, self.head)
            return
        while index > 0:
            previous = current
            current = current.next
            index -= 1
        previous.next = Node(data, current)

    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            previous = None
            current = self.head
            while index > 0:
                previous = current
                current = current.next
                index -= 1
            previous.next = current.next

    def reverse_linked_list(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def print_middle(self):
        p1 = p2 = self.head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        print(p1.data)


ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(5)
ll.insert_at_index(1, 2)
ll.insert_at_index(1, 3)
ll.insert_at_index(2, 4)
ll.print_linked_list()
ll.print_middle()
