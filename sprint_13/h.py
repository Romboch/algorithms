def get_bigger(first, second):
    return int(first + second) >= (int(second + first))

def sort_by_comparator(array, bigger):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and bigger(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


if __name__ == '__main__':
    n = int(input())
    list_ = input().split()
    sort_by_comparator(list_, get_bigger)
    print(''.join(list_))
