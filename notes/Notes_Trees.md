# Trees Deep Dive 🌳

## Table of Contents
- [Core Concepts](#core-concepts)
- [Tree Traversal](#tree-traversal)
- [Binary Search Trees](#binary-search-trees)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Problem-Solving Framework](#problem-solving-framework)

## Core Concepts
<details>
<summary>Click to expand</summary>

### Tree Structure
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Basic Properties
1. Each node has 0 or more children
2. Each node (except root) has exactly one parent
3. Tree is connected and acyclic
4. Binary trees have at most 2 children per node

### Types of Trees
1. Binary Tree
2. Binary Search Tree (BST)
3. Complete Binary Tree
4. Perfect Binary Tree
5. Balanced Binary Tree
</details>

## Tree Traversal
<details>
<summary>Click to expand</summary>

### 1. DFS (Depth-First Search)
```python
# Recursive Implementation
def dfs_recursive(root):
    if not root:
        return
        
    # Preorder: process BEFORE recursion
    process_preorder(root)
    
    dfs_recursive(root.left)
    # Inorder: process BETWEEN recursions
    process_inorder(root)
    dfs_recursive(root.right)
    
    # Postorder: process AFTER recursion
    process_postorder(root)

# Iterative Implementation
def dfs_iterative(root):
    if not root:
        return
        
    stack = [root]
    while stack:
        node = stack.pop()
        # Process node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 2. BFS (Breadth-First Search)
```python
from collections import deque

def bfs(root):
    if not root:
        return
        
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # Process node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

### 3. Level Order Traversal
```python
def level_order(root):
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level)
    
    return result
```
</details>

## Binary Search Trees
<details>
<summary>Click to expand</summary>

### BST Properties
1. Left subtree values < node value
2. Right subtree values > node value
3. Both subtrees are BSTs
4. No duplicate values (typically)

### Basic Operations
```python
def search_bst(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    if target < root.val:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return is_valid_bst(root.left, min_val, root.val) and \
           is_valid_bst(root.right, root.val, max_val)
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Height/Depth Calculation
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))
```

### 2. Path Problems
```python
def diameter(root):
    max_diameter = [0]
    
    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        max_diameter[0] = max(max_diameter[0], left + right)
        return 1 + max(left, right)
    
    depth(root)
    return max_diameter[0]
```

### 3. Tree Modification
```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def merge_trees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Bottom-Up Recursion
```python
def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left = check_height(node.left)
        if left == -1:
            return -1
            
        right = check_height(node.right)
        if right == -1:
            return -1
            
        if abs(left - right) > 1:
            return -1
            
        return 1 + max(left, right)
    
    return check_height(root) != -1
```

### 2. Top-Down Recursion with State
```python
def good_nodes(root):
    def dfs(node, max_so_far):
        if not node:
            return 0
        
        count = 1 if node.val >= max_so_far else 0
        max_so_far = max(max_so_far, node.val)
        
        return count + dfs(node.left, max_so_far) + \
                      dfs(node.right, max_so_far)
    
    return dfs(root, float('-inf'))
```

### 3. BST Properties Utilization
```python
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    return root
```
</details>

## Problem-Solving Framework
<details>
<summary>Click to expand</summary>

### 1. Identify Tree Type
- Regular Binary Tree
- Binary Search Tree
- Complete/Perfect Tree
- Balanced/Unbalanced

### 2. Choose Traversal Method
- DFS: When exploring paths or subtrees
- BFS: When working with levels
- Pre/In/Post order: Based on when to process nodes

### 3. Select Pattern
- Recursion with global variable
- Pure recursion with return values
- Iterative with stack/queue
- Level-by-level processing
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [104. Maximum Depth of Binary Tree](../104/README.md)
- [226. Invert Binary Tree](../226/README.md)
- [235. Lowest Common Ancestor of a BST](../235/README.md)

### Medium
- [98. Validate Binary Search Tree](../98/README.md)
- [230. Kth Smallest Element in a BST](../230/README.md)
- [1448. Count Good Nodes in Binary Tree](../1448/README.md)

### Advanced
- [543. Diameter of Binary Tree](../543/README.md)
- [572. Subtree of Another Tree](../572/README.md)
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Common Operations
| Operation | Average | Worst |
|-----------|---------|-------|
| Search BST | O(log n) | O(n) |
| Insert BST | O(log n) | O(n) |
| DFS/BFS | O(n) | O(n) |
| Height | O(n) | O(n) |

### Space Complexity
- Recursive: O(h) where h is height
- BFS: O(w) where w is max width
- Iterative DFS: O(h)
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Tree Traversal Visualization](https://visualgo.net/en/bst)
2. [Binary Search Tree Guide](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
3. [Tree Interview Problems](https://leetcode.com/tag/tree/)
</details>

---

*Remember: Most tree problems can be solved with either DFS or BFS. The key is choosing the right traversal method and maintaining the right state during recursion.*
