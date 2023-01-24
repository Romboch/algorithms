# Код успешной отправки 79547518

class Deque:

    def __init__(self, limit):
        self.cells = [None] * limit
        self.limit = limit
        self.head = 0
        self.tail = 1
        self._size_ = 0

    def push_back(self, value):
        if self._size_ == self.limit:
            raise LookupError('push to full deque')
        self.cells[self.tail] = value
        self.tail = (self.tail + 1) % self.limit
        self._size_ += 1

    def push_front(self, value):
        if self._size_ == self.limit:
            raise LookupError('push to full deque')
        self.cells[self.head] = value
        self.head = (self.head - 1) % self.limit
        self._size_ += 1

    def pop_back(self):
        if not self._size_:
            raise IndexError('pop from an empty deque')
        self.tail = (self.tail - 1) % self.limit
        self._size_ -= 1
        return self.cells[self.tail]

    def pop_front(self):
        if not self._size_:
            raise IndexError('pop from an empty deque')
        self.head = (self.head + 1) % self.limit
        self._size_ -= 1
        return self.cells[self.head]


if __name__ == '__main__':
    number_of_commands = int(input())
    deque = Deque(int(input()))
    for _ in range(number_of_commands):
        command, *parameters = input().split()
        if not hasattr(deque, command):
            raise RuntimeError(f'Unknown command {command} in input data')
        try:
            result = getattr(deque, command)(*parameters)
            if result is not None:
                print(result)
        except (LookupError, IndexError):
            print('error')
