# Код успешной посылки - 80379620
def in_place_quick_sort(data):
    def partition(left, right):
        pivot = data[(left + right) // 2]
        while True:
            while data[left] < pivot:
                left += 1
            while pivot < data[right]:
                right -= 1
            if left >= right:
                return right
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    def quick_sort(left, right):
        if right == left:
            return
        pivot_position = partition(left, right)
        quick_sort(left, pivot_position)
        quick_sort(pivot_position + 1, right)

    quick_sort(0, len(data) - 1)
    return data


if __name__ == '__main__':
    class Competitor:
        def __init__(self, *input_):
            self.name: str = input_[0]
            self.score: int = int(input_[1])
            self.penalty: int = int(input_[2])

        def __str__(self):
            return str(self.score)

        def __lt__(self, other):
            return (
                    self.score > other.score or
                    (
                            self.score == other.score and
                            (
                                self.penalty < other.penalty or
                                self.penalty == other.penalty and
                                self.name < other.name
                            )
                    )
            )


    print(
        *(item for item in in_place_quick_sort([
            Competitor(
                *input().split()
            ) for _ in range(int(input()))
        ])),
        sep='\n'
    )
