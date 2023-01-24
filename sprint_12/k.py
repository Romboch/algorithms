def fib(n: int):
    if 0 <= n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def read_input():
    number = int(input())
    return str(fib(number))

def main():
    print(read_input())

if __name__ == '__main__':
    main()