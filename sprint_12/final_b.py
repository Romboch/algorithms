# Код успешной отправки 79398940
class StackMax:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return 'error' if self.is_empty() else self.items.pop()


def read_input():
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    stack = StackMax()
    data = input().split()
    for value in data:
        if value in operations:
            var_b = stack.pop()
            var_a = stack.pop()
            stack.push(operations.get(value)(var_a, var_b))
        else:
            stack.push(int(value))
    print(stack.pop())


def main():
    read_input()


if __name__ == '__main__':
    main()
