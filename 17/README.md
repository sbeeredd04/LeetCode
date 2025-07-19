# Letter Combinations of a Phone Number - LeetCode 17

## Problem Statement
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent. The mapping is the same as on a telephone keypad.

**Example:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## My Self-Reflection & Learning Journey

### 1. My Quick Solution (What I Wrote)

**My Implementation:**
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keys = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        combinations = []
        def backtrack(index, curr):
            if index >= len(digits):
                combinations.append(curr)
                return
            letters = keys[int(digits[index])]
            for letter in letters:
                backtrack(index + 1, curr + letter)
        backtrack(0, "")
        return combinations
```

### 2. My Initial Success & What Worked
- Used backtracking to generate all possible combinations
- Mapped each digit to its corresponding letters using a dictionary
- For each digit, called backtrack for every possible letter
- Handled the empty input case correctly

### 3. Critical Issues I Needed to Fix
- Initially forgot to convert `digits[index]` to `int` when accessing the dictionary, which caused a key error
- Once I fixed the type conversion, the solution worked as expected

### 4. How My Algorithm Works
- For each digit in the input, get the corresponding letters
- For each letter, recursively build up the current combination
- When the current combination length equals the input length, add it to the result

### 5. Performance Analysis
- **Time Complexity:** O(4^n × n), where n is the length of `digits` (since each digit can map to up to 4 letters)
- **Space Complexity:** O(4^n × n) for storing all combinations

### 6. What I Learned About My Coding Style
- Always check data types when using dictionary keys
- Backtracking is a simple and effective way to generate all combinations
- Handling edge cases (like empty input) is important

### 7. Best Practices I Should Follow
- Use clear variable names (`index`, `curr`, `combinations`)
- Always convert string digits to integers when using as dictionary keys
- Keep the backtracking function focused and concise

### 8. Complete Corrected Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keys = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        combinations = []
        def backtrack(index, curr):
            if index >= len(digits):
                combinations.append(curr)
                return
            letters = keys[int(digits[index])]
            for letter in letters:
                backtrack(index + 1, curr + letter)
        backtrack(0, "")
        return combinations
```

### 9. Key Takeaways & Reflection
- Backtracking is a powerful tool for generating all possible combinations
- Type conversion errors are easy to make but easy to fix with careful attention
- The problem is simple once you break it down into mapping and recursion

---

## Code Walkthrough (Mermaid Diagram)
```mermaid
flowchart TD
    Start([Start]) --> CheckEmpty[Check if digits is empty]
    CheckEmpty -- Yes --> ReturnEmpty[Return []]
    CheckEmpty -- No --> Backtrack[Call backtrack(0, "")]
    Backtrack --> ForEachDigit[For each digit in digits]
    ForEachDigit --> ForEachLetter[For each letter in keys[digit]]
    ForEachLetter --> Recurse[Recurse with next index and curr + letter]
    Recurse --> End[If index == len(digits), add curr to result]
```

---

## Useful Resources
- [LeetCode Problem Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [Python Recursion Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

## Final Thoughts
- This problem is a classic example of using backtracking for combinations
- Careful attention to data types and edge cases is important for correctness
- The recursive approach is clean and easy to understand
