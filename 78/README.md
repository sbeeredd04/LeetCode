# Subsets - LeetCode 78

## Problem Overview
Given an integer array `nums`, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

---

## Solution Analysis
- **Approach:**
    - Use Depth-First Search (DFS) with backtracking to explore all possible combinations.
    - At each step, decide whether to include the current element or not.
    - Recursively build subsets and backtrack to explore other possibilities.
- **Key Concepts:**
    - Backtracking
    - Recursion
    - Power set generation

---

## Self-Reflection & New Knowledge
### What I Learned
- **Backtracking:**
    - Backtracking is a powerful technique for exploring all possible solutions by building candidates incrementally and abandoning them if they fail to satisfy constraints.
    - The use of `subset.copy()` is crucial to avoid reference issues when storing the current subset.
- **DFS for Combinatorial Problems:**
    - DFS can be used not just for traversing graphs, but also for generating combinations and subsets.
    - The recursive structure makes the code concise and easy to follow.
- **Python List Operations:**
    - Using `append`, `pop`, and `copy` methods efficiently to manage the current subset during recursion.

### Self-Reflection
- I strengthened my understanding of backtracking and how to apply it to generate all subsets.
- I learned the importance of copying lists when storing intermediate results to avoid unintended side effects.
- I appreciated how recursion can simplify complex combinatorial problems.
- Practicing this problem improved my ability to write clean and efficient recursive code.

---

## Code Walkthrough
```mermaid
flowchart TD
    Start([Start]) --> CallDFS[Call dfs(0)]
    CallDFS --> CheckEnd[If i >= len(nums)?]
    CheckEnd -- Yes --> AddSubset[Add current subset to result]
    CheckEnd -- No --> Include[Include nums[i] in subset]
    Include --> Recurse1[dfs(i+1)]
    Recurse1 --> Exclude[Backtrack: remove nums[i] from subset]
    Exclude --> Recurse2[dfs(i+1)]
    Recurse2 --> CheckEnd
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/subsets/)
- [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Final Thoughts
- Backtracking is a versatile tool for solving combinatorial problems.
- Careful handling of mutable data structures is essential in recursive algorithms.
- Visualizing the recursive process helps in understanding and debugging the solution.
