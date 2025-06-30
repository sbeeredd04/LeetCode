# Min Stack - Problem Analysis & Learning

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `MinStack()` initializes the stack object
- `void push(int val)` pushes the element val onto the stack
- `void pop()` removes the element on the top of the stack
- `int top()` gets the top element of the stack
- `int getMin()` retrieves the minimum element in the stack

## Key Insights & Learning Points

### 1. Core Challenge - O(1) Minimum Retrieval
**The Problem:**
- Need to track minimum element as stack changes
- `getMin()` must be O(1) - can't search through stack each time
- When minimum element is popped, need to know next minimum

**Current Implementation Analysis:**
```python
def pop(self) -> None:
    self.stack.pop()
    if not self.stack:
        self.minimum = float('inf')
    else:
        self.minimum = min(self.stack)  # ❌ O(n) operation!
```

### 2. Implementation Approaches

**❌ Current Approach - Inefficient:**
- Recalculate minimum after each pop: `min(self.stack)`
- Time Complexity: O(n) for pop operation
- Space Complexity: O(1) extra space

**✅ Better Approach 1 - Auxiliary Min Stack:**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimums at each level
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push current minimum to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
    
    def getMin(self) -> int:
        return self.min_stack[-1]  # O(1)!
```

**✅ Better Approach 2 - Hash Map with Counts:**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.counts = {}  # Track frequency of each element
        self.min_val = float('inf')
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.counts[val] = self.counts.get(val, 0) + 1
        self.min_val = min(self.min_val, val)
    
    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            self.counts[popped] -= 1
            if self.counts[popped] == 0:
                del self.counts[popped]
                if popped == self.min_val:
                    self.min_val = min(self.counts.keys()) if self.counts else float('inf')
```

### 3. Time & Space Complexity Analysis

**Current Implementation:**
- `push()`: O(1)
- `pop()`: O(n) ❌
- `top()`: O(1)
- `getMin()`: O(1)
- Space: O(1) extra

**Optimized Approaches:**
- All operations: O(1) ✅
- Space: O(n) extra for auxiliary structures

### 4. Python Class Implementation Details

**Class Structure:**
```python
class MinStack:
    def __init__(self):
        """Constructor - initialize instance variables"""
        self.stack = []
        self.minimum = float('inf')
    
    def method_name(self, param: type) -> return_type:
        """Method with type hints"""
        pass
```

**Key Python Concepts:**
- `self` parameter in all instance methods
- `__init__()` constructor method
- Type hints: `val: int` and `-> None`
- Instance variables: `self.stack`, `self.minimum`
- `float('inf')` for representing infinity

### 5. Edge Cases & Error Handling

**Critical Edge Cases:**
1. **Empty stack operations:**
   - `pop()` on empty stack
   - `top()` on empty stack
   - `getMin()` on empty stack

2. **Single element scenarios:**
   - Push one element, then pop
   - Minimum tracking with one element

3. **Duplicate minimums:**
   - Multiple occurrences of minimum value
   - Popping one minimum shouldn't affect others

**Defensive Programming:**
```python
def pop(self) -> None:
    if not self.stack:  # Check before popping
        return  # or raise exception
    # ... rest of implementation

def top(self) -> int:
    if not self.stack:
        raise IndexError("Stack is empty")
    return self.stack[-1]
```

### 6. Alternative Data Structures Considered

**Hash Map + Sorted Keys:**
- Use `collections.Counter` for frequency tracking
- Maintain sorted list of unique elements
- Find next minimum by scanning sorted keys

**Binary Search Tree:**
- Maintain BST of unique elements with counts
- Find minimum in O(log n) worst case
- More complex implementation

**Priority Queue (Heap):**
- Min heap for tracking minimums
- Problem: Can't efficiently remove arbitrary elements
- Not suitable for this specific problem

### 7. Algorithm Walkthrough

**Example: push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()**

```
Initial: stack=[], min=inf

push(-2): stack=[-2], min=-2
push(0):  stack=[-2,0], min=-2
push(-3): stack=[-2,0,-3], min=-3
getMin(): return -3
pop():    stack=[-2,0], need to recalculate min=min([-2,0])=-2
top():    return 0
getMin(): return -2
```

### 8. Key Takeaways

1. **Trade-off Awareness:** Space vs Time complexity considerations
2. **Algorithm Optimization:** Current O(n) pop can be improved to O(1)
3. **Edge Case Handling:** Empty stack scenarios need careful consideration
4. **Python Class Design:** Proper use of `__init__`, `self`, and type hints
5. **Data Structure Choice:** Auxiliary stack often simplest for stack problems

### 9. Common Patterns

**Stack + Auxiliary Structure:**
- Common pattern for maintaining additional properties
- Examples: Min/Max stack, Stack with queues
- Trade extra space for better time complexity

**State Tracking:**
- When current state depends on historical data
- Use auxiliary structures to avoid recalculation
- Maintain invariants as operations proceed

### 10. Related Problems
- Max Stack
- Stack of Plates
- Implement Queue using Stacks
- Baseball Game
- Valid Parentheses

## Problem-Specific Notes

**Test Cases to Consider:**
- Empty stack operations
- Single element push/pop
- Multiple minimums
- Minimum at different positions
- Large stack operations

**Debug Strategy:**
- Print stack and minimum state after each operation
- Verify minimum is always correct
- Test edge cases thoroughly

**Memory Aid:**
"Track minimums as you go - don't recalculate, remember!"