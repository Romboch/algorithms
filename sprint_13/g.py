def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(k):
        for _ in range(counted_values[value]):
            array[index] = value
            index += 1


def read_input():
    total = int(input())
    things = list(map(int, input().split()))
    return total, things


if __name__ == '__main__':
    total, things = read_input()
    counting_sort(things, 3)
    print(*things)