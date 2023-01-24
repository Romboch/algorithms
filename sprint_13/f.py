def get_max_p(edges):
    edges.sort(reverse=True)
    maximum = []
    a, b, c = 0, 1, 2
    while edges[a] >= edges[b] + edges[c] and a < len(edges) - 3:
        a += 1
        b += 1
        c += 1
    maximum = edges[a] + edges[b] + edges[c]

    return maximum



if __name__ == '__main__':
    input()
    edges = [int(_) for _ in input().split()]
    print(get_max_p(
        edges
    ))
