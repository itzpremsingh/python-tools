from typing import Any, Optional


class EmptyError(Exception):
    """Raised when stack or queue is empty."""

    pass


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class Stack:
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> Any:
        if self.is_empty():
            raise EmptyError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self) -> Any:
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self.top.data


class Queue:
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, data: Any) -> None:
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self) -> Any:
        if self.is_empty():
            raise EmptyError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self) -> Any:
        if self.is_empty():
            raise EmptyError("Queue is empty")
        return self.front.data


if __name__ == "__main__":
    # Stack
    s = Stack()
    s.push(10)
    s.push(20)
    print("Stack peek:", s.peek())
    print("Stack pop:", s.pop())

    # Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Queue peek:", q.peek())
    print("Queue dequeue:", q.dequeue())
