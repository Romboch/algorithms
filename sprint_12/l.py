def fib(n):
    a = b = x = 1
    c = y = 0
    while n:
        if n % 2 == 0:
            (a, b, c) = (a * a + b * b,
                       a * b + b * c,
                       b * b + c * c)
            n /= 2
        else:
            (x, y) = (a * x + b * y,
                    b * x + c * y)
            n -= 1
    return y

def read_input():
    n, k = map(int, input().split())
    return str(fib(n+1) % 10 ** k)

def main():
    print(read_input())

if __name__ == '__main__':
    main()