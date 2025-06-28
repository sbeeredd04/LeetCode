# Merge Two Sorted Lists (LeetCode 21) - My Learning Journey

## Problem Understanding

I needed to merge two sorted linked lists into one sorted linked list. The key insight is that both input lists are already sorted, so I can use a "merge" approach similar to the merge step in merge sort.

**Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`  
**Output:** `[1,1,2,3,4,4]`

## My Solution Approach: Dummy Node Pattern

### The Core Strategy I Discovered

Instead of handling complex edge cases about which list to start with, I used a **dummy node** to simplify the logic:

```python
dummy = ListNode(0)  # Placeholder node
curr = dummy         # Pointer to build result
```

This dummy node acts as a "fake head" that makes pointer manipulation much cleaner.

### Algorithm Breakdown

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create dummy node to simplify logic
    dummy = ListNode(0)
    curr = dummy
    
    # Merge while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    # Attach remaining nodes
    curr.next = list1 or list2
    
    return dummy.next  # Skip the dummy node
```

## Step-by-Step Visualization

Let me trace through `list1: 1->2->4` and `list2: 1->3->4`:

### Initial State
```
dummy -> NULL
curr = dummy
list1: 1 -> 2 -> 4 -> NULL
list2: 1 -> 3 -> 4 -> NULL
```

### Iteration 1: Compare 1 vs 1
```
1 <= 1, so choose list1
curr.next = list1 (node with value 1)
list1 = list1.next (moves to 2)
curr = curr.next (moves to the 1 node)

Result: dummy -> 1 -> NULL
        curr = 1 node
        list1: 2 -> 4 -> NULL
        list2: 1 -> 3 -> 4 -> NULL
```

### Iteration 2: Compare 2 vs 1
```
2 > 1, so choose list2
curr.next = list2 (node with value 1)
list2 = list2.next (moves to 3)
curr = curr.next (moves to the 1 node from list2)

Result: dummy -> 1 -> 1 -> NULL
        curr = second 1 node
        list1: 2 -> 4 -> NULL
        list2: 3 -> 4 -> NULL
```

### Iteration 3: Compare 2 vs 3
```
2 <= 3, so choose list1
curr.next = list1 (node with value 2)
list1 = list1.next (moves to 4)
curr = curr.next (moves to the 2 node)

Result: dummy -> 1 -> 1 -> 2 -> NULL
        curr = 2 node
        list1: 4 -> NULL
        list2: 3 -> 4 -> NULL
```

### Iteration 4: Compare 4 vs 3
```
4 > 3, so choose list2
curr.next = list2 (node with value 3)
list2 = list2.next (moves to 4)
curr = curr.next (moves to the 3 node)

Result: dummy -> 1 -> 1 -> 2 -> 3 -> NULL
        curr = 3 node
        list1: 4 -> NULL
        list2: 4 -> NULL
```

### Iteration 5: Compare 4 vs 4
```
4 <= 4, so choose list1
curr.next = list1 (node with value 4)
list1 = list1.next (becomes NULL)
curr = curr.next (moves to the 4 node)

Result: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> NULL
        curr = 4 node
        list1: NULL
        list2: 4 -> NULL
```

### Final Step: Attach Remaining
```
list1 is NULL, list2 has remaining nodes
curr.next = list1 or list2 = list2 (the remaining 4 node)

Final: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> NULL
Return: dummy.next (skips the dummy, returns actual merged list)
```

## Key Insights I Discovered

### 1. The Dummy Node Pattern
**Why It's Brilliant:**
- Eliminates the need to handle "empty result list" edge cases
- Provides a consistent starting point
- Simplifies pointer logic since I always have a `curr` to work with

**Without Dummy Node (More Complex):**
```python
if not list1: return list2
if not list2: return list1

# Need to determine which node becomes the head
if list1.val <= list2.val:
    head = list1
    list1 = list1.next
else:
    head = list2
    list2 = list2.next

curr = head
# ... rest of merging logic
```

### 2. The `list1 or list2` Trick
```python
curr.next = list1 or list2
```

This is elegant because:
- If `list1` is not `None`, use `list1`
- If `list1` is `None` but `list2` is not `None`, use `list2`
- If both are `None`, result is `None` (correct)

### 3. Pointer Movement Pattern
```python
curr.next = chosen_list  # Link to chosen node
chosen_list = chosen_list.next  # Advance chosen list
curr = curr.next  # Advance result list
```

This pattern appears in many linked list problems.

## Edge Cases My Solution Handles

### 1. One List is Empty
```python
list1 = None, list2 = [1,2,3]
# while loop never executes
# curr.next = list1 or list2 = list2
# Returns list2 correctly
```

### 2. Both Lists Empty
```python
list1 = None, list2 = None
# while loop never executes
# curr.next = None or None = None
# Returns None correctly
```

### 3. Lists of Different Lengths
```python
list1 = [1,2], list2 = [3,4,5,6]
# After merging [1,2,3], remaining [4,5,6] gets attached
```

### 4. All Elements from One List Come First
```python
list1 = [1,2,3], list2 = [4,5,6]
# Merges to [1,2,3,4,5,6] correctly
```

## Complexity Analysis

### Time Complexity: O(m + n)
- `m` = length of list1, `n` = length of list2
- Visit each node exactly once
- Each comparison and pointer update is O(1)

### Space Complexity: O(1)
- Only using constant extra space for pointers
- Not creating new nodes, just rearranging existing ones
- The dummy node is the only additional memory used

## Alternative Approaches I Considered

### 1. Recursive Solution
```python
def mergeTwoLists(self, list1, list2):
    if not list1: return list2
    if not list2: return list1
    
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
```

**Why I Chose Iterative:**
- O(1) space vs O(m+n) space for recursion
- Easier to debug and trace
- No risk of stack overflow on large lists

### 2. In-Place Insertion Approach
Insert each node from list2 into list1 one by one.

**Why I Rejected This:**
- More complex logic for finding insertion points
- Less efficient (potentially O(m*n) in worst case)
- Harder to maintain sorted order

### 3. Convert to Arrays, Merge, Rebuild
**Why I Rejected This:**
- O(m+n) extra space
- More operations (convert → sort → rebuild)
- Doesn't utilize the fact that inputs are already sorted

## Common Mistakes I Avoided

### ❌ Forgetting to Skip Dummy Node
```python
return dummy  # WRONG - includes dummy
return dummy.next  # CORRECT - actual merged list
```

### ❌ Not Handling Remaining Nodes
```python
# Missing this line would lose remaining nodes
curr.next = list1 or list2
```

### ❌ Incorrect Pointer Updates
```python
curr.next = list1
curr = curr.next  # Must advance curr
# Missing curr advancement causes infinite loop
```

### ❌ Creating New Nodes
```python
curr.next = ListNode(list1.val)  # WRONG - wastes space
curr.next = list1  # CORRECT - reuse existing nodes
```

## Debugging Experience

### Initial Error I Fixed
```
TypeError: [] is not valid value for the expected return type ListNode
```

**Root Cause:** I was returning `[]` (empty Python list) instead of `None` for empty linked lists.

**The Fix:** Ensured all return paths return `Optional[ListNode]` types.

### Missing Import Issue
```python
from typing import Optional  # Essential for type hints
```

## Final Reflection

This problem taught me several important patterns:

### 1. Dummy Node Pattern
A powerful technique for simplifying linked list operations by providing a consistent starting point.

### 2. Two-Pointer Merge
The core algorithm behind merge sort's merge step, applicable to many sorting and merging problems.

### 3. Edge Case Handling
Using `list1 or list2` is an elegant way to handle remaining elements.

### 4. Space-Time Trade-offs
My O(1) space iterative solution vs O(m+n) space recursive solution.

**Key Insight:** The dummy node pattern transforms a potentially complex edge-case-heavy problem into clean, straightforward logic. This technique appears in many linked list problems and is worth mastering.

The solution efficiently merges two sorted lists while maintaining the sorted property, handles all edge cases naturally, and uses optimal time and space complexity.