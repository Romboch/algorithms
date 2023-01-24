from typing import Tuple, List


def transpose(n: int, m: int, matrix: List[List[int]]) -> List[List[int]]:
    return [[row[i] for row in matrix] for i in range(m)]


def read_input() -> Tuple[int, int, List[List[int]]]:
    n = int(input())
    m = int(input())
    matrix = [[]] * n
    for _ in range(n):
        matrix[_] = list(map(int, input().strip().split()))
    return n, m, matrix


matrix = transpose(*read_input())
for row in matrix:
    print(*row)
