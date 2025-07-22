# Sliding Window Deep Dive 🪟

## Table of Contents
- [Core Concepts](#core-concepts)
- [Window Types](#window-types)
- [Implementation Strategies](#implementation-strategies)
- [Time & Space Analysis](#time--space-analysis)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)

## Core Concepts
<details>
<summary>Click to expand</summary>

### What is a Sliding Window?
A sliding window is an abstract concept commonly used to solve array/string problems. It involves a window that slides over data to track a subset of elements.

### Key Components
```python
def sliding_window_template():
    left = right = 0
    window = {}  # or set(), list(), etc.
    
    while right < len(data):
        # 1. Expand window
        add_to_window(data[right])
        right += 1
        
        # 2. Contract window if needed
        while WINDOW_CONDITION_BROKEN:
            remove_from_window(data[left])
            left += 1
        
        # 3. Update result if needed
        update_result()
```
</details>

## Window Types
<details>
<summary>Click to expand</summary>

### 1. Fixed Size Window
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])  # Initial window
    result = window_sum
    
    for i in range(k, len(arr)):
        # Slide window: remove leftmost, add rightmost
        window_sum = window_sum - arr[i-k] + arr[i]
        result = max(result, window_sum)
    
    return result
```

### 2. Variable Size Window
```python
def variable_window(s):
    left = right = 0
    window = set()
    max_len = 0
    
    while right < len(s):
        while s[right] in window:  # Contract if duplicate
            window.remove(s[left])
            left += 1
        window.add(s[right])  # Expand
        max_len = max(max_len, right - left + 1)
        right += 1
    
    return max_len
```

### 3. Dynamic Condition Window
```python
def dynamic_window(s, k):
    left = right = 0
    max_count = 0
    count = {}
    
    while right < len(s):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
            
        right += 1
    
    return right - left
```
</details>

## Implementation Strategies
<details>
<summary>Click to expand</summary>

### 1. Hash Map Window
```python
def string_window():
    window = {}  # Character frequency
    needed = {}  # Target frequency
    
    def window_contains_target():
        return all(
            char in window and window[char] >= needed[char]
            for char in needed
        )
```

### 2. Counter Window
```python
from collections import Counter

def counter_window():
    window = Counter()
    target = Counter(target_string)
    
    def is_valid():
        return window & target == target
```

### 3. Numeric Window
```python
def sum_window(nums, target):
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
```
</details>

## Time & Space Analysis
<details>
<summary>Click to expand</summary>

### Common Complexities

| Operation | Time | Space |
|-----------|------|-------|
| Fixed Window | O(n) | O(1) or O(k) |
| Variable Window | O(n) | O(k) |
| String Window | O(n) | O(k) |

Where:
- n = length of input array/string
- k = size of window or unique elements

### Optimization Tips
1. Use sliding window when looking for:
   - Subarrays/substrings with conditions
   - Maximum/minimum size windows
   - Contiguous sequences
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Character Frequency Pattern
Used in string permutation/anagram problems
```python
def has_permutation(s1, s2):
    target = Counter(s1)
    window = Counter()
    
    for i in range(len(s2)):
        window[s2[i]] += 1
        if i >= len(s1):
            window[s2[i-len(s1)]] -= 1
            if window[s2[i-len(s1)]] == 0:
                del window[s2[i-len(s1)]]
        if window == target:
            return True
    return False
```

### 2. Maximum Length Pattern
For finding longest valid substring
```python
def max_length_pattern(s):
    left = right = 0
    max_len = curr_len = 0
    
    while right < len(s):
        # Expand window
        curr_len += 1
        
        # Contract if invalid
        while not is_valid():
            curr_len -= 1
            left += 1
            
        # Update result
        max_len = max(max_len, curr_len)
        right += 1
```

### 3. Minimum Window Pattern
For finding smallest window with conditions
```python
def min_window_pattern(s, target):
    need = Counter(target)
    missing = len(target)
    left = start = end = 0
    
    for right, char in enumerate(s):
        missing -= (need[char] > 0)
        need[char] -= 1
        
        if not missing:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not end or right-left < end-start:
                start, end = left, right+1
    
    return s[start:end]
```
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Medium
- [3. Longest Substring Without Repeating Characters](../3/README.md)
- [424. Longest Repeating Character Replacement](../424/README.md)
- [567. Permutation in String](../567/README.md)

Each problem showcases a different sliding window pattern:
- Problem 3: Variable size window with unique elements
- Problem 424: Fixed window with character count
- Problem 567: Fixed window with character frequency matching
</details>

## Common Mistakes
<details>
<summary>Click to expand</summary>

### 1. Window Bounds
```python
# WRONG
while right < len(s):
    # Accessing right before increment
    process(s[right])
    right += 1

# RIGHT
while right < len(s):
    # Increment after processing
    process(s[right])
    right += 1
```

### 2. Window State Updates
```python
# WRONG - Not updating window state correctly
window[s[right]] += 1
right += 1
# ... later
window[s[left]] -= 1  # Forgot to check if zero

# RIGHT
window[s[right]] += 1
right += 1
# ... later
window[s[left]] -= 1
if window[s[left]] == 0:
    del window[s[left]]
```

### 3. Condition Checking
```python
# WRONG - Checking condition after movement
right += 1
if is_valid(window):  # Too late

# RIGHT
if is_valid(window):
    update_result()
right += 1
```
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Sliding Window Technique](https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem)
2. [Window Patterns Guide](https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b)
3. [Time Complexity Analysis](https://www.geeksforgeeks.org/window-sliding-technique/)
</details>

---

*Remember: The key to sliding window problems is identifying when to expand and when to contract the window. The window manipulation should maintain your required conditions while minimizing unnecessary operations.*
