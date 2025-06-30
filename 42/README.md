# 42. Trapping Rain Water

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples
```python
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 3 * 10^4`

---

## Key Insight: Strong Connection to Container With Most Water

This problem has a **deep algorithmic relationship** with [**#11 Container With Most Water**](../11/) - they share the same core two-pointer strategy but solve different geometric problems.

### Container vs Trapping: The Fundamental Difference

| Aspect | Container With Most Water | Trapping Rain Water |
|--------|--------------------------|-------------------|
| **Geometry** | Single rectangular container | Multiple trapped water pockets |
| **Water calculation** | `width × min(left_height, right_height)` | `sum(min(left_max, right_max) - height[i])` |
| **Height logic** | Current bar heights | **Maximum** heights seen so far |
| **Movement rule** | Move pointer with shorter bar | Move pointer with smaller **max** |
| **Goal** | Find one optimal container | Accumulate all trapped water |

### The Shared Core Pattern
Both problems use the **same two-pointer movement logic**:

```python
# Container With Most Water
if height[left] < height[right]:
    left += 1    # Move away from shorter bar
else:
    right -= 1   # Move away from shorter bar

# Trapping Rain Water  
if left_max < right_max:
    left += 1    # Move away from smaller max
else:
    right -= 1   # Move away from smaller max
```

**Why this works**: We can safely process the side with the smaller limiting value because we know it can't be improved by the other side.

---

## Why Use Max Left and Max Right (Not Current Heights)?

### The Water Trapping Principle
> **Water at position `i` is trapped by the minimum of the tallest bars to its left and right**

```
Water at position i = min(max_left, max_right) - height[i]
```

### Visual Understanding
```
height = [3,0,2,0,4]
          ↑ ↑ ↑ ↑ ↑
         max_left:  [3,3,3,3,4]
         max_right: [4,4,4,4,4]
         
At index 1: water = min(3,4) - 0 = 3
At index 3: water = min(3,4) - 0 = 3
Total trapped = 6
```

### Why Two Pointers Work
- **If `left_max < right_max`**: The left side is the limiting factor
  - Water at `left` position = `left_max - height[left]`
  - We know `right_max` is larger, so it won't be the constraint
- **If `right_max < left_max`**: The right side is the limiting factor
  - Water at `right` position = `right_max - height[right]`
  - We know `left_max` is larger, so it won't be the constraint

---

## Solution Analysis

### My Implementation
```python
def trap(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total_water = 0
    
    while left < right: 
        # Move pointer with smaller max (the limiting factor)
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]
            
    return total_water
```

### Why This Works
1. **Track maximums**: `left_max` and `right_max` represent the tallest bars seen so far
2. **Move the constrained side**: Whichever side has smaller max is the bottleneck
3. **Calculate trapped water**: `max_height - current_height` gives water at current position
4. **Update maximums**: Keep track of the tallest bar seen from each direction

---

## Step-by-Step Walkthrough

### Example: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

```
Initial: left=0, right=11, left_max=0, right_max=1
         [0,1,0,2,1,0,1,3,2,1,2,1]
          ↑                     ↑

Step 1: left_max(0) < right_max(1) → move left
        left=1, left_max=1, water += 1-1 = 0

Step 2: left_max(1) = right_max(1) → move right  
        right=10, right_max=2, water += 2-1 = 1

Step 3: left_max(1) < right_max(2) → move left
        left=2, left_max=1, water += 1-0 = 1
        
...continue until left >= right
```

---

## Alternative Approaches

### Approach 1: Brute Force
```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    total = 0
    for i in range(len(height)):
        # Find max height to the left
        left_max = max(height[:i+1])
        # Find max height to the right  
        right_max = max(height[i:])
        # Water trapped at position i
        total += max(0, min(left_max, right_max) - height[i])
    
    return total
```
- **Time**: O(n²) - finding max for each position
- **Space**: O(1)

### Approach 2: Dynamic Programming
```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Fill right_max array
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water
    total = 0
    for i in range(n):
        total += max(0, min(left_max[i], right_max[i]) - height[i])
    
    return total
```
- **Time**: O(n) - three separate passes
- **Space**: O(n) - two arrays for max values

### Approach 3: Two Pointers (Optimal)
```python
# My solution above
```
- **Time**: O(n) - single pass
- **Space**: O(1) - only using pointers and variables

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute Force** | O(n²) | O(1) | Find max for each position |
| **Dynamic Programming** | O(n) | O(n) | Pre-compute max arrays |
| **Two Pointers** | **O(n)** | **O(1)** | Optimal solution |

---

## Key Insights & Pattern Recognition

### Connection to Container With Most Water
Both problems demonstrate the **two-pointer technique** with different objectives:
- **Container**: Maximize area between two lines
- **Trapping**: Accumulate water trapped at each position

### The "Limiting Factor" Pattern
- Move the pointer that represents the current **bottleneck**
- In both problems, the smaller value determines what's possible
- This ensures we don't miss any optimal solutions

### When to Use This Pattern
- **Sorted or structured data** where pointers can eliminate possibilities
- **Optimization problems** where one side limits the solution
- **Area/volume calculations** involving boundaries

---

## Common Pitfalls

### Forgetting to Update Max Values
```python
# Wrong: Don't update max after moving pointer
if left_max < right_max:
    left += 1
    total_water += left_max - height[left]  # Using old max!

# Right: Update max first, then calculate
if left_max < right_max:
    left += 1
    left_max = max(left_max, height[left])
    total_water += left_max - height[left]
```

### Incorrect Water Calculation
```python
# Wrong: Forgetting that water can't be negative
total_water += left_max - height[left]  # Could be negative!

# Right: Ensure non-negative (though not needed with correct algorithm)
total_water += max(0, left_max - height[left])
```

---

## Related Problems

- [**#11 Container With Most Water**](../11/) - Two pointers for area maximization
- [**#84 Largest Rectangle in Histogram**](../84/) - Stack-based area calculation
- [**#407 Trapping Rain Water II**](../407/) - 2D version using priority queue

---

## Why This Solution is Elegant

### Optimal Complexity: O(n) time, O(1) space
### Single Pass: Process each element exactly once  
### Space Efficient: No need for auxiliary arrays
### Pattern Reuse: Same two-pointer strategy as Container problem

The beauty of this solution lies in recognizing that **we only need to track the limiting factor** (smaller max) to determine trapped water, making it both efficient and intuitive!