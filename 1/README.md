# Two Sum Problem: Solution Notes

## Problem Summary
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Key Insights

### Dictionary Approach (Hash Map)
- Use a dictionary to store values and their indices
- For each number, check if `target - number` exists in our dictionary
- If it exists, we found our pair
- Time Complexity: O(n) - single pass through the array
- Space Complexity: O(n) - storing n elements in dictionary

### Dictionary Conversion
Convert a list to a dictionary with values as keys and indices as values:
```python
d = {value: index for index, value in enumerate(nums)}
```

### Edge Cases to Handle
- Need to ensure we don't use the same element twice
- If duplicate values exist, only the last index is stored in the dictionary
- The problem guarantees exactly one solution exists

### Implementation Tips
1. Iterate through the array once
2. For each element `nums[i]`:
   - Calculate complement: `target - nums[i]`
   - Check if complement exists in dictionary
   - Ensure complement index isn't the current index (not using same element twice)

## Optimized Solution
Instead of creating the dictionary first and then searching, we can build the dictionary as we go:
```python
def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No solution found
```

## Time and Space Complexity
- Time Complexity: O(n) where n is the length of the array
- Space Complexity: O(n) for storing values in the hash map 