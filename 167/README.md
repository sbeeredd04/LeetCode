# 167. Two Sum II - Input Array Is Sorted

## Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 ≤ index1 < index2 ≤ numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

## Examples
```python
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: numbers[0] + numbers[1] = 2 + 7 = 9
So we return [1, 2] (1-indexed)

Input: numbers = [2,3,4], target = 6
Output: [1,3] 
Explanation: numbers[0] + numbers[2] = 2 + 4 = 6

Input: numbers = [-1,0], target = -1
Output: [1,2]
```

## Constraints
- `2 ≤ numbers.length ≤ 3 * 10^4`
- `-1000 ≤ numbers[i] ≤ 1000`
- `numbers` is sorted in **non-decreasing** order
- `-1000 ≤ target ≤ 1000`
- The tests are generated such that there is **exactly one solution**

---

## 🧠 Analysis of Current Solution

### ❌ **Current Implementation Issues**
```python
# BUGGY CODE:
if total == target: 
    break
elif total <= target:    # ❌ WRONG: should be total < target
    left += 1
elif total >= target:    # ❌ WRONG: should be total > target  
    right -= 1
```

### 🐛 **Problems Identified:**
1. **Logic Error**: Using `<=` and `>=` instead of `<` and `>`
2. **Infinite Loop Risk**: When `total == target`, we break, but the conditions overlap
3. **Unreachable Code**: The `elif` conditions can both be true when `total == target`

---

## ✅ Optimal Solution: Two Pointers

### 💡 **Key Insight**: Leverage the Sorted Property!

Since the array is sorted, we can use two pointers to efficiently find the target sum.

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1   # Need larger sum, move left pointer right
        else:  # current_sum > target
            right -= 1  # Need smaller sum, move right pointer left
    
    # This should never be reached given problem constraints
    return []
```

### 🎯 **Why This Works:**

| Scenario | Current Sum vs Target | Action | Reasoning |
|----------|----------------------|---------|-----------|
| `sum < target` | Too small | `left += 1` | Need larger numbers → move left pointer right |
| `sum > target` | Too big | `right -= 1` | Need smaller numbers → move right pointer left |
| `sum == target` | Perfect match | Return indices | Found our answer! |

---

## 🔍 Step-by-Step Walkthrough

### Example: `numbers = [2,7,11,15], target = 9`

```
Initial: [2, 7, 11, 15]   target = 9
          ↑           ↑
        left        right

Step 1: sum = 2 + 15 = 17 > 9 → move right left
        [2, 7, 11, 15]
         ↑      ↑
       left   right

Step 2: sum = 2 + 11 = 13 > 9 → move right left  
        [2, 7, 11, 15]
         ↑  ↑
       left right

Step 3: sum = 2 + 7 = 9 == 9 → Found! Return [1, 2]
```

---

## ⚡ Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two Pointers** | **O(n)** | **O(1)** | Optimal for sorted array |
| **Hash Map** | O(n) | O(n) | Overkill since array is sorted |
| **Brute Force** | O(n²) | O(1) | Doesn't leverage sorted property |

### 🔬 **Why O(n) Time?**
- Each element is visited **at most once**
- In worst case, we traverse the entire array once
- No nested loops or repeated work

---

## 🛠️ Alternative Approaches

### 📋 Approach 1: Hash Map (Like Original Two Sum)
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement] + 1, i + 1]  # 1-indexed
        seen[num] = i
    return []
```
- **Pros**: Same as Two Sum I approach
- **Cons**: O(n) extra space, doesn't leverage sorted property

### 🔍 Approach 2: Binary Search
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i, num in enumerate(numbers):
        complement = target - num
        # Binary search for complement in remaining array
        left, right = i + 1, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1
    return []
```
- **Time**: O(n log n)
- **Space**: O(1)
- **Cons**: More complex, slower than two pointers

---

## 🎓 Key Insights & Best Practices

### 🚀 **What Makes Two Pointers Optimal:**
1. **Leverages Sorted Property**: Uses the fact that array is sorted
2. **Eliminates Redundancy**: No need to check all pairs
3. **Space Efficient**: Only uses two pointers
4. **Single Pass**: Each element visited at most once

### 🔧 **Implementation Tips:**
1. **Pointer Initialization**: Start at both ends
2. **Index Conversion**: Remember to convert to 1-indexed in return
3. **Clear Logic**: Use `<` and `>`, not `<=` and `>=` for non-target cases
4. **Early Return**: Return immediately when target found

### 🐛 **Common Pitfalls:**
- ❌ Confusing 0-indexed vs 1-indexed returns
- ❌ Using `<=` and `>=` in conditions (creates overlaps)
- ❌ Not leveraging the sorted property
- ❌ Forgetting to handle edge cases

---

## 🔗 Relationship to Other Problems

### **Problem Evolution:**
- [**#1 Two Sum**](../1/) → Unsorted array, use hash map
- [**#167 Two Sum II**](../167/) → **Sorted array, use two pointers** ⭐
- [**#15 3Sum**](../15/) → Extension to three numbers
- [**#18 4Sum**](../18/) → Extension to four numbers

### **Two Pointer Pattern Applications:**
- [**#125 Valid Palindrome**](../125/) → String validation
- [**#11 Container With Most Water**](../11/) → Area maximization
- [**#42 Trapping Rain Water**](../42/) → Complex pointer movement

---

## 📊 Performance Comparison

| Input Size | Two Pointers | Hash Map | Binary Search |
|------------|-------------|----------|---------------|
| 100 | ~50 ops | ~100 ops | ~664 ops |
| 1,000 | ~500 ops | ~1,000 ops | ~9,966 ops |
| 10,000 | ~5,000 ops | ~10,000 ops | ~132,877 ops |

**Two pointers is consistently 2x faster than hash map and 20x+ faster than binary search!**

---

## 🏆 Why Two Pointers is Perfect Here

1. **🎯 Optimal Complexity**: O(n) time, O(1) space
2. **🚀 Leverages Constraints**: Uses sorted array property
3. **💡 Intuitive Logic**: Move towards target systematically  
4. **🔧 Simple Implementation**: Clean, readable code
5. **⚡ Performance**: Minimal memory access, cache-friendly

The two-pointer approach is not just optimal—it's the **intended solution** for this problem, showcasing how constraints (sorted array) can lead to elegant algorithms!