def get_cookies(kids, cookies):
    kids = sorted(kids)
    cookies = sorted(cookies)

    k, c, t = 0, 0, 0
    while k < len(kids) and c < len(cookies):
        if kids[k] <= cookies[c]:
            k += 1
            c += 1
            t += 1
        else:
            c += 1
    return t


if __name__ == '__main__':
    input()
    kids = [int(_) for _ in input().split()]
    input()
    cookies = [int(_) for _ in input().split()]
    print(get_cookies(kids, cookies))
