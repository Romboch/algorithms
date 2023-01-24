def arrange_plots(array, start, end):
    if end - start <= 1:
        return [array[start]]
    left = arrange_plots(array, start, (start + end) // 2)
    right = arrange_plots(array, (start + end) // 2, end)
    # заводим массив для результата сортировки
    result = [()] * (end - start)
    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l][0] <= right[r][0]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1

    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


def combine_plots(array):
    start, end = array[0]
    result = []
    for index in range(0, len(array)):
        if array[index][0] > end:
            result.append((start, end))
            start, end = array[index]
        elif array[index][1] > end:
            end = array[index][1]
    result.append((start, end))
    array = arrange_plots(result)
    start, end = array[0]
    result = []
    for index in range(0, len(array)):
        if array[index][0] > end:
            result.append((start, end))
            start, end = array[index]
        elif array[index][1] > end:
            end = array[index][1]
    result.append((start, end))
    return result

def read_input():
    gardeners = int(input())
    plots = [()] * gardeners
    for index in range(gardeners):
        plots[index] = [*(int(i) for i in input().split())]
    return gardeners, plots


if __name__ == '__main__':
    gardeners, plots = read_input()
    print(*(f'{value[0]} {value[1]}' for value in combine_plots(plots)), sep='\n')
