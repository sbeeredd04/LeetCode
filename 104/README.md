# Maximum Depth of Binary Tree - Problem 104

## Problem Statement
Given the root of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7

Output: 3
```

## My Self-Reflection & Learning Journey

### 1. My Clean Solution

**What I Wrote:**
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if root is None
        if not root:
            return 0
        
        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return max depth between left and right subtree plus current node
        return 1 + max(left_depth, right_depth)
```

### 2. Why This Solution is Elegant

**✅ What I Got Perfectly Right:**

1. **Clean Recursive Structure:** Classic divide-and-conquer approach
2. **Clear Base Case:** Handle `None` nodes properly 
3. **Intuitive Logic:** Depth = 1 + max depth of subtrees
4. **Self-Documenting:** Code reads like the problem description

### 3. How My Algorithm Works

**Example Tree:**
```
    3
   / \
  9  20
    /  \
   15   7
```

**Execution Trace:**
```python
maxDepth(3):  # Root
├── maxDepth(9):  # Left subtree
│   ├── maxDepth(None) → 0  # 9's left child
│   ├── maxDepth(None) → 0  # 9's right child
│   └── return 1 + max(0, 0) = 1
├── maxDepth(20):  # Right subtree
│   ├── maxDepth(15):  # 20's left child
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── return 1 + max(0, 0) = 1
│   ├── maxDepth(7):   # 20's right child
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── return 1 + max(0, 0) = 1
│   └── return 1 + max(1, 1) = 2
└── return 1 + max(1, 2) = 3

Final result: 3
```

### 4. Foundation for Advanced Problems

**Why This Matters:**
This simple solution becomes the building block for more complex problems like:
- **Diameter of Binary Tree:** Uses height calculation as core component
- **Balanced Binary Tree:** Needs depth comparison between subtrees
- **Binary Tree Maximum Path Sum:** Extends the recursive pattern

**Template Pattern:**
```python
def tree_problem(self, root):
    # Base case
    if not root:
        return base_value
    
    # Recursive calls
    left_result = self.tree_problem(root.left)
    right_result = self.tree_problem(root.right)
    
    # Combine results
    return combine_function(left_result, right_result, root)
```

### 5. Performance Analysis

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(h) - recursion stack where h = height
- Best case (balanced): O(log n)
- Worst case (skewed): O(n)

### 6. Alternative Approaches

**Iterative with Queue (BFS):**
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
```

**Iterative with Stack (DFS):**
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth
```

**Why I Prefer Recursive:**
- More intuitive and readable
- Matches the problem's natural structure
- Easier to extend for related problems

### 7. Key Takeaways

**What This Problem Taught Me:**
1. **Recursive Thinking:** Break complex problems into simpler subproblems
2. **Base Case Design:** Always handle the simplest case first
3. **Pattern Recognition:** This template applies to many tree problems
4. **Foundation Building:** Simple solutions become building blocks for complex ones

**My Success Factors:**
- ✅ Clear recursive structure
- ✅ Proper base case handling  
- ✅ Intuitive combine logic
- ✅ Clean, readable implementation