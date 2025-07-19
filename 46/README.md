# Permutations - LeetCode 46

## Problem Overview
Given an array `nums` of distinct integers, return all possible permutations. Each permutation must use every element exactly once.

---

## Solution Analysis
- **Approach:**
    - Use backtracking (DFS) to build permutations by choosing each available number in turn.
    - At each step, add a number to the current permutation, remove it from the available set, and recurse.
    - When the current permutation has length `n`, add it to the result.
- **Code Example:**
    ```python
    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            res = []
            n = len(nums)
            def dfs(curr, available):
                if len(curr) == n:
                    res.append(curr.copy())
                    return
                for num in available:
                    curr.append(num)
                    next_available = available.copy()
                    next_available.remove(num)
                    dfs(curr, next_available)
                    curr.pop()
            dfs([], set(nums))
            return res
    ```
- **Time Complexity:**
    - There are `n!` possible permutations for `n` numbers.
    - For each permutation, copying the list takes O(n) time.
    - **Total time complexity:** O(n × n!)
- **Possible Improvements:**
    - The current approach is optimal for generating all permutations.
    - For large `n`, memory and time will grow very fast (factorial growth is unavoidable).
    - Using a list for `available` instead of a set may be slightly faster for small `n`.
    - For even more efficiency, use an index-based approach or a boolean array to track used elements:
    ```python
    def permute(nums):
        res = []
        n = len(nums)
        used = [False] * n
        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    used[i] = False
        dfs([])
        return res
    ```
    - This avoids copying and removing from sets/lists, and is more efficient for larger inputs.

---

## Self-Reflection & New Knowledge
### What I Learned
- Backtracking is a natural fit for permutation problems.
- Using a set for available numbers makes it easy to track which numbers are left.
- The time complexity is inherently O(n × n!) for generating all permutations, so the current solution is as efficient as possible for this problem.
- Copying lists is necessary to avoid reference issues in recursive solutions.
- Using a boolean array for visited status can make the code faster and use less memory for large inputs.

### Self-Reflection
- I found this problem straightforward after practicing other backtracking problems.
- I learned to appreciate the power of recursion for generating all possible arrangements.
- I realized that for permutation problems, the main challenge is handling the exponential growth in possibilities.
- This problem helped reinforce my understanding of backtracking and recursion.

---

## Code Walkthrough
```mermaid
flowchart TD
    Start([Start]) --> CallDFS[Call dfs([], set(nums))]
    CallDFS --> CheckLen[If len(curr) == n]
    CheckLen -- Yes --> AddResult[Add curr.copy() to result]
    CheckLen -- No --> ForEach[For each num in available]
    ForEach --> AppendNum[Append num to curr]
    AppendNum --> RemoveNum[Remove num from available]
    RemoveNum --> Recurse[dfs(curr, available - {num})]
    Recurse --> PopNum[Pop num from curr]
    PopNum --> ForEach
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/permutations/)
- [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Final Thoughts
- Backtracking is the best approach for generating all permutations.
- The factorial time complexity is unavoidable for this problem.
- Practice with similar problems helps build confidence and skill in recursion and backtracking.
- For very large inputs, consider iterative or index-based solutions to optimize performance, but the core complexity remains O(n × n!).
