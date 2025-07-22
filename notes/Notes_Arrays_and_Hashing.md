# Arrays and Hashing Deep Dive 🎯

## Table of Contents
- [Key Patterns](#key-patterns)
- [Common Techniques](#common-techniques)
- [Time Complexity Analysis](#time-complexity-analysis)
- [Problem-Solving Framework](#problem-solving-framework)
- [Common Pitfalls](#common-pitfalls)
- [Advanced Techniques](#advanced-techniques)

## Key Patterns
<details>
<summary>Click to expand</summary>

### 1. Frequency Counter Pattern
- Use hash maps to count occurrences
- Useful for: anagrams, duplicates, matching
```python
from collections import Counter
frequency = Counter(array)  # or defaultdict(int)
```

### 2. Two-Pass Hash Table
- First pass: gather information
- Second pass: use the information
```python
# Example: find complement in Two Sum
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### 3. Set Operations
- For quick lookups and deduplication
- Useful for: unique elements, intersections
```python
unique_elements = set(array)
intersection = set1 & set2
union = set1 | set2
```
</details>

## Common Techniques
<details>
<summary>Click to expand</summary>

### 1. Dictionary as Cache
```python
cache = {}  # Memoization/caching results
```

### 2. Using defaultdict
```python
from collections import defaultdict
groups = defaultdict(list)  # Automatic initialization
```

### 3. Counter for frequencies
```python
from collections import Counter
char_count = Counter(string)
```
</details>

## Time Complexity Analysis
<details>
<summary>Click to expand</summary>

| Operation | Hash Table | Array |
|-----------|------------|-------|
| Insert    | O(1) avg   | O(1)  |
| Delete    | O(1) avg   | O(n)  |
| Search    | O(1) avg   | O(n)  |
| Space     | O(n)       | O(1)  |

### Common Operations Cost
- Hash table collision handling: O(n) worst case
- Array resizing: O(n) amortized
- Dictionary comprehension: O(n)
</details>

## Problem-Solving Framework
<details>
<summary>Click to expand</summary>

1. **First, Consider Hash Table**
   - Is lookup optimization needed?
   - Are we tracking frequencies?
   - Do we need key-value pairs?

2. **Then, Consider Array Properties**
   - Is order important?
   - Do we need constant-time access?
   - Are we doing in-place modifications?

3. **Finally, Consider Space-Time Tradeoffs**
   - Can we use extra space for better time?
   - Is in-place modification required?
</details>

## Common Pitfalls
<details>
<summary>Click to expand</summary>

1. **Hash Collisions**
   - Using mutable types as keys
   - Not handling collisions properly

2. **Array Modifications**
   - Modifying array while iterating
   - Not considering edge cases

3. **Space Complexity**
   - Creating unnecessary copies
   - Not utilizing in-place operations
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Custom Hash Functions
```python
class CustomHash:
    def __hash__(self):
        return hash((self.attr1, self.attr2))
```

### 2. Rolling Hash
```python
def rolling_hash(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 1000000007
    return h
```

### 3. Perfect Hashing
- When dataset is static
- Guarantees O(1) lookup
</details>

## Related LeetCode Problems
<details>
<summary>Click to expand</summary>

### Easy
- [1. Two Sum](../1/README.md)
- [242. Valid Anagram](../242/README.md)

### Medium
- [49. Group Anagrams](../49/README.md)
- [347. Top K Frequent Elements](../347/README.md)

### Hard
- [128. Longest Consecutive Sequence](../128/README.md)
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Python Collections Documentation](https://docs.python.org/3/library/collections.html)
2. [Hash Table Implementation Guide](https://en.wikipedia.org/wiki/Hash_table)
3. [Array Data Structure](https://en.wikipedia.org/wiki/Array_data_structure)
</details>

---

*Remember: The key to mastering arrays and hashing is understanding when to use which data structure and recognizing common patterns in problems.*
