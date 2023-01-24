def get_day(sums, cost) -> int:
    if sums[-1] < cost:
        return -1
    elif len(sums) == 1 and sums[0] >= cost:
        return 1

    mid = len(sums) // 2 + len(sums) % 2
    if sums[mid - 1] < cost:
        return mid + get_day(sums[mid:], cost)
    else:
        return get_day(sums[:mid], cost)


def read_input():
    days = int(input())
    sums = list(map(int, input().split()))
    cost = int(input())
    return days, sums, cost


if __name__ == '__main__':
    days, sums, cost = read_input()
    print(get_day(sums, cost), get_day(sums, cost * 2))
