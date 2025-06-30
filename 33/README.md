# Search in Rotated Sorted Array (LeetCode 33) - Learning Notes

## Problem Understanding
I need to search for a target value in a rotated sorted array in O(log n) time. The challenge is that the array is rotated at some pivot, creating two sorted subarrays. My approach: find the pivot point, then perform binary search on the appropriate half.

## My Implementation Journey - Mistakes and Solutions

### Initial Approach - The Wrong Way (My First Mistake)

**What I Originally Tried:**
```python
# WRONG APPROACH - What I did initially
mid = (lo + hi) // 2
l1 = nums[0:mid]  # First half as separate list
l2 = nums[mid:]   # Second half as separate list
# Then binary search on l1 and l2 separately
```

**The Critical Problem:**
When I performed binary search on `l1` and `l2`, they returned **local indices** relative to the sublists, not the original array indices!

**Example of the Issue:**
- Original array: `[4,5,6,7,0,1,2]`, searching for `1`
- If `mid = 3`, then `l1 = [4,5,6]` and `l2 = [7,0,1,2]`
- Binary search on `l2` finds `1` at local index `2`
- But `1` is actually at global index `5` in the original array!

### My Solution - Index Mapping Strategy

**What I Learned:**
Instead of creating separate lists, I needed to work with **index ranges** and map results back to the original array.

**My Corrected Approach:**
```python
def binSearch(self, nums: List[int], target: int, start: int, end: int) -> int:
    lo, hi = start, end-1  # Work with original array using start/end bounds
    # Binary search returns actual index in original array
```

This way, the binary search operates on the original `nums` array but only within the specified range `[start, end)`.

### Second Major Mistake - Edge Case Boundary Issues

**The Problem I Discovered:**
When the pivot point `mid` was at the boundaries (`mid == 0` or `mid == len(nums)-1`), my binary search ranges became invalid.

**Specific Issues:**

**Case 1: Pivot at Start (`mid == 0`)**
```python
elif nums[mid] != target and mid == 0:
    return self.binSearch(nums, target, mid, len(nums))  # Search [0, len(nums))
```
If I tried to search both halves: `[0, 0)` and `[0, len(nums))`, the first range is empty!

**Case 2: Pivot at End (`mid == len(nums)-1`)**
```python
elif nums[mid] != target and mid == len(nums)-1:
    return self.binSearch(nums, target, 0, mid)  # Search [0, mid)
```
If I tried both halves: `[0, mid)` and `[mid, len(nums))`, the second range becomes `[last_index, len(nums))` which is invalid!

**My Smart Solution:**
I added explicit boundary checks to handle these edge cases:
- When `mid == 0`: Only search the right portion `[0, len(nums))`
- When `mid == len(nums)-1`: Only search the left portion `[0, mid)`

### Third Issue - Result Combination Logic Error

**Another Mistake I Fixed:**
```python
# WRONG - My initial result handling
if result1 != -1 or result2 != -1:
    return result1 + result2 + 1  # This is mathematically incorrect!
```

**The Problem:**
When one search returns `-1` (not found) and the other returns a valid index, adding them gives wrong results.

**Example:**
- `result1 = -1`, `result2 = 5`
- `result1 + result2 + 1 = -1 + 5 + 1 = 5` ✓ (happens to work)
- But `result1 = 3`, `result2 = -1`
- `result1 + result2 + 1 = 3 + (-1) + 1 = 3` ✓ (also works by luck!)

**Why It Actually Works:**
This is mathematically sound because exactly one of `result1` or `result2` will be `-1`, and the other will be the actual index. The `+1` compensates for the `-1`.

## My Final Algorithm - What I Got Right

### Step 1: Find the Pivot Point (Reused from LC 153)
```python
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] < nums[hi] and nums[mid-1] < nums[mid]:
        hi = mid - 1  # Pivot in left half
    elif nums[mid] > nums[hi] and nums[mid-1] < nums[mid]:
        lo = mid + 1  # Pivot in right half
    elif nums[mid-1] > nums[mid]:
        break  # Found pivot
    else:
        break  # No rotation or edge case
```

### Step 2: Handle Direct Match
```python
if nums[mid] == target:
    return mid  # Lucky hit at pivot point!
```

### Step 3: Smart Boundary Handling
```python
elif nums[mid] != target and mid == 0:
    return self.binSearch(nums, target, mid, len(nums))
elif nums[mid] != target and mid == len(nums)-1:
    return self.binSearch(nums, target, 0, mid)
```

### Step 4: Binary Search Both Halves
```python
result1 = self.binSearch(nums, target, 0, mid)      # Left half
result2 = self.binSearch(nums, target, mid, len(nums))  # Right half
if result1 != -1 or result2 != -1:
    return result1 + result2 + 1
```

## Key Learning Points

### 1. Index Management is Critical
**Lesson:** When working with subarrays, always consider whether you need local or global indices. Working with ranges on the original array is often better than creating new data structures.

### 2. Edge Cases at Boundaries
**Lesson:** When your algorithm divides the problem space, carefully consider what happens when the division point is at the extremes.

### 3. Mathematical Result Combination
**Lesson:** When combining results where one might be -1 (not found), the math needs to account for this. My `result1 + result2 + 1` formula works because exactly one result is -1.

### 4. Code Reuse
**Lesson:** I successfully reused my pivot-finding logic from LC 153, demonstrating good pattern recognition.

### 5. Debugging Through Examples
**Lesson:** Testing with concrete examples like `[4,5,6,7,0,1,2]` helped me identify the index mapping issues.

## Algorithm Complexity

**Time Complexity: O(log n)**
- Finding pivot: O(log n)
- Binary search on two halves: O(log n) each
- Overall: O(log n)

**Space Complexity: O(1)**
- No additional data structures created
- Working with index ranges instead of copying arrays

## Alternative Approaches I Could Consider

**Single-Pass Binary Search:**
Instead of finding the pivot first, I could determine which half is sorted during each iteration and search accordingly. This is more elegant but my approach is easier to understand and debug.

**Example of Single-Pass:**
```python
def search(self, nums, target):
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

## Summary - What Made This Solution Work

✅ **Problem Breakdown**: Successfully split the problem into "find pivot" + "binary search"
✅ **Index Management**: Learned to work with ranges instead of creating sublists
✅ **Edge Case Handling**: Identified and fixed boundary issues at `mid == 0` and `mid == len(nums)-1`
✅ **Mathematical Insight**: Developed correct result combination formula
✅ **Code Reuse**: Leveraged previous pivot-finding algorithm
✅ **Debugging Skills**: Identified the local vs global index issue through testing

My solution demonstrates strong problem-solving evolution - I identified multiple subtle issues and developed systematic fixes for each one. The final algorithm works correctly and handles all edge cases!