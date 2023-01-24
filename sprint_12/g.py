class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return not len(self.items)

    def push(self, value):
        self.items.append(value)
        if not self.max:
            self.max.append(value)
        elif value >= self.max[-1]:
            self.max.append(value)

    def pop(self):
        if self.is_empty():
            print('error')
            item = 'error'
        else:
            item = self.items.pop()
            if item == self.max[-1]:
                self.max.pop()
        return item

    def get_max(self):
        if self.is_empty():
            result = 'None'
        else:
            result = self.max[-1]
        print(result)
        return result

def read_input():
    COMMANDS = dict(
        pop=StackMaxEffective.pop,
        push=StackMaxEffective.push,
        get_max=StackMaxEffective.get_max,
    )
    n = int(input())
    st = StackMaxEffective()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'pop':
            st.pop()
        if cmd[0] == 'push':
            st.push(int(cmd[1]))
        if cmd[0] == 'get_max':
            st.get_max()

def main():
    read_input()

if __name__ == '__main__':
    main()