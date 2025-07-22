# Binary Search Deep Dive 🎯

## Table of Contents
- [Core Concepts](#core-concepts)
- [Templates](#templates)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Time & Space Complexity](#time--space-complexity)
- [Common Pitfalls](#common-pitfalls)

## Core Concepts
<details>
<summary>Click to expand</summary>

### Basic Binary Search
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2  # or left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
```

### Key Properties
1. Input must be sorted (or have a monotonic property)
2. Reduces search space by half in each iteration
3. Time complexity: O(log n)
4. Can be used to find exact matches or boundaries
</details>

## Templates
<details>
<summary>Click to expand</summary>

### 1. Basic Template (Exact Match)
```python
def basic_binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Not found
```

### 2. Left Boundary Template
```python
def left_boundary(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
            
    return left  # First position >= target
```

### 3. Right Boundary Template
```python
def right_boundary(nums, target):
    left, right = -1, len(nums) - 1
    
    while left < right:
        mid = right - (right - left) // 2  # Ceiling division
        
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
            
    return left  # Last position <= target
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Rotated Array Search
```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
```

### 2. Matrix Search
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False
```

### 3. Capacity/Threshold Search
```python
def threshold_search(items, target):
    left, right = min(items), max(items)
    
    while left < right:
        mid = (left + right) // 2
        if check(mid) >= target:
            right = mid
        else:
            left = mid + 1
            
    return left

def check(capacity):
    # Problem-specific check function
    # Returns some value to compare against target
    pass
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Binary Search on Answer
```python
def binary_search_answer(nums):
    left = min_possible
    right = max_possible
    
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

def is_valid(value):
    # Problem-specific validation
    pass
```

### 2. Double Binary Search
```python
def double_binary_search(matrix, target):
    # Search rows first
    top, bottom = 0, len(matrix) - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if matrix[row][0] <= target <= matrix[row][-1]:
            # Search within the row
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        elif matrix[row][0] > target:
            bottom = row - 1
        else:
            top = row + 1
    return False
```
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Time Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Basic Binary Search | O(log n) |
| Matrix Search | O(log(m*n)) |
| Rotated Array | O(log n) |

### Space Complexity
- Iterative: O(1)
- Recursive: O(log n) due to call stack
</details>

## Common Pitfalls
<details>
<summary>Click to expand</summary>

### 1. Integer Overflow
```python
# WRONG
mid = (left + right) // 2  # Can overflow in some languages

# RIGHT
mid = left + (right - left) // 2
```

### 2. Infinite Loops
```python
# WRONG
while left < right:
    mid = (left + right) // 2
    if condition:
        left = mid  # Might never change

# RIGHT
while left < right:
    mid = (left + right) // 2
    if condition:
        left = mid + 1  # Guaranteed to change
```

### 3. Off-by-One Errors
```python
# WRONG
right = len(nums)  # Too far for array access
mid = (left + right) // 2  # Could be out of bounds

# RIGHT
right = len(nums) - 1
mid = left + (right - left) // 2
```
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [704. Binary Search](../704/README.md) - Classic binary search

### Medium
- [33. Search in Rotated Sorted Array](../33/README.md) - Modified binary search
- [74. Search a 2D Matrix](../74/README.md) - Matrix binary search
- [875. Koko Eating Bananas](../875/README.md) - Binary search on answer

### Hard
- [153. Find Minimum in Rotated Sorted Array](../153/README.md) - Modified binary search
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Binary Search Patterns](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template)
2. [Binary Search on GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
3. [Advanced Binary Search Problems](https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101)
</details>

---

*Remember: Binary search is not just for sorted arrays! Look for any problem where you can reduce the search space by half based on some condition.*
