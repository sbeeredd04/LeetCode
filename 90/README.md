# Subsets II - LeetCode 90

## Problem Statement
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

**Example:**
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

---

## My Self-Reflection & Learning Journey

### 1. My Quick Solution (What I Wrote)

**My Implementation:**
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i, curr):
            if i >= len(nums):
                res.add(tuple(curr))
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)
        backtrack(0, [])
        res = list(res)
        res.sort()
        return res
```

### 2. My Initial Success & What Worked

**✅ What I Got Right:**
- Used backtracking to generate all possible subsets
- Sorted the input to help with duplicate handling
- Used a set to avoid duplicate subsets
- Converted lists to tuples for set storage

**✅ Why This Was Easy for Me:**
- Familiar with backtracking from previous problems
- Recognized the need to handle duplicates
- Knew that sets can be used for uniqueness

### 3. Critical Issues I Needed to Fix

**🚫 Major Bug in My Logic:**
- If I added lists directly to the result, duplicate subsets appeared when `nums` had duplicates
- Needed to convert lists to tuples for set storage
- Sorting both input and result was necessary for consistent output

### 4. How My Algorithm Should Actually Work

**Corrected Version:**
- Sort the input list
- Use backtracking to explore all subset possibilities
- Store each subset as a tuple in a set to avoid duplicates
- Convert the set back to a sorted list at the end

### 5. Alternative Approach: Skipping Duplicates During Backtracking

Instead of using a set, you can skip duplicates during recursion:
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, curr):
            res.append(curr.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res
```

### 6. Performance Analysis
- **Time Complexity:** O(2^n × n) (since each subset can be up to length n)
- **Space Complexity:** O(2^n × n) for storing all subsets
- Using a set is simple but may use more memory; skipping duplicates during recursion is more efficient

### 7. What I Learned About My Coding Style
- Sets are a quick fix for uniqueness, but skipping duplicates in recursion is more elegant
- Sorting is a powerful tool for handling duplicates
- Always test with duplicate-heavy inputs
- Backtracking is a flexible and reusable pattern

### 8. My Debugging Process
- Tested with inputs like [1,2,2] and [2,2,2]
- Checked that no duplicate subsets appeared in the output
- Compared set-based and skip-based approaches for correctness

### 9. Best Practices I Should Follow
- Sort input before backtracking when duplicates are possible
- Use sets for uniqueness if unsure, but prefer skipping duplicates for efficiency
- Convert lists to tuples for set storage
- Always return sorted results for consistency

### 10. Complete Corrected Solutions

**Set-Based Solution:**
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i, curr):
            if i >= len(nums):
                res.add(tuple(curr))
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)
        backtrack(0, [])
        res = list(res)
        res.sort()
        return res
```

**Skip-Duplicates Solution:**
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, curr):
            res.append(curr.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res
```

### 11. Key Takeaways & Reflection
- Handling duplicates is crucial in combinatorial problems
- Sets are easy but skipping duplicates is more efficient
- Sorting is almost always needed when duplicates are present
- Backtracking is a powerful and reusable tool
- Testing with edge cases is important for correctness

---

## Code Walkthrough (Mermaid Diagram)
```mermaid
flowchart TD
    Start([Start]) --> Sort[Sort nums]
    Sort --> CallBacktrack[Call backtrack(0, [])]
    CallBacktrack --> CheckEnd[If i >= len(nums)]
    CheckEnd -- Yes --> AddTuple[Add tuple(curr) to set]
    CheckEnd -- No --> Include[Append nums[i] to curr]
    Include --> Recurse1[backtrack(i+1, curr)]
    Recurse1 --> Pop[Pop nums[i] from curr]
    Pop --> Exclude[backtrack(i+1, curr)]
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/subsets-ii/)
- [Python Set Documentation](https://docs.python.org/3/library/stdtypes.html#set)

---

## Final Thoughts
- Handling duplicates is crucial in combinatorial problems
- Using sets and sorting are simple but effective tools for ensuring unique results
- Backtracking remains a versatile and powerful approach for generating all combinations
