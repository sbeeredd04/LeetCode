# Binary Search (LeetCode 704) - Learning Notes

## Problem Understanding
I need to search for a target value in a sorted array and return its index, or -1 if not found. The key insight is that the array is already sorted, which allows me to use binary search for O(log n) time complexity instead of linear search.

## My Implementation Analysis

### Algorithm Approach
I implemented the classic binary search algorithm:
1. Use two pointers: `left` at start (0) and `right` at end (len(nums)-1)
2. While the search space is valid (`left <= right`):
   - Calculate middle index: `mid = (left + right) // 2`
   - Compare `nums[mid]` with target:
     - If greater: search left half by setting `right = mid - 1`
     - If less: search right half by setting `left = mid + 1`
     - If equal: found target, return `mid`
3. If loop exits without finding target, return -1

### Key Implementation Details I Got Right

**1. Correct Boundary Initialization**
```python
left, right = 0, len(nums)-1
```
I correctly set `right` to `len(nums)-1` (last valid index) rather than `len(nums)`. This is crucial for the "closed interval" approach I'm using.

**2. Proper Loop Condition**
```python
while left <= right:
```
Using `<=` is correct because when `left == right`, there's still one element to check. This prevents missing the target when the search space narrows to a single element.

**3. Safe Midpoint Calculation**
```python
mid = (left + right) // 2
```
Using integer division `//` ensures I get an integer index. This formula works well for Python, though in other languages I might need to worry about integer overflow.

**4. Correct Boundary Updates**
- `right = mid - 1`: When target is smaller, I exclude `mid` since I already checked it
- `left = mid + 1`: When target is larger, I exclude `mid` since I already checked it

This prevents infinite loops and ensures the search space shrinks properly.

### Algorithm Walkthrough Example
Let me trace through `nums = [1,3,5,7,9,11]`, `target = 7`:

**Iteration 1:**
- `left = 0, right = 5`
- `mid = (0 + 5) // 2 = 2`
- `nums[2] = 5 < 7`, so `left = mid + 1 = 3`

**Iteration 2:**
- `left = 3, right = 5`
- `mid = (3 + 5) // 2 = 4`
- `nums[4] = 9 > 7`, so `right = mid - 1 = 3`

**Iteration 3:**
- `left = 3, right = 3`
- `mid = (3 + 3) // 2 = 3`
- `nums[3] = 7 == 7`, return `3`

The algorithm correctly finds the target in 3 iterations instead of potentially 6 with linear search.

### Edge Cases My Solution Handles

**1. Empty Array**
- `nums = []`: `left = 0, right = -1`, condition `left <= right` is false, returns -1

**2. Single Element**
- `nums = [5], target = 5`: `left = 0, right = 0`, finds target immediately
- `nums = [5], target = 3`: `left = 0, right = 0`, doesn't match, updates boundaries, exits loop

**3. Target Not Found**
- Target smaller than all elements: Loop will exhaust with `left > right`
- Target larger than all elements: Same behavior
- Target between elements: Same behavior

**4. Target at Boundaries**
- First element: Algorithm handles correctly
- Last element: Algorithm handles correctly

### Time and Space Complexity

**Time Complexity: O(log n)**
- Each iteration eliminates half of the remaining search space
- Maximum iterations: log₂(n)
- Example: array of 1000 elements needs at most 10 iterations

**Space Complexity: O(1)**
- Only using a constant amount of extra space for variables
- No recursion, so no call stack overhead

### Common Binary Search Pitfalls I Avoided

**1. Infinite Loops**
I avoided this by:
- Using `left <= right` (not `left < right`)
- Properly updating boundaries to exclude already-checked `mid`
- Using `mid - 1` and `mid + 1` instead of just `mid`

**2. Integer Overflow**
- In Python, this isn't an issue, but in languages like Java/C++, I'd use `left + (right - left) // 2`

**3. Off-by-One Errors**
- Correctly initialized `right = len(nums) - 1`
- Proper boundary updates ensure no elements are skipped or double-checked

### Alternative Approaches I Could Consider

**1. Recursive Implementation**
```python
def binarySearchRecursive(self, nums, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return self.binarySearchRecursive(nums, target, left, mid - 1)
    else:
        return self.binarySearchRecursive(nums, target, mid + 1, right)
```
This is more elegant but uses O(log n) space due to call stack.

**2. Template-Based Approach**
Using a more generalized binary search template that works for various binary search problems.

### Why Binary Search Works Here
1. **Sorted Array**: The prerequisite for binary search
2. **Search Property**: If `nums[mid] < target`, the target must be in the right half
3. **Elimination**: Each comparison eliminates half the search space
4. **Monotonicity**: The comparison property is consistent throughout the array

### Learning Takeaways
1. Binary search is powerful when the search space can be eliminated systematically
2. Boundary management is crucial - always be clear about whether you're using open or closed intervals
3. The `<=` vs `<` choice in the while condition depends on the boundary initialization
4. This pattern extends to many other problems beyond simple array search
5. Always trace through examples to verify boundary updates are correct

My implementation is clean, efficient, and handles all edge cases correctly. The key insight is recognizing that the sorted property allows for logarithmic search time.