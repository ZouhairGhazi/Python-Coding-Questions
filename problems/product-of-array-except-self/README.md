# Product of Array Except Self

Source: https://leetcode.com/problems/product-of-array-except-self/

## Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.
Try doing it in O(1) extra space as well.

## Approach

- Make two passes, first in-order, second in-reverse, to compute products directly in the result array while ignoring current element

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (not counting the result array)
