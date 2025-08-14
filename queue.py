class QueueEmptyError(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data):
        newNode = Node(data)

        if not self._head:
            self._head = newNode
            self._tail = newNode

        else:
            self._tail.next = newNode
            self._tail = newNode

        self._size += 1

    def size(self):
        return self._size

    def dequeue(self):
        head = self._head
        if head:
            self._head = head.next
            head.next = None

            self._size -= 1
            return head.data

        raise StackEmptyError("Stack is empty")

    def peek(self):
        head = self._head
        if head:
            return head.data

        raise StackEmptyError("Stack is empty")

    def delete(self, toDelete):
        node = self._head
        lastNode: Node | None = None
        for _ in range(self._size):
            if node.data == toDelete:
                if lastNode:
                    lastNode.next = node.next
                else:
                    # if the toDelete is first value then we can not delete it
                    # we have to swap its next node and then delete the next node
                    temp = node.next
                    node.data = temp.data
                    node.next = temp.next
                self._size -= 1
                return True
            else:
                lastNode = node
                node = node.next
        return False
