# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb **1 step** or **2 steps**. In how many distinct ways can you climb to the top?

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top:
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Example 3:**
```
Input: n = 5
Output: 8
Explanation: Ways to reach step 5:
- From step 4 (take 1 step) 
- From step 3 (take 2 steps)
So: ways(5) = ways(4) + ways(3)
```

## My Initial Approach & Learning Journey

> **"My initial recursive thought was actually RIGHT! I realized that to get to step `n`, I can either come from step `n-1` (by taking 1 step) or from step `n-2` (by taking 2 steps). So the total ways = ways(n-1) + ways(n-2). But this pure recursion is O(2^n) which is too slow! I needed to learn dynamic programming and memoization to make it efficient."**

## Initial Hunch and Solution Evolution

<details>
<summary>► My First Thoughts (Correct but Slow!)</summary>

When I first saw this problem, I immediately thought:
> "To reach step 5, I need to count how many ways I can reach step 4, plus how many ways I can reach step 3. Because from step 4, I take 1 step to reach 5, and from step 3, I take 2 steps to reach 5!"

**My Initial Recursive Solution:**
```python
def climbStairs(self, n: int) -> int:
    def dfs(res, val): 
        if val < 0: 
            return 0
        
        if val == 0: 
            return 1

        n1 = dfs(res, val-1)  # Ways from previous step
        n2 = dfs(res, val-2)  # Ways from 2 steps back
    
        return n1 + n2

    return dfs(0, n)
```

**This was CORRECT but SLOW!**
- Time Complexity: **O(2^n)** - exponential!
- Why? Because I calculate the same values over and over again

**Example of redundant work for n=5:**
```
dfs(5)
├── dfs(4)
│   ├── dfs(3)
│   │   ├── dfs(2)
│   │   │   ├── dfs(1)
│   │   │   └── dfs(0) ✓
│   │   └── dfs(1)
│   │       ├── dfs(0) ✓
│   │       └── dfs(-1) ✗
│   └── dfs(2)         ← CALCULATED AGAIN!
│       ├── dfs(1)     ← CALCULATED AGAIN!
│       └── dfs(0)     ← CALCULATED AGAIN!
└── dfs(3)             ← ENTIRE SUBTREE CALCULATED AGAIN!
    ├── dfs(2)
    └── dfs(1)
```

I'm calculating `dfs(3)`, `dfs(2)`, `dfs(1)` multiple times!
</details>

<details>
<summary>▲ Key Insights That Helped Me Understand</summary>

### The Pattern Discovery:
Let me work through small examples:
- **n=1**: Only 1 way → take 1 step
- **n=2**: 2 ways → (1+1) or (2)
- **n=3**: 3 ways → ways(2) + ways(1) = 2 + 1 = 3
- **n=4**: 5 ways → ways(3) + ways(2) = 3 + 2 = 5
- **n=5**: 8 ways → ways(4) + ways(3) = 5 + 3 = 8

**This is the Fibonacci sequence!**

### Why This Formula Works:
To get to step `n`, I can **only** arrive from:
1. **Step n-1** (by taking 1 step) → all the ways to reach n-1
2. **Step n-2** (by taking 2 steps) → all the ways to reach n-2

**Total ways to reach n = ways(n-1) + ways(n-2)**

This formula automatically considers both possibilities (taking 1 step or 2 steps) for step `n`!

### The Memoization Insight:
- Instead of recalculating the same values, **save them** in a dictionary or array
- When I need a value again, just **look it up** instead of recalculating
- This changes time complexity from **O(2^n)** to **O(n)**!
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Forgetting base cases**: What if n=0 or n=1?
- **Array size**: Need `dp[n+1]` to store values from 0 to n
- **Overcomplicated thinking**: Don't try to enumerate all combinations, just count them!
- **Not realizing the pattern**: This is Fibonacci in disguise!
</details>

## My Solution Analysis

### What I Implemented (Dynamic Programming):

**Bottom-Up DP Solution (Optimal):**
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2: 
            return n

        # Create array to store number of ways for each step
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        
        # Build up from step 3 to step n
        for i in range(3, n+1): 
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
```

### Key Design Decisions:

**1. Bottom-Up Approach (Instead of Top-Down)**
```python
# Start from small values and build up
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
```
- **Easier to understand**: Build from known values
- **No recursion overhead**: Just a simple loop
- **Guaranteed to work**: No stack overflow issues

**2. Array for Memoization**
```python
dp = [0] * (n+1)  # Store ways for steps 0 to n
dp[1], dp[2] = 1, 2  # Base cases
```
- **Fast lookup**: O(1) access time
- **Clear index mapping**: `dp[i]` = ways to reach step `i`

**3. Base Case Handling**
```python
if n <= 2: 
    return n
```
- **n=1**: Only 1 way (take 1 step)
- **n=2**: 2 ways (1+1 or 2)
- Handles edge cases before array creation

## Algorithm Walkthrough

### Example: n = 5

**Initial Setup:**
```python
dp = [0, 1, 2, 0, 0, 0]
       0  1  2  3  4  5  (indices)
```

**Step-by-step calculation:**

```
i=3: dp[3] = dp[2] + dp[1] = 2 + 1 = 3
     dp = [0, 1, 2, 3, 0, 0]

i=4: dp[4] = dp[3] + dp[2] = 3 + 2 = 5
     dp = [0, 1, 2, 3, 5, 0]

i=5: dp[5] = dp[4] + dp[3] = 5 + 3 = 8
     dp = [0, 1, 2, 3, 5, 8]

Answer: dp[5] = 8
```

**Visualization of the 8 ways to reach step 5:**
```
1. [1, 1, 1, 1, 1]
2. [1, 1, 1, 2]
3. [1, 1, 2, 1]
4. [1, 2, 1, 1]
5. [2, 1, 1, 1]
6. [1, 2, 2]
7. [2, 1, 2]
8. [2, 2, 1]
```

## Why My Initial Thought Was Right!

### The Core Insight:
```
To reach step n:
- I can take 1 step from (n-1) → this gives me ALL ways to reach (n-1)
- I can take 2 steps from (n-2) → this gives me ALL ways to reach (n-2)

Total = ways(n-1) + ways(n-2)
```

**This formula automatically handles both the 1-step and 2-step choices!**

### Example for n=5:
- **Ways to reach step 4**: 5 different ways
  - From each of these, I can take **1 step** to reach 5
  - So that's **5 ways** to reach 5
- **Ways to reach step 3**: 3 different ways
  - From each of these, I can take **2 steps** to reach 5
  - So that's **3 more ways** to reach 5
- **Total**: 5 + 3 = **8 ways** to reach step 5

## Comparison: Recursion vs Dynamic Programming

### My Initial Recursion (Slow):
```python
def climbStairs(n):
    if n <= 1: return 1
    return climbStairs(n-1) + climbStairs(n-2)

Time: O(2^n) - exponential!
Space: O(n) - recursion stack
```

### Optimized DP (Fast):
```python
def climbStairs(n):
    if n <= 2: return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

Time: O(n) - linear!
Space: O(n) - array storage
```

### Even More Optimized (Space-Efficient):
```python
def climbStairs(n):
    if n <= 2: return n
    prev2, prev1 = 1, 2
    for i in range(3, n+1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1

Time: O(n) - linear!
Space: O(1) - only 2 variables!
```

## What I Learned

### Problem-Solving Insight:
- **My recursive thinking was correct!** The formula was right
- **Recognizing repeated work** is key to optimization
- **Dynamic Programming** = Recursion + Memoization
- This pattern appears in many problems (Fibonacci, house robber, etc.)

### Technical Skills:
- **Memoization**: Store results to avoid recalculation
- **Bottom-up building**: Start from base cases and build up
- **Space optimization**: Only need last 2 values, not entire array

### Pattern Recognition:
This is a classic **1D Dynamic Programming** problem:
- State: `dp[i]` = number of ways to reach step i
- Transition: `dp[i] = dp[i-1] + dp[i-2]`
- Base cases: `dp[1] = 1, dp[2] = 2`

## Time and Space Complexity

### My DP Solution:
- **Time Complexity**: O(n)
  - Single loop from 3 to n
  - Each iteration does constant work
  
- **Space Complexity**: O(n)
  - Array of size n+1 to store results

### Space-Optimized Solution:
- **Time Complexity**: O(n)
  - Same loop as before
  
- **Space Complexity**: O(1)
  - Only storing 2 previous values

## Related Problems

- [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) - Similar pattern with cost
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) - Exact same pattern
- [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) - Same pattern with 3 previous values
- [198. House Robber](https://leetcode.com/problems/house-robber/) - Similar DP pattern

## Tags
- Dynamic Programming
- Math
- Memoization
- Fibonacci Pattern
