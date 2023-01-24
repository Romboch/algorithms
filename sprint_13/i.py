def arrange_lovers(array):
    result = [0] * (max(array)+1)
    for i in array:
        result[i] += 1
    school = [(-result[i], i) for i in range(len(result))]
    return [item[1] for item in sorted(school)]


if __name__ == '__main__':
    input()
    lovers = [int(_) for _ in input().split()]
    print(*arrange_lovers(lovers)[:int(input())])
