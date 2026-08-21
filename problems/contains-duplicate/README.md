# Contains Duplicate

Source: https://leetcode.com/problems/contains-duplicate/description/

## Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Approach
- Use a hash map to store value → index
- For each element, check if `target - nums[i]` is in the map

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)