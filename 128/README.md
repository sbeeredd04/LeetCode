# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n) time**.

## Examples
```python
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]  
Output: 9
```

## Constraints
- `0 ≤ nums.length ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`

---

## 🧠 Thought Process Evolution

### ❌ First Attempt: Bidirectional Expansion
```python
# WRONG: Time Limit Exceeded
def longestConsecutive(self, nums: List[int]) -> int:
    seen = set()
    max_length = 1
    
    for num in nums:
        if num in seen: continue
        seen.add(num)
        
        # Count left
        left = num - 1
        left_length = 1
        while left in seen:
            left_length += 1
            left -= 1
            
        # Count right  
        right = num + 1
        right_length = 1
        while right in seen:
            right_length += 1
            right += 1
            
        current_length = left_length + right_length - 1
        max_length = max(max_length, current_length)
```

### ⚠️ **Why This Failed:**
- **Redundant Work**: For sequence `[1,2,3,4]`, we count the same sequence 4 times!
- **Time Complexity**: O(n²) in worst case - violates the O(n) requirement
- **Inefficient**: Each number triggers a full bidirectional scan

---

## ✅ Optimal Solution: Sequence Start Detection

### 💡 **Key Insight**: Only Start from Sequence Beginnings!

A number `x` is the **start** of a sequence if `x-1` is NOT in the array.

```python
def longestConsecutive(self, nums: List[int]) -> int:
    seen = set(nums)  # O(1) lookup
    longest_streak = 0
    
    for num in seen:
        # 🔍 Check if this is a sequence start
        if num - 1 not in seen:
            current_num = num
            current_streak = 1
            
            # 📏 Count sequence length going right only
            while current_num + 1 in seen:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
```

### 🎯 **Why This Works:**

| Array | Sequence Starts | Sequences Found |
|-------|----------------|-----------------|
| `[100,4,200,1,3,2]` | `100`, `200`, `1` | `[100]`, `[200]`, `[1,2,3,4]` |
| `[0,3,7,2,5,8,4,6,1]` | `0` | `[0,1,2,3,4,5,6,7,8]` |

---

## 🔍 Step-by-Step Walkthrough

### Example: `nums = [100, 4, 200, 1, 3, 2]`

1. **Create Set**: `seen = {100, 4, 200, 1, 3, 2}`

2. **Check each number:**
   - `num = 100`: `99 ∉ seen` → **START** → sequence: `[100]` → length = 1
   - `num = 4`: `3 ∈ seen` → **NOT START** → skip
   - `num = 200`: `199 ∉ seen` → **START** → sequence: `[200]` → length = 1  
   - `num = 1`: `0 ∉ seen` → **START** → sequence: `[1,2,3,4]` → length = 4
   - `num = 3`: `2 ∈ seen` → **NOT START** → skip
   - `num = 2`: `1 ∈ seen` → **NOT START** → skip

3. **Result**: `max(1, 1, 4) = 4`

---

## ⚡ Complexity Analysis

| Metric | Bidirectional | Optimal |
|--------|---------------|---------|
| **Time** | O(n²) | **O(n)** |
| **Space** | O(n) | **O(n)** |
| **Passes** | Multiple per sequence | Single per sequence |

### 🔬 **Why O(n) Time?**
- Each number is visited **at most twice**:
  1. Once in the outer loop
  2. Once in the inner while loop (only for sequence members)
- Total operations ≤ 2n → **O(n)**

---

## 🛠️ Alternative Approaches

### 📋 Approach 1: Sort + Linear Scan
```python
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums: return 0
    
    nums = sorted(set(nums))  # Remove duplicates & sort
    max_len = current_len = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    
    return max(max_len, current_len)
```
- **Time**: O(n log n) - slower due to sorting
- **Space**: O(1) - if we can modify input

### 🗺️ Approach 2: Union-Find
```python
def longestConsecutive(self, nums: List[int]) -> int:
    parent = {}
    size = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
            size[x] = 1
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            size[py] += size[px]
    
    for num in nums:
        find(num)
        if num + 1 in parent:
            union(num, num + 1)
        if num - 1 in parent:
            union(num, num - 1)
    
    return max(size.values()) if nums else 0
```
- **Time**: O(n α(n)) ≈ O(n) - where α is inverse Ackermann
- **Space**: O(n)
- **Complexity**: Overkill for this problem

---

## 🎓 Key Takeaways

1. **🎯 Identify Redundancy**: Don't count the same sequence multiple times
2. **🚀 Sequence Start Optimization**: `num-1 not in seen` is the magic condition
3. **⚡ Set vs Array**: O(1) lookup vs O(n) lookup makes all the difference
4. **📊 Amortized Analysis**: Sometimes apparent O(n²) is actually O(n)
5. **🔄 Edge Cases**: Handle empty arrays gracefully

## 🐛 Common Pitfalls

- ❌ Forgetting to handle empty arrays
- ❌ Using lists instead of sets for membership testing
- ❌ Counting sequences from every number (not just starts)
- ❌ Off-by-one errors in sequence length calculation
- ❌ Not handling duplicates properly

---

## 🔗 Related Problems

- [📋 **#217 Contains Duplicate**](../217/) - Set membership basics
- [🔢 **#268 Missing Number**](../268/) - Array analysis patterns  
- [⚡ **#41 First Missing Positive**](../41/) - O(n) array techniques
- [🎯 **#3 Longest Substring Without Repeating**](../3/) - Sliding window on sequences