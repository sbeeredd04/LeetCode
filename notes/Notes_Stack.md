# Stack Deep Dive 📚

## Table of Contents
- [Core Concepts](#core-concepts)
- [Implementation Strategies](#implementation-strategies)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Time & Space Complexity](#time--space-complexity)
- [Common Pitfalls](#common-pitfalls)

## Core Concepts
<details>
<summary>Click to expand</summary>

### Basic Stack Operations
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

### Key Properties
1. LIFO (Last In, First Out) structure
2. O(1) push and pop operations
3. Useful for tracking state and backtracking
4. Natural choice for nested structures
</details>

## Implementation Strategies
<details>
<summary>Click to expand</summary>

### 1. Basic Stack (List-based)
```python
def basic_stack_usage():
    stack = []
    
    # Push
    stack.append(item)
    
    # Pop
    if stack:
        item = stack.pop()
    
    # Peek
    if stack:
        top = stack[-1]
```

### 2. Monotonic Stack
```python
def monotonic_decreasing_stack(nums):
    stack = []  # (number, index)
    result = [0] * len(nums)
    
    for i, num in enumerate(nums):
        while stack and stack[-1][0] < num:
            prev_num, prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append((num, i))
```

### 3. Two Stacks
```python
class TwoStackStructure:
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []  # For min/max tracking
        
    def push(self, x):
        self.main_stack.append(x)
        if not self.aux_stack or x <= self.aux_stack[-1]:
            self.aux_stack.append(x)
            
    def pop(self):
        if self.main_stack:
            if self.main_stack[-1] == self.aux_stack[-1]:
                self.aux_stack.pop()
            return self.main_stack.pop()
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Parentheses Matching
```python
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
```

### 2. Expression Evaluation
```python
def evaluate_rpn(tokens):
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(int(token))
            
    return stack[0]
```

### 3. Monotonic Stack Pattern
```python
def next_greater_element(nums):
    stack = []  # Indices
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            prev_idx = stack.pop()
            result[prev_idx] = nums[i]
        stack.append(i)
        
    return result
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Stack with Extra Info
```python
class MinStack:
    def __init__(self):
        self.stack = []  # (value, current_min)
        
    def push(self, val):
        curr_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, curr_min))
        
    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
            
    def top(self):
        if self.stack:
            return self.stack[-1][0]
            
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
```

### 2. Stack with Lazy Updates
```python
class LazyStack:
    def __init__(self):
        self.stack = []
        self.lazy_value = 0
        
    def push(self, x):
        self.stack.append((x, self.lazy_value))
        
    def increment(self, k, val):
        self.lazy_value += val
        
    def pop(self):
        if self.stack:
            x, old_lazy = self.stack.pop()
            return x + (self.lazy_value - old_lazy)
```

### 3. Iterative DFS using Stack
```python
def iterative_dfs(graph, start):
    stack = [(start, [])]  # (node, path)
    visited = set()
    
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # Process node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path))
```
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Basic Operations
| Operation | Time | Space |
|-----------|------|-------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| isEmpty | O(1) | O(1) |

### Special Cases
- MinStack operations: All O(1)
- Expression evaluation: O(n) time, O(n) space
- Monotonic stack: O(n) time, O(n) space
</details>

## Common Pitfalls
<details>
<summary>Click to expand</summary>

### 1. Stack Underflow
```python
# WRONG
value = stack.pop()  # Stack might be empty

# RIGHT
if stack:
    value = stack.pop()
```

### 2. Missing Edge Cases
```python
# WRONG - Doesn't handle empty string
def evaluate(s):
    stack = []
    for char in s:  # Will fail for s = ""

# RIGHT
def evaluate(s):
    if not s:
        return 0
    stack = []
```

### 3. Stack Cleanup
```python
# WRONG - Leftover items not checked
while i < len(tokens):
    # Process tokens
    
# RIGHT
while i < len(tokens):
    # Process tokens
if stack:  # Check remaining items
    # Handle remaining
```
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [20. Valid Parentheses](../20/README.md)
- [155. Min Stack](../155/README.md)

### Medium
- [150. Evaluate Reverse Polish Notation](../150/README.md)
- [739. Daily Temperatures](../739/README.md)
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/)
2. [Monotonic Stack Patterns](https://leetcode.com/problems/daily-temperatures/discuss/109832/Java-Easy-AC-Solution-with-Stack)
3. [Expression Evaluation Guide](https://www.geeksforgeeks.org/expression-evaluation/)
</details>

---

*Remember: Stacks are perfect for problems involving matching, nesting, or maintaining order in reverse chronological order. When you see these patterns, consider using a stack!*
