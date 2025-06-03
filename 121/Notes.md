# 121. Best Time to Buy and Sell Stock

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Examples
```python
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit possible since prices only decrease.
```

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Key Insight: Sliding Window Pattern

This problem is a **perfect example of the sliding window technique**, but with a twist - the window is **dynamic and conceptual** rather than fixed-size.

### The Sliding Window Intuition

```
Think of it as a "buy-sell window":
- Left pointer (implicit): Minimum price seen so far
- Right pointer (explicit): Current price we're considering selling at
- Window constraint: Can only sell AFTER buying (future day)
- Goal: Maximize profit within this constraint
```

### Why This is a Sliding Window Problem

| Sliding Window Element | Best Time to Buy/Sell Implementation |
|----------------------|-------------------------------------|
| **Left pointer** | `left_min` (minimum price seen so far) |
| **Right pointer** | Current `price` in iteration |
| **Window expansion** | Move right by iterating through prices |
| **Window contraction** | Update `left_min` when we find a lower price |
| **Window validation** | Always valid (can always sell after buying) |
| **Optimization goal** | Maximize `current_price - left_min` |

---

## Solution Analysis

### My Implementation
```python
def maxProfit(self, prices: List[int]) -> int:
    left_min = prices[0] if prices else 0
    max_profit = 0
    
    for price in prices:   
        # Update the minimum price seen so far (contract window)
        left_min = min(left_min, price)
        
        # Calculate profit if we sell at current price (expand window)
        profit = price - left_min
        
        # Update the maximum profit
        max_profit = max(max_profit, profit)
        
    return max_profit if max_profit > 0 else 0
```

### How the Sliding Window Works Here

```
prices = [7, 1, 5, 3, 6, 4]
         ↑  ↑  ↑  ↑  ↑  ↑
        Day 0 1  2  3  4  5

Step-by-step sliding window:
Day 0: left_min=7, price=7, profit=0, max_profit=0
Day 1: left_min=1, price=1, profit=0, max_profit=0  ← Window contracts
Day 2: left_min=1, price=5, profit=4, max_profit=4  ← Window expands
Day 3: left_min=1, price=3, profit=2, max_profit=4  ← Window stays
Day 4: left_min=1, price=6, profit=5, max_profit=5  ← Window expands
Day 5: left_min=1, price=4, profit=3, max_profit=5  ← Window stays
```

### Window Movement Logic

1. **Expand Window**: When `current_price > left_min`
   - Calculate potential profit
   - Update `max_profit` if better

2. **Contract Window**: When `current_price < left_min`
   - Update `left_min` to current price
   - Reset our "buy" point to get better future profits

3. **Maintain Window**: When `current_price == left_min`
   - No profit change, continue scanning

---

## Why This Works: The Greedy Insight

### The Core Principle
> **To maximize profit, always buy at the lowest price seen so far**

### Mathematical Proof
```
For any selling day i, optimal profit = prices[i] - min(prices[0...i])

Since we process left to right:
- min(prices[0...i]) is exactly our left_min at day i
- We consider selling at every day i
- We track the maximum profit across all possibilities
```

### Visual Understanding
```
Prices: [7, 1, 5, 3, 6, 4]
         
Buy at 7:  [X, -, 5-7=-2, 3-7=-4, 6-7=-1, 4-7=-3] → Max: -1
Buy at 1:  [-, X, 5-1=4,  3-1=2,  6-1=5,  4-1=3]  → Max: 5 ✓

Our algorithm automatically finds the optimal buy point (1) and 
considers all valid sell points after it.
```

---

## Alternative Approaches

### Approach 1: Brute Force
```python
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit
```
- **Time**: O(n²) - nested loops
- **Space**: O(1)

### Approach 2: Sliding Window (My Solution)
```python
# Implementation above
```
- **Time**: O(n) - single pass
- **Space**: O(1) - only variables

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute Force** | O(n²) | O(1) | Check all buy-sell pairs |
| **Sliding Window** | **O(n)** | **O(1)** | Single pass with running minimum |

---

## Pattern Recognition: When to Use This Approach

### This Sliding Window Variant Works When:
1. **One-pass optimization** problems
2. **Running minimum/maximum** tracking needed
3. **Future dependency** (can only sell after buying)
4. **Greedy choice** is optimal (lowest buy price)

### Similar Problems:
- **Maximum Subarray** (Kadane's algorithm)
- **Best Time to Buy and Sell Stock II** (multiple transactions)
- **Maximum difference** between elements in array

---

## Common Pitfalls

### Edge Case: All Decreasing Prices
```python
prices = [7, 6, 4, 3, 1]
# Should return 0, not negative profit

# Handle with:
return max_profit if max_profit > 0 else 0
# Or simply: return max_profit (since we start with max_profit = 0)
```

### Forgetting the Time Constraint
```python
# Wrong: Can sell before buying
for i in range(len(prices)):
    for j in range(len(prices)):  # j can be < i
        if prices[j] > prices[i]:
            profit = prices[j] - prices[i]

# Right: Can only sell after buying  
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):  # j > i
```

---

## Key Takeaways

### Sliding Window Insight
- **Not all sliding windows have explicit left/right pointers**
- **The "left" can be a running statistic** (like minimum seen so far)
- **Window size is variable** and determined by the optimal choice

### Problem-Solving Pattern
1. Identify the **constraint** (can only sell after buying)
2. Find the **greedy choice** (buy at minimum price)
3. Track the **running optimum** (maximum profit)
4. **Single pass** is sufficient when greedy choice is optimal

### Why This is Elegant
- **O(n) time complexity** with simple logic
- **Handles all edge cases** naturally
- **Generalizable pattern** to similar optimization problems
- **Space efficient** with only a few variables

The beauty lies in recognizing that we don't need to track actual buy/sell days - just the **running minimum price** and **maximum profit achieved so far**!
