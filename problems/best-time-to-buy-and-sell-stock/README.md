# Best Time to Buy and Sell Stock  

Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on day `i`.

Your goal is to maximize profit by choosing one day to buy and a later day to sell.

Return the maximum possible profit.  
If no profit can be made, return `0`.

## Approach

This problem can be solved efficiently with a single pass through the price list.

Track two values:

- `min_price`: the lowest price encountered so far (best day to buy)
- `max_profit`: the highest profit found so far

For each price:
1. Update `min_price` if the current price is lower.
2. Compute profit: `price - min_price`.
3. Update `max_profit` if this profit is greater.

This ensures an optimal time complexity.

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
