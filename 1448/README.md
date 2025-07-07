# Count Good Nodes in Binary Tree (LeetCode 1448) - My Learning Journey

## Problem Understanding

I needed to count the number of "good" nodes in a binary tree. A node X in the tree is named **good** if in the path from root to X there are no nodes with a value greater than X.

**Example:**
```
Input:     3
          / \
         1   4
        /   / \
       3   1   5

Output: 4
Explanation: Good nodes are 3, 1, 4, 5 (highlighted in the path)
- Root 3 is always good
- Node 1: path is [3,1], max = 3, 1 <= 3 ✓
- Node 3: path is [3,1,3], max = 3, 3 >= 3 ✓  
- Node 4: path is [3,4], max = 3, 4 >= 3 ✓
- Node 1: path is [3,4,1], max = 4, 1 < 4 ✗
- Node 5: path is [3,4,5], max = 4, 5 >= 4 ✓
```

## My Algorithm - Simple Path Maximum Tracking

### The Key Insight 💡

This problem clicked for me immediately:

> **"I just need to keep track of the maximum value encountered on the path from root to current node. If current node >= path_max, it's a good node!"**

This was a **straightforward DFS with state tracking** - very similar to other tree problems I've solved.

### My Solution

```python
def goodNodes(self, root: TreeNode) -> int:
    maxVal = float('-inf')

    def trackNodes(node, maxVal): 
        if not node : 
            return 0

        count = 1 if node.val >= maxVal else 0

        count += trackNodes(node.left, max(maxVal, node.val))
        count += trackNodes(node.right, max(maxVal, node.val))
        
        return count

    count = trackNodes(root, maxVal)
    return count
```

### Why This Works - The Algorithm Logic

**Core Strategy:**
1. **DFS traversal** with path maximum tracking
2. **At each node:** check if `node.val >= path_max`
3. **Return counting approach:** add 1 if good, 0 if bad
4. **Recursive accumulation:** sum up all good nodes from subtrees

**The Brilliant Simplicity:**
- **Path maximum tracking:** `max(maxVal, node.val)` updates the maximum for child calls
- **Clean counting:** return 1 or 0, then sum recursively
- **No global state:** everything passed through parameters

## Step-by-Step Algorithm Walkthrough

Let me trace through the example tree:
```
    3
   / \
  1   4
 /   / \
3   1   5
```

### DFS Traversal with Path Maximum:

1. **Visit 3 (maxVal = -∞)**: 3 >= -∞ ✓ → count = 1
   - Update maxVal = max(-∞, 3) = 3

2. **Visit 1 (maxVal = 3)**: 1 >= 3 ✗ → count = 0
   - Update maxVal = max(3, 1) = 3

3. **Visit 3 (maxVal = 3)**: 3 >= 3 ✓ → count = 1
   - Leaf node, return 1

4. **Back to node 1**: total from left = 1, return 1

5. **Visit 4 (maxVal = 3)**: 4 >= 3 ✓ → count = 1
   - Update maxVal = max(3, 4) = 4

6. **Visit 1 (maxVal = 4)**: 1 >= 4 ✗ → count = 0
   - Leaf node, return 0

7. **Visit 5 (maxVal = 4)**: 5 >= 4 ✓ → count = 1
   - Leaf node, return 1

8. **Back to node 4**: total = 1 + 0 + 1 = 2

9. **Back to root**: total = 1 + 1 + 2 = 4

**Final Answer: 4 good nodes**

## Algorithm Analysis

### Time Complexity: O(n)
- Visit each node exactly once
- Constant work per node (comparison and max calculation)
- Linear in the number of nodes

### Space Complexity: O(h)
- **O(h)** for recursion stack depth (h = height of tree)
- **No additional data structures needed**
- **Best case:** O(log n) for balanced tree
- **Worst case:** O(n) for skewed tree

## Key Design Decisions & Why They Work

### 1. **Starting with float('-inf')**
```python
maxVal = float('-inf')
```
- Ensures root node is always counted as good
- Handles negative values correctly
- Clean initial condition

### 2. **Recursive Return Pattern**
```python
count = 1 if node.val >= maxVal else 0
count += trackNodes(node.left, max(maxVal, node.val))
count += trackNodes(node.right, max(maxVal, node.val))
return count
```
- **Clean accumulation:** no need for global variables
- **Functional approach:** each call returns its contribution
- **Easy to reason about:** sum of current + left subtree + right subtree

### 3. **Path Maximum Update**
```python
max(maxVal, node.val)
```
- **Immutable approach:** doesn't modify the original maxVal
- **Correct propagation:** each path maintains its own maximum
- **Simple logic:** current max is either previous max or current value

## Alternative Approaches I Considered

### Approach 1: Global Counter (Less Elegant)
```python
def goodNodes(self, root: TreeNode) -> int:
    self.count = 0
    
    def dfs(node, maxVal):
        if not node:
            return
        
        if node.val >= maxVal:
            self.count += 1
            
        dfs(node.left, max(maxVal, node.val))
        dfs(node.right, max(maxVal, node.val))
    
    dfs(root, float('-inf'))
    return self.count
```

**Why I Avoided This:**
- **Global state management** feels messier
- **Side effects** make testing harder
- **Less functional** programming style

### Approach 2: Path List Tracking (Overkill)
```python
def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, path):
        if not node:
            return 0
        
        path.append(node.val)
        count = 1 if node.val >= max(path) else 0
        
        count += dfs(node.left, path[:])  # Copy path
        count += dfs(node.right, path[:])
        
        return count
    
    return dfs(root, [])
```

**Why This Is Inefficient:**
- **O(n) space per path** vs O(1) for max tracking
- **Redundant max calculation** at each level
- **Path copying overhead**

## Edge Cases Analysis

### 1. Single Node Tree
```python
Input: root = [1]
Path: [1], maxVal = -∞
Output: 1 (root is always good)
```

### 2. All Increasing Path
```python
Input:   1
          \
           2
            \
             3
Path: [1] → [1,2] → [1,2,3]
Each node >= previous max ✓
Output: 3
```

### 3. All Decreasing Path
```python
Input:   3
        /
       2
      /
     1
Path: [3] → [3,2] → [3,2,1]
Only root is good (3 >= -∞)
2 < 3 ✗, 1 < 3 ✗
Output: 1
```

### 4. Negative Values
```python
Input:  -1
       /  \
     -2   -3
All nodes >= -∞ ✓
Output: 3
```

## Self-Reflection on My Problem-Solving Process

### 1. **Immediate Pattern Recognition**
This problem felt very familiar - it's essentially **DFS with path state tracking**. I've seen this pattern in:
- Path sum problems
- Maximum depth problems  
- Validate BST problems

### 2. **Clean Recursive Design**
I'm getting much better at designing **clean recursive functions**:
- **Clear base case:** `if not node: return 0`
- **Single responsibility:** each call counts its subtree
- **Immutable parameters:** no side effects
- **Natural accumulation:** sum of recursive calls

### 3. **Avoiding Overcomplication**
My first instinct was to track the entire path, but I quickly realized I only need the **maximum value**, not the entire path. This shows I'm developing **optimization intuition**.

### 4. **Functional Programming Influence**
My solution uses a **functional approach**:
- No global state
- Pure functions (given same input, same output)
- Return values instead of side effects
- Immutable parameter passing

## What I Learned

### 1. **Path State Tracking Pattern**
The pattern of passing **path-specific state** through recursive parameters is very powerful:
```python
def dfs(node, path_state):
    # Use path_state for current decision
    # Update path_state for children
    dfs(child, updated_path_state)
```

### 2. **Return vs Side Effect Design**
**Returning counts** is cleaner than **global counters**:
- Easier to test individual subtrees
- No hidden state dependencies  
- More composable and predictable

### 3. **State Minimization**
Only track what you need! I could have tracked the entire path, but only the **maximum** was necessary. This reduces:
- Space complexity
- Computational overhead
- Code complexity

### 4. **Edge Case Thinking**
Starting with `float('-inf')` handles all edge cases elegantly:
- Negative values work correctly
- Root is always considered good
- No special case handling needed

## Key Insights and Patterns

### DFS with Path State Pattern:
```python
def dfs_with_path_state(node, path_state):
    if not node:
        return base_case_value
    
    # Make decision based on current node + path_state
    current_result = make_decision(node, path_state)
    
    # Update path_state for children
    updated_state = update_path_state(path_state, node)
    
    # Recursively process children
    left_result = dfs_with_path_state(node.left, updated_state)
    right_result = dfs_with_path_state(node.right, updated_state)
    
    # Combine results
    return combine_results(current_result, left_result, right_result)
```

### State Update Strategy:
```python
# Good: Immutable update
new_max = max(current_max, node.val)
dfs(child, new_max)

# Avoid: Mutable state
current_max = max(current_max, node.val)  # Side effect
dfs(child, current_max)
```

## Mistakes I Avoided

### 1. **Global Variable Trap**
Could have used `self.count += 1`, but recursive return is cleaner.

### 2. **Path Array Overhead**
Could have tracked full path `[3,1,3]`, but only needed max value.

### 3. **Complicated Base Case**
Could have special-cased root, but `float('-inf')` handles it naturally.

### 4. **Mutable State Issues**
Could have modified `maxVal` in place, but immutable passing is safer.

## Final Thoughts

This problem reinforced my growing confidence with **recursive tree algorithms**. The key insight was recognizing this as a **path state tracking** problem rather than overcomplicating it.

My solution is:
- ✅ **Efficient:** O(n) time, O(h) space
- ✅ **Clean:** No global state, pure recursion
- ✅ **Readable:** Clear logic flow
- ✅ **Robust:** Handles all edge cases

The **recursive counting pattern** I used here will definitely be useful for similar tree problems in the future!
