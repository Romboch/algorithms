def arrange_plots(array):
    if len(array) == 1:
        return array
    left = arrange_plots(array[0: len(array) // 2])
    right = arrange_plots(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    # result = [[]] * len(array)
    result = []

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l][0] == right[r][0]:
            if left[l][1] >= right[r][1]:
                result.append(left[l])
            else:
                result.append(right[r])
            l += 1
            r += 1
        elif left[l][0] < right[r][0]:
            if left[l][1] >= right[r][0]:
                if left[l][1] <= right[r][1]:
                    result.append((left[l][0], right[r][1]))
                else:
                    result.append(left[l])
                l += 1
                r += 1
            else:
                result.append(left[l])
                l += 1
        elif left[l][0] > right[r][0]:
            if left[l][0] <= right[r][1]:
                if left[l][1] >= right[r][1]:
                    result.append((right[r][0], left[l][1]))
                else:
                    result.append(right[r])
                l += 1
                r += 1
            else:
                result.append(right[r])
                r += 1
        else:
            raise RuntimeError('Unexpected expression')
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result.append(left[l])  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1

    while r < len(right):
        result.append(right[r])  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result




def read_input():
    plots = []
    gardeners = int(input())
    for index in range(gardeners):
        plots.append(tuple(map(int, input().split())))
    return gardeners, plots


if __name__ == '__main__':
    gardeners, plots = read_input()
    print(gardeners)
    print(*plots)
    print(*(f'{value[0]} {value[1]}' for value in arrange_plots(plots)), sep='\n')
