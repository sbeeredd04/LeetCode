# Evaluate Reverse Polish Notation - Problem Analysis & Learning

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

## Key Insights & Learning Points

### 1. Reverse Polish Notation (RPN) Understanding
**What is RPN:**
- Postfix notation where operators come after operands
- No parentheses needed - order of operations is implicit
- Examples:
  - `"2 1 +"` → `2 + 1 = 3`
  - `"2 1 + 3 *"` → `(2 + 1) * 3 = 9`
  - `"4 13 5 / +"` → `4 + (13 / 5) = 6`

**Stack Perfect for RPN:**
- Process tokens left to right
- Push operands onto stack
- When operator found, pop required operands and apply operation
- Push result back onto stack

### 2. Algorithm Implementation

**Core Strategy:**
```python
stack = []
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y)  # Truncate towards zero
}

for token in tokens:
    if token in operators:
        right = int(stack.pop())  # Second operand
        left = int(stack.pop())   # First operand
        result = operators[token](left, right)
        stack.append(result)
    else:
        stack.append(int(token))

return stack[0]
```

### 3. Critical Mistakes & Learning Points

**❌ Major Mistake 1 - Operand Order Confusion:**
```python
# Wrong order - causes incorrect results
second = int(stack.pop())  # Gets 5
first = int(stack.pop())   # Gets 13
result = operators[char](second, first)  # 5 / 13 = 0 ❌

# Correct order
right = int(stack.pop())   # Second operand (5)
left = int(stack.pop())    # First operand (13)
result = operators[char](left, right)    # 13 / 5 = 2 ✅
```

**Why This Happens:**
- Stack is LIFO (Last In, First Out)
- For `["4", "13", "5", "/"]`: stack becomes `[4, 13, 5]`
- First `pop()` gets the **second** operand (5)
- Second `pop()` gets the **first** operand (13)
- Division should be `first / second` = `13 / 5` = `2`

**❌ Major Mistake 2 - Division Truncation:**
```python
# Wrong - floors towards negative infinity
'/': lambda x, y: x // y

# Correct - truncates towards zero (as RPN requires)
'/': lambda x, y: int(x / y)
```

**Examples of Difference:**
- `13 // 5 = 2` ✅ (positive numbers same result)
- `(-13) // 5 = -3` ❌ (floors to -3)
- `int((-13) / 5) = -2` ✅ (truncates to -2)

### 4. Data Type Handling

**❌ Common Mistake - String vs Integer:**
```python
# Wrong - storing strings instead of integers
if char not in operators: 
    stack.append(char)  # Storing string "5"
else:
    second = int(stack.pop())  # Converting back to int
```

**✅ Better Approach:**
```python
# Store as integers from the start
if token not in operators:
    stack.append(int(token))  # Store as integer
else:
    right = stack.pop()  # Already integer
    left = stack.pop()   # Already integer
```

### 5. Dictionary Mapping for Operators

**Benefits of Lambda Functions:**
```python
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y)
}
```

**Advantages:**
- Clean, readable code
- Easy to extend with new operators
- Functional programming approach
- Avoids long if/elif chains

**Alternative - operator Module:**
```python
import operator
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda x, y: int(operator.truediv(x, y))
}
```

### 6. Algorithm Walkthrough

**Example: `["4", "13", "5", "/", "+"]`**
```
Initial: stack = []

Step 1: "4" → stack = [4]
Step 2: "13" → stack = [4, 13]
Step 3: "5" → stack = [4, 13, 5]
Step 4: "/" → 
  - right = pop() = 5
  - left = pop() = 13
  - result = 13 / 5 = 2
  - stack = [4, 2]
Step 5: "+" →
  - right = pop() = 2
  - left = pop() = 4
  - result = 4 + 2 = 6
  - stack = [6]

Final result: 6
```

### 7. Edge Cases & Error Handling

**Valid RPN Properties:**
- Exactly one result remains in stack
- Sufficient operands for each operator
- Valid tokens only

**Error Handling:**
```python
# Check sufficient operands
if len(stack) < 2:
    raise ValueError("Invalid RPN expression")

# Check final result
if len(stack) != 1:
    raise ValueError("Invalid RPN expression")
```

### 8. Debugging Strategies

**Print Stack States:**
```python
print(f"Processing token: {token}, Current stack: {stack}")
if token in operators:
    print(f"Popped: left={left}, right={right}")
    print(f"Operation: {left} {token} {right} = {result}")
```

**Common Debug Points:**
- Stack state after each operation
- Operand order for non-commutative operations (`-`, `/`)
- Final stack size (should be 1)
- Type consistency (all integers)

### 9. Time & Space Complexity
- **Time:** O(n) - single pass through tokens
- **Space:** O(n) - stack size in worst case

### 10. Key Takeaways

1. **Stack Order Matters:** First pop = second operand, second pop = first operand
2. **Division Truncation:** Use `int(x / y)` not `x // y` for RPN
3. **Data Type Consistency:** Convert to int early, maintain throughout
4. **Dictionary Mapping:** Clean way to handle multiple operators
5. **Debug Methodology:** Print intermediate states to catch order errors
6. **RPN Properties:** Stack should have exactly one element at end

### 11. Common Patterns

**Stack-Based Expression Evaluation:**
- RPN (Postfix) - operators after operands
- Infix to Postfix conversion
- Calculator implementations
- Compiler expression parsing

### 12. Related Problems
- Basic Calculator
- Basic Calculator II
- Expression Add Operators
- Different Ways to Add Parentheses
- Infix to Postfix Conversion

## Problem-Specific Notes

**Test Cases to Consider:**
- Single number: `["42"]` → `42`
- Simple operation: `["2", "1", "+"]` → `3`
- Multiple operations: `["2", "1", "+", "3", "*"]` → `9`
- Division with truncation: `["4", "13", "5", "/", "+"]` → `6`
- Negative numbers: `["4", "-13", "5", "/", "+"]`

**Memory Aid:**
"First pop is second operand, second pop is first operand"
"For division: use int(x/y) not x//y"