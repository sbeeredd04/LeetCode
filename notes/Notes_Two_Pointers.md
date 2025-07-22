# Two Pointers Deep Dive 👉👈

## Table of Contents
- [Core Concepts](#core-concepts)
- [Common Patterns](#common-patterns)
- [Implementation Strategies](#implementation-strategies)
- [Time & Space Complexity](#time--space-complexity)
- [Common Mistakes](#common-mistakes)
- [Advanced Applications](#advanced-applications)

## Core Concepts
<details>
<summary>Click to expand</summary>

### 1. Types of Two Pointer Approaches

#### Opposite Direction
```python
def opposite_direction(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process elements from both ends
        left += 1
        right -= 1
```

#### Same Direction
```python
def same_direction(arr):
    slow = fast = 0
    while fast < len(arr):
        # Fast pointer moves ahead
        # Slow pointer follows with condition
        fast += 1
```

#### Multiple Arrays
```python
def multiple_arrays(arr1, arr2):
    p1 = p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        # Compare and process elements
        # Move appropriate pointer
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Fast & Slow Pointers
- Cycle detection
- Middle element finding
- Linked list operations

### 2. Left & Right Pointers
- Palindrome checking
- Two sum in sorted array
- Container with most water

### 3. Sliding Window Variation
- Fixed window size
- Variable window size
- Substring problems
</details>

## Implementation Strategies
<details>
<summary>Click to expand</summary>

### 1. Basic Template
```python
def two_pointers(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Process current elements
        if CONDITION:
            left += 1
        else:
            right -= 1
    return result
```

### 2. Fast-Slow Template
```python
def fast_slow(arr):
    slow = fast = 0
    
    while fast < len(arr):
        if CONDITION:
            # Move slow pointer
            slow += 1
        fast += 1
    return slow
```
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Common Complexities
| Pattern | Time | Space |
|---------|------|-------|
| Opposite Direction | O(n) | O(1) |
| Same Direction | O(n) | O(1) |
| Multiple Arrays | O(n+m) | O(1) |

### Optimization Tips
1. Avoid extra space when possible
2. Early termination conditions
3. Skip duplicate elements
</details>

## Common Mistakes
<details>
<summary>Click to expand</summary>

1. **Boundary Conditions**
   - Not handling empty arrays
   - Off-by-one errors
   - Not checking pointer validity

2. **Pointer Movement**
   - Infinite loops
   - Missing elements
   - Moving wrong pointer

3. **Edge Cases**
   - Single element
   - Duplicate elements
   - Sorted vs unsorted input
</details>

## Advanced Applications
<details>
<summary>Click to expand</summary>

### 1. Three Pointers
```python
def three_pointers(arr):
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            # Process with three pointers
```

### 2. Cyclic Sort
```python
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
```

### 3. Partition Schemes
```python
def partition(arr):
    pivot = arr[-1]
    i = j = 0
    for j in range(len(arr)):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
```
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [125. Valid Palindrome](../125/README.md)
- [167. Two Sum II](../167/README.md)

### Medium
- [15. 3Sum](../15/README.md)
- [11. Container With Most Water](../11/README.md)

### Hard
- [42. Trapping Rain Water](../42/README.md)
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Floyd's Cycle Detection Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
2. [Dutch National Flag Problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
3. [Quicksort Partitioning](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
</details>

---

*Remember: Two pointers is all about reducing the search space efficiently. When you see a problem involving array traversal or comparison, consider if two pointers could help optimize the solution.*
