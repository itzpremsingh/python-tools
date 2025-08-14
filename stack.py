class StackEmptyError(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, data, previous):
            self.data = data
            self.previous: Stack.Node | None = previous

    def __init__(self):
        self.top: Stack.Node | None = None
        self.size = 0

    def push(self, data):
        self.top = self.Node(data, self.top)
        self.size += 1

    def pop(self):
        if self.top:
            top = self.top
            self.top = top.previous
            self.size -= 1

            return top.data
        else:
            raise StackEmptyError()

    def peek(self):
        if self.top:
            return self.top.data
