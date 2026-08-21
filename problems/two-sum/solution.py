from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if num in nums_map:
            return [nums_map[num], i]
        nums_map[target - num] = i
    return [-1]
