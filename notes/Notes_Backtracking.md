# Backtracking Deep Dive 🔄

## Table of Contents
- [Core Concepts](#core-concepts)
- [Algorithm Template](#algorithm-template)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Problem-Solving Framework](#problem-solving-framework)

## Core Concepts
<details>
<summary>Click to expand</summary>

### What is Backtracking?
**Backtracking** is a systematic approach to solving constraint satisfaction problems by:
1. **Building solutions incrementally**
2. **Exploring all possible paths**
3. **Abandoning paths that can't lead to valid solutions**
4. **"Backtracking" to previous states when stuck**

### Key Characteristics
- **Recursive in nature**: Uses recursion to explore possibilities
- **State exploration**: Builds candidates piece by piece
- **Constraint checking**: Validates partial solutions early
- **Pruning**: Eliminates invalid branches to save time

### When to Use Backtracking
- **Combinatorial problems**: Permutations, combinations, subsets
- **Constraint satisfaction**: N-Queens, Sudoku
- **Path finding**: Maze solving, game solutions
- **Decision problems**: When you need ALL possible solutions

### Backtracking vs Other Approaches
| Approach | Use Case | Time Complexity |
|----------|----------|----------------|
| Backtracking | All solutions | O(b^d) where b=branching, d=depth |
| Dynamic Programming | Optimal solution | O(states) |
| Greedy | One good solution | O(n log n) typically |
| Brute Force | All combinations | O(n!) or worse |
</details>

## Algorithm Template
<details>
<summary>Click to expand</summary>

### Basic Backtracking Template
```python
def backtrack(path, choices):
    # Base case: solution found
    if is_solution(path):
        result.append(path.copy())  # Important: make a copy!
        return
    
    # Explore all possible choices
    for choice in choices:
        # Choose: add choice to path
        path.append(choice)
        
        # Explore: recurse with updated state
        backtrack(path, get_next_choices(choice))
        
        # Unchoose: backtrack by removing choice
        path.pop()
```

### Template with Pruning
```python
def backtrack_with_pruning(path, choices, constraints):
    # Base case
    if is_solution(path):
        result.append(path.copy())
        return
    
    # Early termination (pruning)
    if not is_valid(path, constraints):
        return
    
    for choice in choices:
        # Only explore valid choices
        if is_choice_valid(choice, path, constraints):
            path.append(choice)
            backtrack_with_pruning(path, get_next_choices(choice), constraints)
            path.pop()
```

### Template for Index-Based Problems
```python
def backtrack_indexed(nums, path, used, start_index=0):
    # Base case
    if len(path) == target_length:
        result.append(path.copy())
        return
    
    for i in range(start_index, len(nums)):
        # Skip duplicates (if array is sorted)
        if i > start_index and nums[i] == nums[i-1]:
            continue
            
        # Choose
        path.append(nums[i])
        used[i] = True
        
        # Explore (choose next start_index based on problem)
        backtrack_indexed(nums, path, used, i + 1)  # For combinations
        # backtrack_indexed(nums, path, used, 0)    # For permutations
        
        # Unchoose
        path.pop()
        used[i] = False
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Generate All Subsets
```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        # Every path is a valid subset
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # Next element starts from i+1
            path.pop()
    
    backtrack(0, [])
    return result
```

### 2. Generate All Permutations
```python
def permutations(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for num in nums:
            if num not in path:  # Or use a boolean array for efficiency
                path.append(num)
                backtrack(path)
                path.pop()
    
    backtrack([])
    return result
```

### 3. Generate All Combinations
```python
def combinations(nums, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # Next starts from i+1 (no duplicates)
            path.pop()
    
    backtrack(0, [])
    return result
```

### 4. Combination Sum (With Repeats)
```python
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return  # Pruning: invalid path
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            # Can reuse same number: start from i (not i+1)
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result
```

### 5. String Generation (Phone Numbers)
```python
def letter_combinations(digits):
    if not digits:
        return []
    
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        
        possible_letters = mapping[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Handling Duplicates
```python
def subsets_with_dup(nums):
    nums.sort()  # Sort to group duplicates
    result = []
    
    def backtrack(start, path):
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            # Skip duplicates: only use first occurrence at each level
            if i > start and nums[i] == nums[i-1]:
                continue
                
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

### 2. Palindrome Partitioning
```python
def partition(s):
    result = []
    
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path.copy())
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    backtrack(0, [])
    return result
```

### 3. N-Queens Problem
```python
def solve_n_queens(n):
    result = []
    board = ['.' * n for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append(board.copy())
            return
        
        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                backtrack(row + 1)
                # Remove queen
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    
    backtrack(0)
    return result
```

### 4. Memoization in Backtracking
```python
def word_break(s, word_dict):
    memo = {}
    
    def backtrack(start):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return True
        
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict and backtrack(end):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
    
    return backtrack(0)
```
</details>

## Problem-Solving Framework
<details>
<summary>Click to expand</summary>

### 1. Problem Analysis
**Ask yourself:**
- Do I need ALL possible solutions? → Backtracking
- Are there constraints to satisfy? → Backtracking with pruning
- Can I build solutions incrementally? → Backtracking
- Is this about combinations/permutations? → Backtracking

### 2. State Representation
**Choose your state variables:**
- **Path/Solution**: Current partial solution
- **Choices**: Available options at current state  
- **Constraints**: Rules that must be satisfied
- **Index/Position**: Where we are in the input

### 3. Base Cases
**Define when to stop:**
- **Success case**: Valid solution found
- **Failure case**: No more choices or constraints violated
- **Boundary case**: Reached end of input space

### 4. Choice and Unchoice
**The core loop:**
```python
for choice in available_choices:
    # 1. Make choice (modify state)
    make_choice(choice)
    
    # 2. Recurse (explore consequences)
    backtrack(new_state)
    
    # 3. Unmake choice (restore state)
    unmake_choice(choice)
```

### 5. Optimization Strategies
- **Early pruning**: Check constraints early
- **Sorting**: Group duplicates for easier skipping
- **Memoization**: Cache results of subproblems
- **Constraint propagation**: Use problem-specific optimizations
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [17. Letter Combinations of a Phone Number](../17/README.md)
- [22. Generate Parentheses](../22/README.md)

### Medium  
- [39. Combination Sum](../39/README.md)
- [40. Combination Sum II](../40/README.md)
- [46. Permutations](../46/README.md)
- [78. Subsets](../78/README.md)
- [90. Subsets II](../90/README.md)
- [131. Palindrome Partitioning](../131/README.md)

### Hard
- [37. Sudoku Solver](#) *(if available)*
- [51. N-Queens](#) *(if available)*
- [52. N-Queens II](#) *(if available)*
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Typical Complexities
| Problem Type | Time Complexity | Space Complexity |
|--------------|----------------|------------------|
| Subsets | O(2^n × n) | O(n) recursion depth |
| Permutations | O(n! × n) | O(n) recursion depth |
| Combinations | O(C(n,k) × k) | O(k) recursion depth |
| N-Queens | O(n!) | O(n^2) board space |

### Complexity Analysis Tips
- **Time**: Number of solutions × Cost per solution
- **Space**: Maximum recursion depth + solution storage
- **Pruning impact**: Can significantly reduce actual runtime
- **Memoization**: May reduce time but increase space
</details>

## Common Pitfalls & Best Practices
<details>
<summary>Click to expand</summary>

### ❌ Common Mistakes

1. **Forgetting to Copy Solutions**
   ```python
   # Wrong: All solutions will be the same (empty) reference
   result.append(path)
   
   # Correct: Make a copy
   result.append(path.copy())
   ```

2. **Incorrect Duplicate Handling**
   ```python
   # Wrong: May skip valid solutions
   if nums[i] == nums[i-1]:
       continue
   
   # Correct: Only skip at same recursion level
   if i > start and nums[i] == nums[i-1]:
       continue
   ```

3. **Missing Backtrack Step**
   ```python
   # Wrong: State not restored
   path.append(choice)
   backtrack(path)
   # Missing: path.pop()
   ```

4. **Inefficient State Management**
   ```python
   # Wrong: Inefficient for permutations
   if num not in path:  # O(n) check each time
   
   # Better: Use boolean array
   if not used[i]:  # O(1) check
   ```

### ✅ Best Practices

1. **Always Copy Solutions**
   ```python
   result.append(path[:])  # or path.copy()
   ```

2. **Handle Duplicates with Sorting**
   ```python
   nums.sort()  # Group duplicates together
   if i > start and nums[i] == nums[i-1]:
       continue
   ```

3. **Use Appropriate Data Structures**
   ```python
   # For permutations: boolean array
   used = [False] * len(nums)
   
   # For combinations: start index
   backtrack(i + 1, path)
   ```

4. **Implement Early Pruning**
   ```python
   # Check constraints before recursing
   if not is_valid_partial_solution(path):
       return
   ```

5. **Clear Variable Names**
   ```python
   def backtrack(start_index, current_path):
       # Much clearer than backtrack(i, path)
   ```
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Backtracking Algorithm Visualization](https://algorithm-visualizer.org/backtracking)
2. [Backtracking vs Dynamic Programming](https://stackoverflow.com/questions/3592943/difference-between-back-tracking-and-dynamic-programming)
3. [Classic Backtracking Problems](https://leetcode.com/tag/backtracking/)
</details>

---

*Remember: Backtracking is about systematic exploration of solution spaces. Master the choose-explore-unchoose pattern, and most combinatorial problems become manageable!* 