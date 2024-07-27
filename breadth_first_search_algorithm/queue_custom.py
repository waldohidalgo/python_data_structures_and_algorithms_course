"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self,*args):
        self.items = deque(
            args
        )

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue('wore','a','silly','hat','the','aardvark')
    print(q)
    for i in range(4):
        q.enqueue(q.dequeue())
    print(q)
   

