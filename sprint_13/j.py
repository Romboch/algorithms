def buble_sort(list_):
    sort = 0
    for index in range(1, len(list_)):
        if list_[index - 1] > list_[index]:
            list_[index - 1], list_[index] = list_[index], list_[index - 1]
            sort += 1
    return sort, list_


if __name__ == '__main__':
    n = int(input())
    list_ = list(map(int, input().split()))
    sort, list_ = buble_sort(list_)
    if not sort:
        print(*list_)
    while sort:
        print(*list_)
        sort, list_ = buble_sort(list_)
