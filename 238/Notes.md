# 238. Product of Array Except Self

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator.

## Examples
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints
- 2 ≤ nums.length ≤ 10^5
- -30 ≤ nums[i] ≤ 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Approach 1: Total Product with Division (My Solution)

### Key Insights
1. **Basic Idea**: Calculate the total product of all numbers, then divide by each element to get the product except self
2. **Critical Edge Case**: Handle zeros carefully since division by zero is undefined
3. **Zero Handling Logic**:
   - If there are **more than 1 zeros**: All results should be 0
   - If there's **exactly 1 zero**: Only the position with zero gets the total product (excluding the zero), all others get 0
   - If there are **no zeros**: Each position gets `total_product // nums[i]`

### Implementation
```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Calculate total product (excluding zeros) and count zeros
    total_product = 1
    count0 = 0
    for num in nums:
        if num != 0:
            total_product *= num
        else:
            count0 += 1
    
    # If more than one zero, all results are zero
    if count0 > 1:
        return [0] * len(nums)
    
    # Process each position
    for i in range(len(nums)):
        if count0 == 1:
            if nums[i] == 0:
                nums[i] = total_product  # Only zero position gets the product
            else:
                nums[i] = 0  # All non-zero positions get 0
        else:
            nums[i] = total_product // nums[i]  # Normal case
    
    return nums
```

### Time & Space Complexity
- **Time**: O(n) - Two passes through the array
- **Space**: O(1) - Modifying input array in-place (excluding output space)

### Pros & Cons
- ✅ **Pros**: Simple logic, easy to understand, handles edge cases well
- ❌ **Cons**: Uses division operator (problem asks to avoid it), modifies input array

## Approach 2: Left & Right Products (Optimal)

### Key Insights
1. For each position `i`, the result is `left_product[i] * right_product[i]`
2. `left_product[i]` = product of all elements to the left of index `i`
3. `right_product[i]` = product of all elements to the right of index `i`
4. Can be optimized to use only one array by doing two passes

### Implementation
```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    
    # First pass: calculate left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Second pass: multiply by right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result
```

### Time & Space Complexity
- **Time**: O(n) - Two passes
- **Space**: O(1) - Only using the output array

## Python Built-in Functions for Products

Python doesn't have a built-in `product()` function like `sum()`, but you can use:

1. **`math.prod()`** (Python 3.8+):
   ```python
   import math
   product = math.prod(nums)
   ```

2. **`functools.reduce()`**:
   ```python
   from functools import reduce
   import operator
   product = reduce(operator.mul, nums, 1)
   ```

3. **`numpy.prod()`** (if using NumPy):
   ```python
   import numpy as np
   product = np.prod(nums)
   ```

## Key Takeaways
1. **Edge Case Handling**: Always consider zeros when dealing with products
2. **Division Alternative**: Use left/right product approach to avoid division
3. **Space Optimization**: Can achieve O(1) extra space by reusing output array
4. **Multiple Solutions**: Sometimes a "wrong" approach (using division) can still provide valuable insights 