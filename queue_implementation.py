import time
from collections import deque
from threading import Thread


class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        self.container.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            return self.container.pop()
        return

    def is_empty(self):
        return not len(self.container)

    def size(self):
        return len(self.container)

    def front(self):
        return self.container[-1]


food_order_queue = Queue()


def order_items(orders):
    for order in orders:
        print("Placing order: ", order)
        food_order_queue.enqueue(order)
        time.sleep(2)


def serve_items():
    while True:
        print("Serving order: ", food_order_queue.dequeue())
        time.sleep(0.5)


if __name__ == '__main__':
    # t1 = Thread(target=order_items, args=(['pizza', 'samosa', 'pasta', 'biryani', 'burger'],))
    # t2 = Thread(target=serve_items)
    #
    # t1.start()
    # t2.start()
    n = 10
    queue = Queue()
    queue.enqueue("1")
    for i in range(n):
        front = queue.front()
        print(front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")
        queue.dequeue()
