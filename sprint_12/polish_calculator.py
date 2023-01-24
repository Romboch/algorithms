# Код успешной отправки 79547770
from operator import add, sub, mul, floordiv

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError('pop from an empty stack')


def polish_calculations(data, operations=OPERATIONS, stack=None, _type=int):
    stack = Stack() if stack is None else stack
    for value in data:
        if value in operations:
            second, first = stack.pop(), stack.pop()
            stack.push(operations[value](first, second))
        else:
            try:
                stack.push(_type(value))
            except ValueError:
                raise ValueError (
                    f'{value} is neither operation, nor number'
                )

    return stack.pop()


if __name__ == '__main__':
    print(polish_calculations(input().split()))
