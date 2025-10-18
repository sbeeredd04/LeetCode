# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Examples

**Example 1:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: 
- At speed k=4: 
  - Pile 1: ceil(3/4) = 1 hour
  - Pile 2: ceil(6/4) = 2 hours
  - Pile 3: ceil(7/4) = 2 hours
  - Pile 4: ceil(11/4) = 3 hours
  - Total: 1+2+2+3 = 8 hours ✓
```

**Example 2:**
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: At speed k=30, Koko can finish all piles in exactly 5 hours (one pile per hour).
```

**Example 3:**
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
Explanation: At speed k=23, Koko needs 6 hours total.
```

**Constraints:**
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## Approach & Intuition

### Key Insight

> **The minimum eating speed lies somewhere between 1 (slowest) and max(piles) (fastest). We can use binary search to find it efficiently!**

### Problem Analysis
1. **Search space**: The eating speed `k` ranges from `1` to `max(piles)`
2. **Monotonic property**: If Koko can finish at speed `k`, she can also finish at any speed > `k`
3. **Binary search on answer space**: We're searching for the minimum `k` where `canFinish(k) == True`

### Why Binary Search?
- If we can finish at speed `k`, we don't need to check speeds > `k`
- If we can't finish at speed `k`, we need a faster speed (speeds < `k` won't work either)
- This monotonic property makes binary search perfect for this problem

---

## My Implementation

```python
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max element in the piles array
        max_pile = max(piles)
        
        # Binary search to find the minimum eating speed
        left = 1
        right = max_pile
        
        # Start with the middle of the array and the left and right pointers
        while left < right: 
            # Find the middle of the array
            mid = (left + right) // 2
            
            # Calculate the total hours needed to eat all the bananas at the current speed
            total_hours = sum(math.ceil(pile/mid) for pile in piles)
            
            # If the total hours is less than or equal to required then right = mid
            if total_hours <= h:
                right = mid
            # If the total hours is greater than required then left = mid + 1
            else:
                left = mid + 1
        
        # Return the minimum eating speed
        return left
```

---

## Algorithm Explanation

### Step-by-Step Process

**1. Initialize Binary Search Range**
```python
left = 1              # Minimum possible speed
right = max(piles)    # Maximum possible speed (eating the largest pile in 1 hour)
```

**2. Binary Search Loop**
```python
while left < right:
    mid = (left + right) // 2
    total_hours = sum(math.ceil(pile/mid) for pile in piles)
```

**3. Decision Logic**
```python
if total_hours <= h:
    right = mid      # Can finish in time, try slower speed
else:
    left = mid + 1   # Too slow, need faster speed
```

### Visual Example
```
piles = [3,6,7,11], h = 8

Initial: left=1, right=11
  Range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Iteration 1: mid=6
  Hours needed: ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)
              = 1 + 1 + 2 + 2 = 6 hours ≤ 8 ✓
  → Can finish in time, try slower: right = 6
  Range: [1, 2, 3, 4, 5, 6]

Iteration 2: mid=3
  Hours needed: ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
              = 1 + 2 + 3 + 4 = 10 hours > 8 ✗
  → Too slow, need faster: left = 4
  Range: [4, 5, 6]

Iteration 3: mid=5
  Hours needed: ceil(3/5) + ceil(6/5) + ceil(7/5) + ceil(11/5)
              = 1 + 2 + 2 + 3 = 8 hours ≤ 8 ✓
  → Can finish in time, try slower: right = 5
  Range: [4, 5]

Iteration 4: mid=4
  Hours needed: ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4)
              = 1 + 2 + 2 + 3 = 8 hours ≤ 8 ✓
  → Can finish in time, try slower: right = 4
  Range: [4]

left == right, return 4
```

---

## Complexity Analysis

### Time Complexity: O(n log m)
Where:
- `n = len(piles)` - number of piles
- `m = max(piles)` - maximum pile size

**Breakdown:**
- Binary search iterations: `O(log m)` where `m = max(piles)`
- For each iteration, we calculate total hours: `O(n)` to sum over all piles
- **Total: O(n log m)**

### Space Complexity: O(1)
- Only using a few variables: `left`, `right`, `mid`, `total_hours`
- No additional data structures needed
- **Total: O(1)** constant space

---

## Key Insights & Lessons

### Lesson 1: Binary Search on Answer Space
This problem demonstrates a powerful pattern: **binary search on the answer space** rather than searching in an array.

**The pattern:**
```python
# Instead of searching for an element in a sorted array,
# we search for the minimum/maximum value that satisfies a condition

left, right = min_possible_answer, max_possible_answer
while left < right:
    mid = (left + right) // 2
    if condition_satisfied(mid):
        right = mid  # Try smaller value
    else:
        left = mid + 1  # Need larger value
return left
```

### Lesson 2: Using Math.ceil for Division
```python
# Time needed for a pile at speed k
hours = math.ceil(pile / k)

# Alternative without math.ceil:
hours = (pile + k - 1) // k  # Integer division trick
```

### Lesson 3: Monotonic Property Recognition
**Key question:** "If I can do X at value k, can I also do X at any value > k?"
- If yes → the problem has monotonic property → binary search applicable
- In this problem: If I can finish at speed k, I can finish at any speed > k ✓

### Lesson 4: Left < Right vs Left <= Right
```python
# Use left < right (not left <= right) when:
# - We want to find the minimum value that satisfies a condition
# - We use right = mid (not right = mid - 1)

while left < right:    # Correct for this problem
    mid = (left + right) // 2
    if can_finish(mid):
        right = mid    # Include mid in next search
```

---

## Related Problems

### Similar Binary Search on Answer Space:
- **410. Split Array Largest Sum** - Binary search on maximum subarray sum
- **774. Minimize Max Distance to Gas Station** - Binary search on maximum distance
- **1011. Capacity To Ship Packages Within D Days** - Binary search on ship capacity
- **1283. Find the Smallest Divisor Given a Threshold** - Binary search on divisor

### Pattern Recognition:
When you see:
- "Find minimum/maximum value that satisfies a condition"
- A search space with monotonic property
- Need to optimize over a range of values

Consider: **Binary search on answer space**

---

## Quick Reference

### Binary Search on Answer Space Template
```python
def binary_search_answer_space(problem_input):
    # Define search range
    left = minimum_possible_answer
    right = maximum_possible_answer
    
    # Binary search
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid satisfies the condition
        if is_valid(mid, problem_input):
            right = mid      # Try smaller value for minimum
            # left = mid + 1  # Use this for maximum
        else:
            left = mid + 1   # Need larger value for minimum
            # right = mid     # Use this for maximum
    
    return left
```

---

**Time Complexity:** O(n log m) where n = number of piles, m = max pile size  
**Space Complexity:** O(1)  
**Pattern:** Binary Search on Answer Space
