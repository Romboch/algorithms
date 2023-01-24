def broken_search(nums, target) -> int:
    left, middle, right = 0, len(nums) // 2, len(nums) - 1
    if len(nums) == 1:
        return 0 if nums[left] == target else -1
    elif nums[middle] == target:
        return middle
    elif nums[left] < nums[middle]:     # левая половина отсортирована
        if nums[left] <= target < nums[middle]:
            return broken_search(nums[:middle], target)
        else:
            result = broken_search(nums[middle:], target)
            return middle + result if result != -1 else -1
    elif nums[middle] < nums[right]:   # правая половина отсортирована
        if nums[middle] < target <= nums[right]:
            result = broken_search(nums[middle:], target)
            return middle + result if result != -1 else -1
        else:
            return broken_search(nums[:middle], target)


def test():
    _ = input()
    x = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, x))

test()