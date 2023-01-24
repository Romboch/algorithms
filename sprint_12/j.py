class Queue:

    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self._size_ = 0

    def put(self, value):
        if not self._size_:
            self.head = self.Node(value=value)
            self.tail = self.head
            self._size_ += 1
        else:
            self.tail.next = self.Node(value=value)
            self.tail = self.tail.next
            self._size_ += 1
        return self.head

    def get(self):
        if not self._size_:
            return 'error'
        elif self._size_ == 1:
            value = self.head.value
            self.head = self.Node()
            self.tail = self.Node()
            self._size_ -= 1
            return value
        value = self.head.value
        self.head = self.head.next
        self._size_ -= 1
        return value

    def size(self):
        return self._size_

def read_input():
    n = int(input())
    queue = Queue()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'put':
            queue.put(int(cmd[1]))
        if cmd[0] == 'get':
            print(queue.get())
        if cmd[0] == 'size':
            print(queue.size())

def main():
    read_input()

if __name__ == '__main__':
    main()