class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)


if __name__ == "__main__":

    def reverse_string(my_string):
        # Use the "accumulator pattern."
        # Start with an "empty bucket" of the right data type,
        # and build the solution by filling the bucket within a loop.
        reversed_string = ""

        # Create a new stack
        s = Stack()
        for i in range(len(my_string)):
            s.push(my_string[i])
        while not s.is_empty():
            reversed_string += s.pop()

        # Iterate through my_string and push the characters onto the stack

        # Use a while loop with the exit condition that the stack is empty.
        # Within this loop, update reversed_string with characters popped off the stack.

        # Return the result
        return reversed_string
    test_string = "gninraeL nIdekniL htiw tol a nraeL"
    result = reverse_string(test_string)
    print(result)