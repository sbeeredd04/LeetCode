# Combination Sum - LeetCode 39

## Problem Overview
Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers sum to `target`. Each number in `candidates` may be used an unlimited number of times. The combinations must not contain duplicates.

---

## Solution Analysis
- **Approach:**
    - Use backtracking (DFS) to explore all possible combinations.
    - At each step, decide to include the current number (and stay at the same index) or skip to the next number.
    - Only add combinations to the result if their sum equals the target.
    - Avoid duplicates by always moving forward in the list (never going back to previous indices).
- **Key Points:**
    - Use `curr.copy()` to avoid reference issues when saving combinations.
    - The recursive function takes the current index and the current combination.
    - If the sum exceeds the target or we run out of numbers, we stop that path.

---

## Self-Reflection & New Knowledge
### What I Learned
- If you build combinations by just appending numbers, you can get duplicate combinations in different orders (e.g., [2,3,2] and [2,2,3]).
- To avoid duplicates, always decide at each step: either include the current number (and stay at the same index) or skip it (move to the next index).
- Backtracking is powerful for exploring all possible options, but you must control the order and choices to avoid repeated results.
- Using `.copy()` is important to save the current state of the combination before backtracking.

### Self-Reflection
- I learned that the way you structure your recursive calls can affect whether you get duplicate results.
- I realized that thinking about the problem as a series of choices (include or skip) makes the code much simpler and avoids bugs.
- Practicing this problem helped me understand how to use indices to control recursion and avoid duplicates.

---

## Code Walkthrough
```mermaid
flowchart TD
    Start([Start]) --> CallDFS[Call dfs(0, [])]
    CallDFS --> CheckBase[If sum(curr) > target or i >= len(candidates)]
    CheckBase -- Yes --> EndPath[Return]
    CheckBase -- No --> CheckTarget[If sum(curr) == target]
    CheckTarget -- Yes --> AddResult[Add curr.copy() to result]
    CheckTarget -- No --> Include[Append candidates[i] to curr]
    Include --> RecurseInclude[dfs(i, curr)]
    RecurseInclude --> Backtrack[Pop last from curr]
    Backtrack --> Exclude[dfs(i+1, curr)]
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/combination-sum/)
- [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Final Thoughts
- Backtracking is a simple but powerful way to try all possibilities.
- Always think about how to avoid duplicates by controlling your choices and recursion.
- Drawing a diagram or writing out the choices can help you understand and debug your code.
