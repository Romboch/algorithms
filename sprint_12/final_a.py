# Код успешной отправки 79396567
class Deck:
    class Node:
        def __init__(self, value=None, previous=None, next=None):
            self.value = value
            self.previous = previous
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self, limit):
        self.head = self.Node()
        self.tail = self.Node()
        self._size_ = 0
        self.limit = limit

    def push_back(self, value):
        if self._size_ == self.limit:
            return 'error'
        elif not self._size_:
            self.head = self.Node(value=value)
            self.tail = self.head
            self._size_ += 1
        else:
            self.tail.next = self.Node(value=value, previous=self.tail)
            self.tail = self.tail.next
            self._size_ += 1
        return self.tail

    def push_front(self, value):
        if self._size_ == self.limit:
            return 'error'
        elif not self._size_:
            self.head = self.Node(value=value)
            self.tail = self.head
            self._size_ += 1
        else:
            self.head.previous = self.Node(value=value, next=self.head)
            self.head = self.head.previous
            self._size_ += 1
        return self.head

    def pop_back(self):
        if not self._size_:
            return 'error'
        value = self.tail.value
        if self._size_ == 1:
            self.head = self.Node()
            self.tail = self.Node()
        else:
            self.tail = self.tail.previous
        self._size_ -= 1
        return value

    def pop_front(self):
        if not self._size_:
            return 'error'
        value = self.head.value
        if self._size_ == 1:
            self.head = self.Node()
            self.tail = self.Node()
        else:
            self.head = self.head.next
        self._size_ -= 1
        return value


def read_input():
    var_n = int(input())
    var_m = int(input())
    deck = Deck(var_m)
    for _ in range(var_n):
        cmd = input().split()
        if 0:
            pass
        elif cmd[0] == 'push_back':
            result = deck.push_back(int(cmd[1]))
            if type(result) == str:
                print(result)
        elif cmd[0] == 'push_front':
            result = deck.push_front(int(cmd[1]))
            if type(result) == str:
                print(result)
        elif cmd[0] == 'pop_back':
            print(deck.pop_back())
        elif cmd[0] == 'pop_front':
            print(deck.pop_front())
        else:
            print('Unknown command')


def main():
    read_input()


if __name__ == '__main__':
    main()
