# Linked Lists Deep Dive 🔗

## Table of Contents
- [Core Concepts](#core-concepts)
- [Common Patterns](#common-patterns)
- [Implementation Strategies](#implementation-strategies)
- [Time & Space Complexity](#time--space-complexity)
- [Common Mistakes](#common-mistakes)
- [Advanced Techniques](#advanced-techniques)

## Core Concepts
<details>
<summary>Click to expand</summary>

### 1. Node Structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 2. Basic Operations
```python
# Traversal
def traverse(head):
    curr = head
    while curr:
        # Process curr.val
        curr = curr.next

# Insertion
def insert_after(node, val):
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

# Deletion
def delete_after(node):
    if node.next:
        node.next = node.next.next
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Dummy Node Pattern
```python
def dummy_node_pattern():
    dummy = ListNode(0)  # Create dummy node
    curr = dummy        # Work with curr
    # ... operations ...
    return dummy.next   # Skip dummy in result
```

### 2. Fast & Slow Pointers
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Middle node
```

### 3. Multiple Pointers
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```
</details>

## Implementation Strategies
<details>
<summary>Click to expand</summary>

### 1. List Manipulation Templates

#### Reversing a List
```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

#### Finding Cycle
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

#### Merging Lists
```python
def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Common Operations
| Operation | Time | Space |
|-----------|------|-------|
| Access | O(n) | O(1) |
| Insert | O(1)* | O(1) |
| Delete | O(1)* | O(1) |
| Search | O(n) | O(1) |

*Assuming we have reference to the node

### Traversal Patterns
- Single pass: O(n)
- Fast & Slow: O(n)
- Multiple passes: O(kn)
</details>

## Common Mistakes
<details>
<summary>Click to expand</summary>

### 1. Null Pointer Errors
```python
# WRONG
curr.next = new_node  # curr might be None

# RIGHT
if curr:
    curr.next = new_node
```

### 2. Lost References
```python
# WRONG - Lost reference to next node
curr.next = prev
curr = curr.next

# RIGHT - Save next reference
next_temp = curr.next
curr.next = prev
curr = next_temp
```

### 3. Cycle Creation
```python
# WRONG - Creates cycle
last.next = head

# RIGHT - Check for cycle
if last != head:
    last.next = head
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Recursive Traversal
```python
def recursive_traverse(head):
    if not head:
        return
    # Process head.val
    recursive_traverse(head.next)
```

### 2. Multi-level Traversal
```python
def flatten_list(head):
    curr = head
    while curr:
        if curr.child:
            temp = curr.next
            curr.next = curr.child
            curr.child = None
            tail = curr.next
            while tail.next:
                tail = tail.next
            tail.next = temp
        curr = curr.next
```

### 3. In-place Operations
```python
def reorder_list(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Merge halves
    first = head
    second = prev
    while second.next:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
```
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [21. Merge Two Sorted Lists](../21/README.md)
- [141. Linked List Cycle](../141/README.md)
- [206. Reverse Linked List](../206/README.md)

### Medium
- [2. Add Two Numbers](../2/README.md)
- [19. Remove Nth Node From End of List](../19/README.md)
- [143. Reorder List](../143/README.md)

### Hard
- [146. LRU Cache](../146/README.md) (Uses doubly-linked list)
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Floyd's Cycle Detection Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
2. [Linked List on GeeksforGeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)
3. [Memory Management with Linked Lists](https://en.wikipedia.org/wiki/Linked_list#Memory_management)
</details>

---

*Remember: Many linked list problems can be solved with the right combination of pointer manipulation patterns. The key is identifying which pattern fits your current problem.*
