def get_houses(budget, houses):
    houses = sorted(houses)

    t = 0
    while t < len(houses) and budget >= houses[t]:
        budget -= houses[t]
        t += 1
    return t


if __name__ == '__main__':
    budget = int(input().split()[1])
    costs = [int(_) for _ in input().split()]
    print(get_houses(
        budget,
        costs
    ))
