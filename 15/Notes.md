# 15. 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k` 
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must **not contain duplicate triplets**.

## Examples
```python
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []

Input: nums = [0,0,0]
Output: [[0,0,0]]
```

---

## 🧠 My Initial Approach & Evolution

### 💭 **Initial Intuition**
> "Fix the rightmost element `k`, then use two pointers `i` and `j` to find pairs that sum to `-nums[k]`"

### 🔧 **My Implementation Strategy**
```python
# My approach: Fix k (rightmost), vary i and j
k = len(nums) - 1
while k >= 2:  # ✅ FIXED: was k > 2 initially
    i, j = 0, k - 1
    # Use two pointers between i and j
    while i < j:
        total = nums[i] + nums[j] + nums[k]
        # ... handle cases
    k -= 1
```

### ⚠️ **Critical Mistake Made**
```python
# ❌ WRONG: 
while k > 2:  # This skips k=2, missing valid triplets!

# ✅ CORRECT:
while k >= 2: # Need at least 3 elements: indices 0,1,2
```

**Why this matters**: For array `[a, b, c]`, we need `k=2` to check triplet `(0,1,2)`!

---

## 🔍 Current Solution Analysis

### ✅ **What's Working**
1. **Sorting first**: `nums.sort()` enables two-pointer technique
2. **Correct bounds**: `k >= 2` ensures minimum 3 elements
3. **Two-pointer logic**: Correctly moves `i` and `j` based on sum
4. **Duplicate skipping**: Handles adjacent duplicates within inner loop

### ❌ **Issues & Inefficiencies**
1. **Incomplete duplicate handling**: Only skips duplicates for `i` and `j`, not `k`
2. **Set conversion overhead**: `[list(x) for x in set(tuple(x) for x in result)]`
3. **Redundant work**: Processes some duplicate configurations

### 🐛 **Example of Missing Duplicate Handling**
```python
nums = [-2, 0, 0, 2, 2]  # After sorting
# Your code might generate: [[-2,0,2], [-2,0,2]] 
# Because it doesn't skip duplicate k values
```

---

## ✅ Optimal Solution: Fix First Element

### 💡 **Better Intuition**: Fix the leftmost element instead!

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):  # Fix first element
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1  # Two pointers
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for both pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif total < 0:
                left += 1   # Need larger sum
            else:
                right -= 1  # Need smaller sum
    
    return result
```

---

## 🔄 Approach Comparison

| Aspect | My Approach (Fix K) | Optimal (Fix I) |
|--------|-------------------|-----------------|
| **Fixed Element** | Rightmost (`k`) | Leftmost (`i`) |
| **Duplicate Handling** | Partial (missing `k`) | Complete (all positions) |
| **Code Clarity** | More complex | Cleaner structure |
| **Performance** | O(n³) worst case | O(n²) guaranteed |
| **Memory** | Extra set conversion | Direct result building |

---

## 🎯 Key Insights & Lessons

### 🚀 **Why Fix First Element is Better**
1. **Natural iteration**: `for i in range()` is more intuitive than `while k >= 2`
2. **Easier duplicate skipping**: Skip `i` duplicates with simple `continue`
3. **Clearer bounds**: No complex k-index management
4. **Standard pattern**: Matches typical 3Sum implementations

### 🔧 **Critical Implementation Details**

#### **Boundary Conditions**
```python
# ✅ Correct bounds
for i in range(len(nums) - 2):  # Leave room for j, k
left, right = i + 1, len(nums) - 1  # Ensure i < left < right
```

#### **Duplicate Handling Strategy**
```python
# Skip duplicate i values
if i > 0 and nums[i] == nums[i-1]:
    continue

# Skip duplicate left/right values  
while left < right and nums[left] == nums[left + 1]:
    left += 1
while left < right and nums[right] == nums[right - 1]:
    right -= 1
```

---

## ⚡ Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute Force** | O(n³) | O(1) | Check all triplets |
| **My Approach** | O(n²) + overhead | O(k) | Set conversion cost |
| **Optimal** | **O(n²)** | **O(1)** | Clean, no overhead |

### 🔬 **Why O(n²)?**
- Outer loop: O(n) iterations
- Inner two-pointer: O(n) per iteration
- Total: O(n) × O(n) = O(n²)

---

## 🐛 Common Pitfalls & Watch-Outs

### ❌ **Boundary Errors**
```python
# Wrong: Doesn't leave room for 3 elements
for i in range(len(nums)):

# Right: Ensures space for i, left, right  
for i in range(len(nums) - 2):
```

### ❌ **Incomplete Duplicate Handling**
```python
# Wrong: Only handles inner duplicates
# Missing: Skip duplicate i values

# Right: Handle ALL duplicate positions
if i > 0 and nums[i] == nums[i-1]: continue
```

### ❌ **Pointer Management**
```python
# Wrong: Forget to move both pointers after finding triplet
left += 1  # Missing: right -= 1

# Right: Move both pointers
left += 1
right -= 1
```

---

## 🎓 What I Learned

### 🔄 **Algorithm Evolution**
1. **Started with**: Fix rightmost element (less common)
2. **Realized**: Leftmost fixing is more natural 
3. **Improved**: Better duplicate handling
4. **Optimized**: Removed unnecessary set conversion

### 💡 **Pattern Recognition**
- **3Sum** → Fix one element + Two Sum on remainder
- **Two pointers** work best on sorted arrays
- **Duplicate handling** requires careful boundary checks

### 🚀 **Best Practices Applied**
- Sort first to enable two-pointer technique
- Handle duplicates at the source, not post-processing
- Use clear, standard iteration patterns
- Maintain proper loop invariants

---

## 🔗 Related Problems

- [**#1 Two Sum**](../1/) - Foundation pattern
- [**#167 Two Sum II**](../167/) - Two pointers on sorted array  
- [**#18 4Sum**](../18/) - Extension to 4 elements
- [**#16 3Sum Closest**](../16/) - Variation of 3Sum

The 3Sum problem perfectly demonstrates how **sorting + two pointers** creates elegant O(n²) solutions for sum-based problems! 🎯