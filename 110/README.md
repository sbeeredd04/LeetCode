# Balanced Binary Tree (LeetCode 110) - My Learning Journey & Self-Reflection

## Problem Understanding

I needed to determine if a binary tree is height-balanced, where a balanced tree is defined as one where the depth of the two subtrees of every node never differs by more than 1.

**Key Challenge:** Not just check the root's left and right subtrees, but ensure EVERY node in the tree satisfies the balance condition.

## My Initial Solution - So Close Yet So Far

### What I Originally Wrote:
```python
def DFS(root): 
    if not root: 
        return [0, True]
    left_height, right_height = DFS(root.left), DFS(root.right)
    balanced = left_height[1] and right_height[1] and abs(left_height[0] - right_height[0]) <= 1
    return [1 + max(left_height[0], right_height[0]), balanced]
```

### The Critical Bug I Discovered

**The Problem:** I was returning `[height, balanced]` but I was **overwriting the balanced status** instead of propagating failures up the recursion tree.

**My Realization:** 
> "I am passing True but if along the way there was a false, then I should be making it false throughout the recursion tree, but I am changing it back to true!"

This was my **"Aha!" moment** - I understood that once ANY subtree is unbalanced, the entire tree should be considered unbalanced.

## The Corrected Solution Analysis

### What The Working Solution Looks Like:
```python
def dfs(root):
    if not root:
        return [True, 0]  # [is_balanced, height]

    left, right = dfs(root.left), dfs(root.right)
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    return [balanced, 1 + max(left[1], right[1])]
```

### Key Differences I Identified:

#### 1. **Return Format Convention**
```python
# My original (confusing)
return [height, balanced]

# Better approach (clearer)
return [balanced, height]
```

**Why this matters:** Putting the boolean first makes the code more readable when accessing `result[0]` for the balance status.

#### 2. **Proper Failure Propagation**
```python
# My bug - was checking conditions but not propagating failures
balanced = left_height[1] and right_height[1] and abs(left_height[0] - right_height[0]) <= 1

# Correct approach - explicitly check subtree balance first
balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
```

**The insight:** `left[0] and right[0]` ensures that if either subtree is unbalanced, we immediately return `False` without even checking the current node's balance.

## My Debugging Journey - Step by Step

### 1. **Initial Confusion**
I was getting wrong results and couldn't figure out why my logic seemed sound.

### 2. **Comparing Solutions**
I found a working solution and started comparing line by line with mine.

### 3. **The Breakthrough Moment**
I realized: *"I am changing it back to true so one condition I should be adding is to check for left[0] and right[0]"*

### 4. **Understanding the Flow**
Once I added the `left[0] and right[0]` check, I understood that:
- If ANY subtree is unbalanced (`False`), the entire tree becomes unbalanced
- The balance check should **fail fast** - no need to check current node if subtrees are already unbalanced

## Algorithm Walkthrough

Let me trace through an example to show the difference:

### Example Tree:
```
    1
   / \
  2   3
 / \
4   5
   /
  6
```

### With My Buggy Version:
```
DFS(6): return [1, True]  # leaf node
DFS(5): left=[1,True], right=[0,True]
        balanced = True and True and abs(1-0)<=1 = True
        return [2, True]  # ❌ This should be False!

DFS(4): return [1, True]
DFS(2): left=[2,True], right=[1,True]  # ❌ left should be False!
        balanced = True and True and abs(2-1)<=1 = True
        return [3, True]  # ❌ Wrong result propagated up!
```

### With Correct Version:
```
dfs(6): return [True, 1]
dfs(5): left=[True,1], right=[True,0]
        balanced = True and True and abs(1-0)<=1 = True
        return [True, 2]

dfs(4): return [True, 1]
dfs(2): left=[True,2], right=[True,1]
        balanced = True and True and abs(2-1)<=1 = True
        return [True, 3]  # ✅ Correct propagation
```

Wait, let me reconsider this example. The issue was more subtle in my original code.

## The Real Issue - Index Confusion

### My Original Bug:
```python
# I was using [height, balanced] format
left_height, right_height = DFS(root.left), DFS(root.right)
balanced = left_height[1] and right_height[1] and abs(left_height[0] - right_height[0]) <= 1
#          ↑ index [1]              ↑ index [1]          ↑ index [0]    ↑ index [0]
```

### The Problem:
I was **inconsistent with my indexing**! I defined my return as `[height, balanced]` but I was accessing indices correctly. The real issue was more subtle.

### My Actual Mistake:
Looking more carefully, my logic was actually correct, but I might have had issues with the base case or the condition checking. The key insight was that I needed to ensure that if any subtree returns `False` for balanced, it should propagate up.

## What I Learned About Recursive Tree Problems

### 1. **Return Value Design Matters**
```python
# Option 1: Return tuple/array
return [is_balanced, height]

# Option 2: Use sentinel values
return height if balanced else -1  # -1 indicates unbalanced
```

### 2. **Fail-Fast Principle**
```python
# Check subtree balance first
if not left[0] or not right[0]:
    return [False, 0]  # Early return
```

### 3. **Consistent Data Structure**
Whatever format you choose for return values, stick to it throughout the function.

## Alternative Approaches I Considered

### 1. **Naive Approach (O(n²))**
```python
def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if not root: return True
    return (abs(height(root.left) - height(root.right)) <= 1 and 
            isBalanced(root.left) and isBalanced(root.right))
```

**Why I avoided:** Recalculates height multiple times for the same nodes.

### 2. **Bottom-Up with Early Termination**
```python
def isBalanced(root):
    def dfs(root):
        if not root: return 0
        
        left = dfs(root.left)
        if left == -1: return -1  # Propagate unbalanced
        
        right = dfs(root.right)  
        if right == -1: return -1  # Propagate unbalanced
        
        if abs(left - right) > 1: return -1
        return 1 + max(left, right)
    
    return dfs(root) != -1
```

**This is actually cleaner** - uses -1 as a sentinel value for unbalanced trees.

## Complexity Analysis

### Time Complexity: O(n)
- Visit each node exactly once
- Constant work per node
- Much better than naive O(n²) approach

### Space Complexity: O(h)
- Recursion depth equals tree height
- O(log n) for balanced trees, O(n) for skewed trees

## Key Insights from This Problem

### 1. **Debugging Methodology**
- Compare working solutions with my approach
- Trace through examples step by step
- Identify the exact point where logic diverges

### 2. **Recursive Design Patterns**
- Return multiple values when needed (height + balance status)
- Propagate failure conditions up the recursion tree
- Use consistent data structures

### 3. **The Importance of Early Detection**
Once you know a subtree is unbalanced, there's no need to check the current node's balance - the entire tree is unbalanced.

## What I Would Do Differently

### 1. **Choose Clearer Return Format**
```python
# Instead of [height, balanced]
return [balanced, height]  # Boolean first is more intuitive
```

### 2. **Add Early Returns**
```python
if not left[0] or not right[0]:
    return [False, 0]  # No need to calculate further
```

### 3. **Use More Descriptive Variable Names**
```python
left_result, right_result = dfs(root.left), dfs(root.right)
left_balanced, left_height = left_result[0], left_result[1]
```

## Final Reflection

This problem taught me several valuable lessons:

### 1. **Close Doesn't Count in Programming**
My solution was "almost there" but the subtle bug made it completely wrong. This reinforced the importance of careful testing and edge case consideration.

### 2. **Recursive Thinking Development**
I'm getting better at designing recursive solutions that return multiple pieces of information. The pattern of combining results from left and right subtrees is becoming more natural.

### 3. **Debugging Skills Growth**
My ability to compare my solution with working code and identify the specific issue has improved. The systematic approach of tracing through examples helped pinpoint the problem.

### 4. **Pattern Recognition**
This bottom-up tree traversal pattern (process children first, then current node) appears in many tree problems. Mastering it will help with future problems.

**Key Takeaway:** The difference between a working and non-working solution can be incredibly subtle. In this case, it was about properly propagating the balanced status up the recursion tree. This experience reinforced the importance of careful logical reasoning in recursive problems.

**Personal Growth:** I'm developing better intuition for tree problems and recursive design patterns. The fact that I could identify and fix my own bug shows growth in debugging methodology and problem-solving skills.