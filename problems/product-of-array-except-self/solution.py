from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    prod_nums = [0] * n

    prefix = 1
    for i in range(n):
        prod_nums[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        prod_nums[i] *= suffix
        suffix *= nums[i]

    return prod_nums
