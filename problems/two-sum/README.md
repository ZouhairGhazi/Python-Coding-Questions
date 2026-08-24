# Two Sum

Source: https://leetcode.com/problems/two-sum/description/

## Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Otherwise, return [-1]

## Approach

- Use a hash map to store value → index
- For each element, check if `target - nums[i]` is in the map

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)