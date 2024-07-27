import heapq


class PriorityQueue:

    def __init__(self):
        self.elements = []
    def is_empty(self):
        return not self.elements
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
    def peek(self):
        return self.elements[0][1]
    def __str__(self):
        return str(self.elements)
    
if __name__ == "__main__":
    # queue = PriorityQueue()
    # queue.put("foo", 1)
    # queue.put("bar", 5)
    # queue.put("spam", 4)
    # queue.put("grok", 1)
    # print(queue)
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())

    def process_tasks(tasks):
        # Create a priority queue
        pq=PriorityQueue()
        # Iterate through the tasks
        for task, priority in tasks:
            # Add each task to the priority queue along with its priority value
            pq.put(task,priority)
        # Use the "accumulator pattern."
        # Start with an "empty bucket" of the right data type (list in this case)
        # and build the solution by filling the bucket within a loop.
        ordered_task_list = []
        while not pq.is_empty():
            ordered_task_list.append(pq.get())

        # Use a while loop with the exit condition that the priority queue is empty.
        # Within this loop, update result with items got from the priority queue.


        return ordered_task_list

    tasks = [("drink", 2), ("eat", 1), ("be merry", 3)]
    result = process_tasks(tasks)
    print(result)