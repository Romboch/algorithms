class StackMax:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print('error')
        return 'error' if self.is_empty() else self.items.pop()

    def get_max(self):
        if self.is_empty():
            result = 'None'
        else:
            result = max(self.items)
        print(result)
        return result

def read_input():
    n = int(input())
    st = StackMax()
    for _ in range(n):
        _str = input().strip().split()
        if len(_str) == 1:
            command = 'st.' + _str[0] + '()'
        elif len(_str) == 2:
            command = 'st.' + _str[0] + f'({_str[1]})'
        exec(command)
    return n, _str

def main():
    read_input()

if __name__ == '__main__':
    main()