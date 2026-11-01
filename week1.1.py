def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution
# Test cases
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]  → 2 + 7 = 9
print(two_sum([3, 2, 4], 6))  # [1, 2]  → 2 + 4 = 6
print(two_sum([3, 3], 6))  # [0, 1]  → 3 + 3 = 6
print(two_sum([1, 2, 3], 100))  # []