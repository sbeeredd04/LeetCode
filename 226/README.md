# Invert Binary Tree - Problem 226

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root.

**Example:**
```
Input:      Output:
     4           4
   /   \       /   \
  2     7     7     2
 / \   / \   / \   / \
1   3 6   9 9   6 3   1
```

## My Self-Reflection & Learning Journey

### 1. My Quick Solution (What I Wrote)

**My Implementation:**
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recur(node): 
            if node.left and node.right : 
                node.left, node.right = node.right, node.left

            if node.left: 
                recur(node.left)
            if node.right: 
                recur(node.right)

            if not node.left or node.right : 
                pass

        #start the recursion from root node
        recur(root) if root else None
        return root 
```

### 2. My Initial Success & What Worked

**✅ What I Got Right:**
- **Core Logic:** I correctly identified that inverting means swapping left and right children
- **Recursive Structure:** I used recursion to traverse the entire tree
- **Python Swap:** I used the elegant `node.left, node.right = node.right, node.left` syntax
- **Edge Case Handling:** I handled the empty root case with `recur(root) if root else None`

**✅ Why This Was Easy for Me:**
Since this is a straightforward problem, I was able to get the solution quickly because:
1. The pattern is clear - swap children at every node
2. Recursion naturally fits tree traversal
3. The logic is intuitive - mirror the tree structure

### 3. Critical Issues I Need to Fix

**🚫 Major Bug in My Logic:**
```python
if node.left and node.right : 
    node.left, node.right = node.right, node.left
```

**Problem:** I only swap when BOTH children exist! This misses cases where:
- Node has only left child
- Node has only right child  
- One child becomes None after recursion

**🚫 Logic Error:**
```python
if not node.left or node.right : 
    pass
```
This condition is confusing and incorrect. `not node.left or node.right` means "if no left child OR has right child", which doesn't make logical sense here.

### 4. How My Algorithm Should Actually Work

**Corrected Version:**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert_subtree(node):
        if not node:  # Base case: empty node
            return
        
        # Always swap children (even if one or both are None)
        node.left, node.right = node.right, node.left
        
        # Recursively invert subtrees
        invert_subtree(node.left)
        invert_subtree(node.right)
    
    invert_subtree(root)
    return root
```

**Key Fixes:**
1. **Always swap:** Don't check if both children exist
2. **Base case:** Handle `None` nodes properly
3. **Clean logic:** Remove unnecessary conditions

### 5. Alternative Approach: Iterative with While Loop

**My Exploration: Using While Loop Instead of Recursion**

Since I wanted to explore using a while loop instead of the recursive function, here's how I can implement it:

**Iterative Approach with Stack:**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    nodes_to_process = [root]  # Use list as stack
    
    while nodes_to_process:
        current_node = nodes_to_process.pop()
        
        # Swap children
        current_node.left, current_node.right = current_node.right, current_node.left
        
        # Add children to stack for processing
        if current_node.left:
            nodes_to_process.append(current_node.left)
        if current_node.right:
            nodes_to_process.append(current_node.right)
    
    return root
```

**Iterative Approach with Queue (BFS):**
```python
from collections import deque

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        
        # Swap children
        current_node.left, current_node.right = current_node.right, current_node.left
        
        # Add children to queue for processing
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return root
```

### 6. Better Naming Conventions I Should Use

**My Current Names vs Better Alternatives:**

| My Names | Better Names | Why Better |
|----------|--------------|------------|
| `recur` | `invert_subtree` or `invert_node` | Describes what the function does |
| `node` | `current_node` or `curr` | More descriptive |
| `nodes_to_process` | `stack` or `queue` | Indicates data structure purpose |

**Improved Variable Naming:**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert_subtree(current_node):
        if not current_node:
            return
        
        # Swap left and right children
        current_node.left, current_node.right = current_node.right, current_node.left
        
        # Recursively invert left and right subtrees
        invert_subtree(current_node.left)
        invert_subtree(current_node.right)
    
    invert_subtree(root)
    return root
```

### 7. Comparing All Three Approaches

**Approach 1: Recursive (Corrected)**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root
```

**Approach 2: Iterative with Stack (DFS)**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        current = stack.pop()
        current.left, current.right = current.right, current.left
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return root
```

**Approach 3: Iterative with Queue (BFS)**
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return root
```

### 8. Performance Analysis

**All Three Approaches:**
- **Time Complexity:** O(n) - visit each node exactly once
- **Space Complexity:** 
  - Recursive: O(h) where h is tree height (call stack)
  - Iterative: O(w) where w is maximum width of tree (stack/queue size)

**When to Use Each:**
- **Recursive:** Most intuitive and clean for tree problems
- **Stack (DFS):** When you want iterative but don't care about level order
- **Queue (BFS):** When you want to process level by level

### 9. What I Learned About My Coding Style

**Areas for Improvement:**

1. **Logic Verification:** I need to test edge cases mentally before coding
   - What if node has only left child?
   - What if node has only right child?
   - What if node is None?

2. **Naming Conventions:** My function and variable names should be more descriptive
   - `recur` → `invert_subtree`
   - `node` → `current_node`
   - Use verbs for functions, nouns for variables

3. **Code Clarity:** Avoid unnecessary conditions
   - Remove the confusing `if not node.left or node.right: pass`
   - Keep logic simple and readable

4. **Testing Mindset:** I should trace through examples step by step

### 10. My Debugging Process

**How I Would Test My Original Solution:**

Test Case: Tree with only right children
```
    1
     \
      2
       \
        3
```

**Tracing My Original Code:**
```python
# At node 1: node.left=None, node.right=2
if node.left and node.right:  # False! (None and 2 = False)
    # Swap doesn't happen - BUG!

# At node 2: node.left=None, node.right=3  
if node.left and node.right:  # False! (None and 3 = False)
    # Swap doesn't happen - BUG!
```

**Result:** Tree remains unchanged - completely wrong!

**How Fixed Version Works:**
```python
# At each node: Always swap regardless of children
node.left, node.right = node.right, node.left
# Result: Correctly inverted tree
```

### 11. Best Practices I Should Follow

**Function Design:**
```python
def function_name(self, parameters):
    """
    Clear docstring explaining what the function does
    """
    # Handle edge cases first
    if not root:
        return None
    
    # Main logic with clear comments
    # Use descriptive variable names
    # Keep functions focused on single responsibility
```

**Variable Naming:**
- Use `current_node` instead of `node`
- Use `left_child`, `right_child` for clarity
- Use `stack`, `queue` instead of generic `container`

**Code Organization:**
- Handle base cases first
- Group related operations
- Use meaningful comments for complex logic

### 12. Complete Corrected Solutions

**My Preferred Recursive Solution:**
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping left and right children recursively.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            Root node of the inverted tree
        """
        if not root:
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

**My Iterative Alternative (Stack-based):**
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree iteratively using a stack for DFS traversal.
        """
        if not root:
            return None
        
        nodes_to_process = [root]
        
        while nodes_to_process:
            current_node = nodes_to_process.pop()
            
            # Swap children
            current_node.left, current_node.right = current_node.right, current_node.left
            
            # Add children to stack if they exist
            if current_node.left:
                nodes_to_process.append(current_node.left)
            if current_node.right:
                nodes_to_process.append(current_node.right)
        
        return root
```

### 13. Key Takeaways & Reflection

**What This Problem Taught Me:**

1. **Edge Case Testing:** Even "easy" problems can have subtle bugs if I don't test thoroughly

2. **Code Review Importance:** My initial solution had a critical logical flaw that would fail many test cases

3. **Multiple Valid Approaches:** Recursive vs iterative - both have merit depending on constraints

4. **Naming Matters:** Good variable names make code self-documenting

5. **Simplicity Wins:** The simplest correct solution is often the best

**My Development Areas:**
- Test edge cases mentally before submitting
- Use more descriptive names consistently  
- Verify logic with simple examples
- Consider iterative alternatives for stack-sensitive environments

**Why This Was Still a Learning Experience:**
Even though I got the "easy" solution quickly, debugging my logical errors and exploring iterative approaches deepened my understanding of:
- Tree traversal patterns
- Recursive vs iterative trade-offs
- The importance of thorough testing
- Clean coding practices

**My Final Reflection:**
Getting a solution quickly doesn't mean getting it right! This problem reminded me that even simple algorithms require careful thought about edge cases and clear logic. The exploration of iterative approaches also showed me that there are always multiple ways to solve the same problem, each with its own benefits.