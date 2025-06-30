# Diameter of Binary Tree - Problem 543

## Problem Statement
Given the root of a binary tree, return the length of the diameter of the tree.

The **diameter** of a binary tree is the **length of the longest path** between any two nodes in a tree. This path may or may not pass through the root.

The **length of a path** between two nodes is represented by the number of edges between them.

**Example:**
```
Input: root = [1,2,3,4,5]
        1
       / \
      2   3
     / \
    4   5

Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

## My Self-Reflection & Learning Journey

### 1. Understanding the Connection to Max Depth

**First, My Max Depth Solution (Problem 104):**
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)
```

**Key Insight:** The diameter problem builds directly on the max depth concept! The diameter passing through any node equals the sum of the heights of its left and right subtrees.

### 2. My Diameter Solution Analysis

**What I Wrote:**
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def maxDiameter(node): 
            nonlocal d
            if not node : 
                return 0
            left_height = maxDiameter(node.left)
            right_height = maxDiameter(node.right)
            d = max(left_height+right_height, d)
            return 1+max(left_height, right_height)
        
        maxDiameter(root)
        return d
```

### 3. Why My Solution is Brilliant

**✅ What I Got Perfectly Right:**

1. **Dual Purpose Function:** My `maxDiameter` function does two things simultaneously:
   - Calculates height of subtree (returns `1 + max(left_height, right_height)`)
   - Updates global maximum diameter (updates `d` with `left_height + right_height`)

2. **Efficient Single Pass:** I solve the problem in O(n) time by visiting each node exactly once

3. **Correct Diameter Calculation:** At each node, the diameter passing through that node is `left_height + right_height`

4. **Global State Tracking:** I use `nonlocal d` to maintain the maximum diameter found so far

### 4. Deep Dive: The `nonlocal` Keyword

**Why I Needed `nonlocal`:**

```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    d = 0  # This variable is in the outer function scope
    
    def maxDiameter(node):
        nonlocal d  # This tells Python I want to modify 'd' from outer scope
        # Without nonlocal, I would create a new local variable 'd'
        d = max(left_height + right_height, d)  # Modifying outer 'd'
```

**What `nonlocal` Does:**
- **Without `nonlocal`:** Python would create a new local variable `d` inside `maxDiameter`
- **With `nonlocal`:** Python modifies the `d` from the enclosing function scope
- **Alternative without `nonlocal`:** I would need to return the diameter and track it differently

**Example of the Problem Without `nonlocal`:**
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    d = 0
    
    def maxDiameter(node):
        # No nonlocal declaration
        if not node:
            return 0
        left_height = maxDiameter(node.left)
        right_height = maxDiameter(node.right)
        d = max(left_height + right_height, d)  # Creates LOCAL 'd'!
        return 1 + max(left_height, right_height)
    
    maxDiameter(root)
    return d  # Returns the original 'd' = 0, not the updated value!
```

### 5. How My Algorithm Works Step by Step

**Example Tree:**
```
    1
   / \
  2   3
 / \
4   5
```

**Execution Trace:**
```python
maxDiameter(1):  # Root node
├── maxDiameter(2):  # Left subtree
│   ├── maxDiameter(4):  # Left leaf
│   │   ├── maxDiameter(None) → returns 0
│   │   ├── maxDiameter(None) → returns 0
│   │   ├── d = max(0+0, 0) = 0
│   │   └── returns 1+max(0,0) = 1
│   ├── maxDiameter(5):  # Right leaf
│   │   ├── maxDiameter(None) → returns 0
│   │   ├── maxDiameter(None) → returns 0
│   │   ├── d = max(0+0, 0) = 0
│   │   └── returns 1+max(0,0) = 1
│   ├── left_height = 1, right_height = 1
│   ├── d = max(1+1, 0) = 2  # Diameter through node 2
│   └── returns 1+max(1,1) = 2
├── maxDiameter(3):  # Right subtree
│   ├── maxDiameter(None) → returns 0
│   ├── maxDiameter(None) → returns 0
│   ├── d = max(0+0, 2) = 2
│   └── returns 1+max(0,0) = 1
├── left_height = 2, right_height = 1
├── d = max(2+1, 2) = 3  # Diameter through root: 4→2→1→3
└── returns 1+max(2,1) = 3

Final result: d = 3
```

### 6. Alternative Approaches I Could Have Used

**Approach 1: Return Both Height and Diameter**
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def helper(node):
        if not node:
            return 0, 0  # (height, diameter)
        
        left_height, left_diameter = helper(node.left)
        right_height, right_diameter = helper(node.right)
        
        current_height = 1 + max(left_height, right_height)
        current_diameter = max(
            left_height + right_height,  # Diameter through current node
            left_diameter,               # Max diameter in left subtree
            right_diameter               # Max diameter in right subtree
        )
        
        return current_height, current_diameter
    
    _, diameter = helper(root)
    return diameter
```

**Approach 2: Class Variable**
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update global maximum
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.max_diameter
```

**Why I Chose My Approach:**
- **Cleaner than tuple returns:** No need to unpack values
- **More contained than class variables:** `nonlocal` keeps state local to the function
- **Clear separation:** The helper function has a clear single responsibility

### 7. Performance Analysis

**Time Complexity:** O(n)
- Visit each node exactly once
- Constant work at each node

**Space Complexity:** O(h) where h is height of tree
- Recursion stack depth equals tree height
- Best case (balanced): O(log n)
- Worst case (skewed): O(n)

**Efficiency Comparison:**
- My approach: Single pass, optimal
- Naive approach (calculate height for each node): O(n²)

### 8. Edge Cases My Solution Handles

**Edge Case 1: Empty Tree**
```python
root = None
# maxDiameter(None) returns 0
# Final result: d = 0 ✓
```

**Edge Case 2: Single Node**
```python
root = TreeNode(1)
# left_height = 0, right_height = 0
# d = max(0+0, 0) = 0 ✓
```

**Edge Case 3: Linear Tree (Skewed)**
```python
#   1
#    \
#     2
#      \
#       3
# Diameter = 2 (path: 1→2→3) ✓
```

**Edge Case 4: Diameter Not Through Root**
```python
#     1
#    /
#   2
#  / \
# 3   4
#    / \
#   5   6
# Diameter = 3 (path: 3→2→4→5 or 3→2→4→6) ✓
```

### 9. What I Learned About Variable Scoping

**Key Insights About `nonlocal`:**

1. **When to Use `nonlocal`:**
   - When I need to modify a variable from an enclosing (but not global) scope
   - Alternative to returning multiple values or using class variables

2. **Python Scoping Rules (LEGB):**
   - **L**ocal: Inside the current function
   - **E**nclosing: In enclosing functions
   - **G**lobal: At module level
   - **B**uilt-in: Built-in names

3. **Without `nonlocal` - Creates Local Variable:**
   ```python
   def outer():
       x = 10
       def inner():
           x = 20  # Creates new local 'x', doesn't modify outer 'x'
       inner()
       print(x)  # Still 10
   ```

4. **With `nonlocal` - Modifies Enclosing Variable:**
   ```python
   def outer():
       x = 10
       def inner():
           nonlocal x
           x = 20  # Modifies outer 'x'
       inner()
       print(x)  # Now 20
   ```

### 10. Common Mistakes I Avoided

**❌ Mistake 1: Confusing Diameter with Height**
```python
# WRONG - This returns height, not diameter
def diameterOfBinaryTree(self, root):
    if not root:
        return 0
    return 1 + max(self.diameterOfBinaryTree(root.left), 
                   self.diameterOfBinaryTree(root.right))
```

**❌ Mistake 2: Not Considering All Possible Diameters**
```python
# WRONG - Only considers diameter through root
def diameterOfBinaryTree(self, root):
    if not root:
        return 0
    left_height = self.maxDepth(root.left)
    right_height = self.maxDepth(root.right)
    return left_height + right_height
```

**❌ Mistake 3: Forgetting `nonlocal`**
```python
# WRONG - 'd' remains 0
def diameterOfBinaryTree(self, root):
    d = 0
    def helper(node):
        # Missing: nonlocal d
        d = max(left_height + right_height, d)  # Creates local 'd'
    helper(root)
    return d  # Returns original 'd' = 0
```

### 11. Relationship to Other Tree Problems

**Similar Pattern - Path Sum Problems:**
- Use similar technique of maintaining global state while traversing
- Combine recursive traversal with state tracking

**Building on Max Depth:**
- Diameter extends the max depth concept
- Shows how to reuse helper functions for different metrics

**Template for Tree Problems with Global State:**
```python
def tree_problem(self, root):
    result = initial_value
    
    def helper(node):
        nonlocal result
        if not node:
            return base_case
        
        left_value = helper(node.left)
        right_value = helper(node.right)
        
        # Update global result based on current node
        result = update_function(result, left_value, right_value, node)
        
        # Return value for parent's calculation
        return value_for_parent(left_value, right_value, node)
    
    helper(root)
    return result
```

### 12. My Solution Strengths & Areas for Improvement

**✅ Strengths:**
1. **Optimal Efficiency:** Single pass solution with O(n) time
2. **Correct Logic:** Properly handles all edge cases
3. **Clean Structure:** Clear separation between height calculation and diameter tracking
4. **Proper Use of `nonlocal`:** Demonstrates understanding of Python scoping

**🔧 Areas for Improvement:**

1. **Variable Naming:** Could be more descriptive
   ```python
   # Current
   d = 0
   def maxDiameter(node):
   
   # Better
   max_diameter = 0
   def calculate_height_and_update_diameter(node):
   ```

2. **Comments:** Could add more explanatory comments
   ```python
   def calculate_height_and_update_diameter(node):
       nonlocal max_diameter
       if not node:
           return 0
       
       # Get heights of left and right subtrees
       left_height = calculate_height_and_update_diameter(node.left)
       right_height = calculate_height_and_update_diameter(node.right)
       
       # Update max diameter if path through current node is longer
       max_diameter = max(left_height + right_height, max_diameter)
       
       # Return height of current subtree for parent's calculation
       return 1 + max(left_height, right_height)
   ```

### 13. Testing Strategy

**Test Cases I Should Verify:**
```python
# Test 1: Example from problem
#     1
#    / \
#   2   3
#  / \
# 4   5
# Expected: 3 (path: 4→2→1→3 or 5→2→1→3)

# Test 2: Diameter not through root
#       1
#      /
#     2
#    / \
#   3   4
#      / \
#     5   6
# Expected: 3 (path: 3→2→4→5 or 3→2→4→6)

# Test 3: Single node
#   1
# Expected: 0

# Test 4: Linear tree
#   1
#    \
#     2
#      \
#       3
# Expected: 2 (path: 1→2→3)
```

### 14. Key Takeaways & Learning

**What This Problem Taught Me:**

1. **Building on Previous Knowledge:** Diameter problem elegantly extends max depth solution

2. **`nonlocal` Mastery:** Learned when and how to use `nonlocal` for enclosing scope modification

3. **Dual-Purpose Functions:** A single recursive function can compute multiple metrics simultaneously

4. **Global State in Recursion:** How to maintain and update global state during tree traversal

5. **Optimization Thinking:** Single-pass solution is much better than naive O(n²) approach

**Problem-Solving Pattern I Discovered:**
> "When you need to track both local properties (height) and global properties (max diameter), use a helper function that returns the local property while updating the global property via `nonlocal`"

### 15. Related Problems to Practice

**Similar Pattern Problems:**
- Binary Tree Maximum Path Sum (LC 124)
- Longest Univalue Path (LC 687) 
- Binary Tree Tilt (LC 563)
- Sum Root to Leaf Numbers (LC 129)

**All use the pattern:** Local calculation + Global state tracking

## My Final Optimized Solution

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate diameter of binary tree in single pass.
        
        Diameter = length of longest path between any two nodes
        """
        max_diameter = 0
        
        def calculate_height_and_update_diameter(node):
            """
            Returns height of subtree while updating global max diameter.
            """
            nonlocal max_diameter
            
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left_height = calculate_height_and_update_diameter(node.left)
            right_height = calculate_height_and_update_diameter(node.right)
            
            # Update max diameter if path through current node is longer
            current_diameter = left_height + right_height
            max_diameter = max(max_diameter, current_diameter)
            
            # Return height of current subtree for parent calculations
            return 1 + max(left_height, right_height)
        
        calculate_height_and_update_diameter(root)
        return max_diameter
```

**My Memory Aid:**
> "Diameter = sum of heights through each node. Track max diameter globally while calculating heights recursively. Use `nonlocal` to update outer scope variable."

**What Made My Solution Successful:**
1. ✅ Recognized connection to max depth problem
2. ✅ Used `nonlocal` correctly for state management
3. ✅ Single-pass optimization with dual-purpose function
4. ✅ Handled all edge cases properly
5. ✅ Clean, efficient implementation