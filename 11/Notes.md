# 11. Container With Most Water

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that can hold the most water.

Return the maximum amount of water a container can store.

## Examples
```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 form container with area = min(8,7) * (8-1) = 7 * 7 = 49

Input: height = [1,1]
Output: 1
```

---

## My Solution Journey

### First Attempt: Brute Force (O(n²))
```python
# My initial intuition: Check ALL possible pairs
def maxArea(self, height: List[int]) -> int:
    left, right = 0, 0
    area = 0 

    while left < len(height) - 1: 
        right = len(height) - 1 
        
        while right > left: 
            area = max(area, (min(height[left], height[right]) * (right - left)))
            right -= 1
        
        left += 1
    
    return area
```

### Why I Started Here
- **Obvious approach**: Try every possible container
- **Clear logic**: For each left line, check all possible right lines
- **Easy to implement**: Nested loops are straightforward

### Problems with Brute Force
- **Time Complexity**: O(n²) - too slow for large inputs
- **Redundant calculations**: Many unnecessary comparisons
- **Inefficient**: Doesn't leverage problem structure

---

## The Breakthrough: Two Pointer Intuition

### The Key Question
> "When should I move the left pointer vs right pointer?"

### The Insight
> **Always move the pointer with the shorter line!**

**Why?** Because the container's height is limited by the shorter line. Moving the taller line's pointer won't increase the area - we need to find a potentially taller short line.

### Critical Understanding: Why Move the Shorter Line?
The area formula is: `Area = min(height[left], height[right]) * width`

- **The shorter line determines the height** - it's the bottleneck
- **Moving the taller line pointer** would keep the same limiting height but reduce width → guaranteed smaller area
- **Moving the shorter line pointer** might find a taller line → potential for larger area despite reduced width
- **Only by moving the shorter line can we possibly improve the area**

### Optimal Solution
```python
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right: 
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_area = max(max_area, current_area)
        
        # KEY INSIGHT: Move pointer with shorter line
        if height[left] < height[right]:
            left += 1   # Left line is shorter, try to find taller one
        else:
            right -= 1  # Right line is shorter, try to find taller one
            
    return max_area
```

---

## Why This Works: The Logic

### Area Calculation
```
Area = min(height[left], height[right]) * (right - left)
       ↑                                   ↑
   Limited by shorter line              Width decreases as pointers move
```

### Movement Strategy
| Scenario | Action | Reasoning |
|----------|--------|-----------|
| `height[left] < height[right]` | `left += 1` | Left line limits height - find taller left line |
| `height[left] > height[right]` | `right -= 1` | Right line limits height - find taller right line |
| `height[left] == height[right]` | Move either | Both limit equally - either direction works |

### Example Walkthrough
```
height = [1,8,6,2,5,4,8,3,7]
          ↑               ↑
        left            right

Step 1: area = min(1,7) * 8 = 8    → height[left] < height[right] → left++
Step 2: area = min(8,7) * 7 = 49   → height[left] > height[right] → right--
Step 3: area = min(8,3) * 6 = 18   → height[left] > height[right] → right--
...continue until left >= right
```

---

## Performance Comparison

| Approach | Time | Space | Intuition |
|----------|------|-------|-----------|
| **Brute Force** | O(n²) | O(1) | Check all pairs |
| **Two Pointers** | **O(n)** | **O(1)** | Move shorter line pointer |

### Why O(n) Time?
- Each pointer moves at most `n` times
- Total moves: `left` moves ≤ n, `right` moves ≤ n
- Combined: ≤ 2n moves → O(n)

---

## Key Learning Moments

### The "Aha!" Moment
> "I was stuck until I realized: **the shorter line is always the bottleneck**"

### From Brute Force to Optimal
1. **Started with**: Check every possible pair
2. **Realized**: Most comparisons are unnecessary  
3. **Key insight**: Only move the limiting (shorter) pointer
4. **Result**: O(n²) → O(n) improvement!

### Pattern Recognition
- **Two pointers**: Start at extremes, move based on conditions
- **Greedy choice**: Always optimize the current bottleneck
- **Problem structure**: Sorted/structured data often enables pointer techniques

---

## Common Pitfalls & Watch-Outs

### Wrong Movement Logic
```python
# Wrong: Always move left or always move right
left += 1  # Ignores which line is limiting

# Right: Move based on height comparison
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

### Off-by-One Errors
```python
# Wrong: Might miss the last valid pair
while left <= right:  # Could compare element with itself

# Right: Ensure valid container
while left < right:
```

### Forgetting to Update Maximum
```python
# Wrong: Calculate but don't track
current_area = width * current_height  # Missing max update

# Right: Always track maximum
max_area = max(max_area, current_area)
```

---

## Related Two-Pointer Problems

- [**#167 Two Sum II**](../167/) - Find sum in sorted array
- [**#15 3Sum**](../15/) - Three number sum with two pointers
- [**#42 Trapping Rain Water**](../42/) - Similar water/area concept
- [**#125 Valid Palindrome**](../125/) - Two pointers from extremes

---

## Why This Solution is Elegant

### Optimal Complexity: O(n) time, O(1) space
### Intuitive Logic: Move the bottleneck pointer
### Single Pass: Each element visited at most once
### Simple Implementation: Clean, readable code

**The beauty**: Transforms an obvious O(n²) problem into an elegant O(n) solution through clever pointer movement!