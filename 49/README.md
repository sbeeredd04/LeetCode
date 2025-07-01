        # LeetCode Problem 49: Group Anagrams

## Problem Overview
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Hashable vs Non-Hashable Types in Python

### What are Hashable Types?
A hashable object has a hash value which never changes during its lifetime. It can be used as a dictionary key or as an element of a set.

**Hashable types in Python:**
- Immutable built-in types: `int`, `float`, `str`, `bool`, `None`
- Tuples (only if all elements are hashable)
- Frozen sets
- Custom objects that implement `__hash__()` and `__eq__()`

**Non-hashable types in Python:**
- Mutable types: `list`, `dict`, `set`
- Custom objects without proper `__hash__()` implementation

### Why This Matters for Group Anagrams

The key insight for the Group Anagrams problem is that we need to group strings that are anagrams of each other. To do this efficiently, we use a dictionary where:
- **Key**: A representation that's the same for all anagrams
- **Value**: A list of strings that are anagrams

### The TypeError We Fixed

**Original problematic approach:**
```python
# This causes TypeError: unhashable type: 'list'
key = sorted(s)  # sorted() returns a list
grouped[key].append(s)  # Can't use list as dict key!
```

**Why it fails:**
- `sorted(s)` returns a `list` of characters
- Lists are mutable and therefore non-hashable
- Dictionary keys must be hashable
- Python raises: `TypeError: unhashable type: 'list'`

**Correct approach:**
```python
# This works because strings are hashable
key = ''.join(sorted(s))  # Convert list back to string
grouped[key].append(s)  # String can be used as dict key
```

## Key Generation Strategies

### 1. Sorted String Approach (Recommended)
```python
def groupAnagrams(self, strs):
    grouped = {}
    for s in strs:
        key = ''.join(sorted(s))  # "eat" -> "aet", "tea" -> "aet"
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(s)
    return list(grouped.values())
```

**Pros:**
- Simple and intuitive
- Works for all character sets
- Easy to understand

**Cons:**
- O(n * k log k) time complexity due to sorting

### 2. Character Count Tuple Approach
```python
def groupAnagrams(self, strs):
    grouped = {}
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)  # Convert list to tuple (hashable)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(s)
    return list(grouped.values())
```

**Pros:**
- O(n * k) time complexity
- More efficient for longer strings

**Cons:**
- Only works for lowercase English letters
- More complex implementation

### 3. Using defaultdict (Cleaner Code)
```python
from collections import defaultdict

def groupAnagrams(self, strs):
    grouped = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        grouped[key].append(s)
    return list(grouped.values())
```

## Common Mistakes and Solutions

### Mistake 1: Using Unsorted Characters
```python
# WRONG: Different anagrams will have different keys
key = s  # "eat" and "tea" have different keys
```

### Mistake 2: Using Non-Hashable Types as Keys
```python
# WRONG: TypeError because list is not hashable
key = sorted(s)  # Returns a list
key = list(s)    # List is not hashable
key = set(s)     # Set is not hashable (but frozenset would work)
```

### Mistake 3: Not Converting Back to Hashable Type
```python
# WRONG: Character frequency count as list
count = [0] * 26
# ... populate count ...
key = count  # List is not hashable

# CORRECT: Convert to tuple
key = tuple(count)  # Tuple is hashable
```

## Performance Analysis

### Time Complexity:
- **Sorted approach**: O(n * k log k) where n = number of strings, k = average string length
- **Count array approach**: O(n * k) - more efficient for longer strings

### Space Complexity:
- O(n * k) for storing all strings in the result

## Key Takeaways

1. **Dictionary keys must be hashable** - this is a fundamental Python requirement
2. **Immutable types are hashable** - strings, tuples, numbers, etc.
3. **Mutable types are not hashable** - lists, sets, dictionaries
4. **Convert mutable to immutable** when you need to use them as keys:
   - `list` → `tuple` using `tuple()`
   - `list of chars` → `string` using `''.join()`
5. **Anagram key generation**: Any representation that's identical for anagrams works
6. **Use `defaultdict(list)`** to avoid checking if key exists

## Related Problems
- Problem 242: Valid Anagram (single pair comparison)
- Problem 438: Find All Anagrams in a String
- Any problem requiring grouping by some characteristic 

