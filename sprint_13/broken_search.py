# Код успешной посылки 80373417
def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        left_value = nums[left]
        if left_value == target:
            return left
        right_value = nums[right]
        if right_value == target:
            return right
        middle = (left + right) // 2
        middle_value = nums[middle]
        if middle_value == target:
            return middle
        if left_value <= middle_value:     # левая половина отсортирована
            if left_value < target < middle_value:
                right = middle - 1
            else:
                left = middle + 1
        else:   # правая половина отсортирована
            if middle_value < target < right_value:
                left = middle + 1
            else:
                right = middle - 1
    return -1
