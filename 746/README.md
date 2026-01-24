# [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Problem Statement
You are given an integer array `cost` where `cost[i]` is the cost of the i-th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

**Example 1:**
```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**
```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

## Connection to Problem 70

> **This is essentially [Problem 70: Climbing Stairs](../70/README.md) but with costs!** Instead of counting ways, we track the minimum cost to reach each step.

### Key Difference:
- **Problem 70**: Count number of ways → `dp[i] = dp[i-1] + dp[i-2]`
- **Problem 746**: Find minimum cost → `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`

## My Solution

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1): 
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
```

## Key Insights

### The DP Formula:
```
To reach step i with minimum cost:
- Come from step i-1: cost = dp[i-1] + cost[i-1]
- Come from step i-2: cost = dp[i-2] + cost[i-2]

dp[i] = min(both options)
```

### Why This Works:
- **Base cases**: `dp[0] = 0` and `dp[1] = 0` (can start at either step 0 or 1)
- **At each step**: Choose the cheaper path (from 1 step back or 2 steps back)
- **Final answer**: `dp[n]` is the minimum cost to reach the top (beyond the last step)

## Example Walkthrough

**Input: cost = [10, 15, 20]**

```
Step 0: dp[0] = 0 (can start here for free)
Step 1: dp[1] = 0 (can start here for free)

Step 2: dp[2] = min(dp[1] + cost[1], dp[0] + cost[0])
              = min(0 + 15, 0 + 10)
              = 10

Step 3 (top): dp[3] = min(dp[2] + cost[2], dp[1] + cost[1])
                     = min(10 + 20, 0 + 15)
                     = 15

Answer: 15
```

**Path taken**: Start at index 1 (cost 0) → Pay 15 at step 1 → Climb 2 steps to top = Total: 15

## Time and Space Complexity

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - DP array of size n+1

**Space Optimization Possible**: Can reduce to O(1) by keeping only last 2 values (like in problem 70)

## Related Problems

- [70. Climbing Stairs](../70/README.md) - Base problem without costs
- [198. House Robber](https://leetcode.com/problems/house-robber/) - Similar DP pattern with constraints

## Tags
- Dynamic Programming
- Array
