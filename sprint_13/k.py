def merge(arr, lf, mid, rg):
    result = [0] * (rg - lf)
    l, r, k = lf, mid, 0
    while l < mid and r < rg:
        if arr[l] <= arr[r]:
            result[k] = arr[l]
            l += 1
        else:
            result[k] = arr[r]
            r += 1
        k += 1
    while l < mid:
        result[k] = arr[l]
        l += 1
        k += 1

    while r < rg:
        result[k] = arr[r]
        r += 1
        k += 1
    return result


def merge_sort(arr, lf, rg):
    mid = lf + (rg - lf) // 2
    if rg - lf <= 1:
        return
    elif rg - lf == 2:
        arr[lf:rg] = merge(arr, lf, mid, rg)
        return
    else:
        mid = lf + (rg - lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)



def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [4, 1, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
