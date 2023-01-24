class MyQueueSized:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.max_size = capacity
        self._size = 0
        self.head = 0
        self.tail = 0

    def push(self, value):
        if self._size == self.max_size:
            print('error')
        else:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self._size += 1

    def pop(self):
        if not self._size:
            print('None')
        else:
            print(self.items[self.head])
            self.head = (self.head + 1) % self.max_size
            self._size -= 1

    def peek(self):
        if not self._size:
            print('None')
        else:
            print(self.items[self.head])

    def size(self):
        print(self._size)

def read_input():
    n_op = int(input())
    size = int(input())
    mqs = MyQueueSized(size)
    for _ in range(n_op):
        cmd = input().split()
        if cmd[0] == 'pop':
            mqs.pop()
        elif cmd[0] == 'push':
            mqs.push(int(cmd[1]))
        elif cmd[0] == 'peek':
            mqs.peek()
        elif cmd[0] == 'size':
            mqs.size()

def main():
    read_input()

if __name__ == '__main__':
    main()