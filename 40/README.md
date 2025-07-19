# Combination Sum II - LeetCode 40

## Problem Overview
Given a collection of candidate numbers (which may include duplicates) and a target number, find all unique combinations in candidates where the candidate numbers sum to the target. Each number in candidates may only be used once in the combination.

---

## Solution Analysis
- **Approach:**
    - Sort the candidates to make it easier to skip duplicates.
    - Use backtracking (DFS) to explore all possible combinations.
    - At each step, decide to include the current number or skip it.
    - After backtracking (pop), use a while loop to skip over any duplicate numbers to avoid generating the same combination more than once.
- **Key Points:**
    - Sorting is essential for handling duplicates efficiently.
    - The while loop after popping ensures that we do not use the same number again at the same recursion level.
    - Only add combinations to the result if their sum equals the target.

---

## Self-Reflection & New Knowledge
### What I Learned
- Sorting the input is a simple but powerful way to handle duplicates in backtracking problems.
- If you don't skip duplicates, you will generate the same combination multiple times.
- The while loop after popping is crucial: it skips over all repeated numbers, so each unique number is only considered once at each recursion level.
- Backtracking is straightforward once you understand how to control for duplicates.

### Self-Reflection
- I realized that handling duplicates is the main challenge in this problem.
- I learned that the order of operations (sort, choose, pop, skip) is very important for correctness.
- Practicing this problem helped me get better at writing clean backtracking code that avoids repeated work.

---

## Code Walkthrough
```mermaid
flowchart TD
    Start([Start]) --> Sort[Sort candidates]
    Sort --> CallDFS[Call dfs(0, [], 0)]
    CallDFS --> CheckTarget[If total == target]
    CheckTarget -- Yes --> AddResult[Add cur.copy() to result]
    CheckTarget -- No --> CheckEnd[If i >= len(candidates) or total > target]
    CheckEnd -- Yes --> EndPath[Return]
    CheckEnd -- No --> Include[Append candidates[i] to cur]
    Include --> RecurseInclude[dfs(i+1, cur, total+candidates[i])]
    RecurseInclude --> Backtrack[Pop last from cur]
    Backtrack --> SkipDup[While next is duplicate, i += 1]
    SkipDup --> Exclude[dfs(i+1, cur, total)]
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/combination-sum-ii/)
- [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Final Thoughts
- Sorting and skipping duplicates are key for unique combinations.
- Backtracking is a flexible tool for exploring all possibilities.
- Drawing diagrams and writing out the steps helps clarify the logic.
