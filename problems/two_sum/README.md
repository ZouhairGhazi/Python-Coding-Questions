# Two Sum

Source: LeetCode: https://leetcode.com/problems/two-sum/description/

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach
- Use a hash map to store value → index
- For each element, check if `target - nums[i]` is in the map
- Time: O(n), Space: O(n)

## How to run
```bash
python solution.py
pytest test_solution.py