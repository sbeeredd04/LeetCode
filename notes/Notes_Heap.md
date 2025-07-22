# Heap / Priority Queue Deep Dive 🏔️

## Table of Contents
- [Core Concepts](#core-concepts)
- [Python heapq Module](#python-heapq-module)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Problem-Solving Framework](#problem-solving-framework)

## Core Concepts
<details>
<summary>Click to expand</summary>

### What is a Heap?
A **heap** is a specialized tree-based data structure that satisfies the **heap property**:
- **Min-Heap**: Parent node ≤ both children (smallest element at root)
- **Max-Heap**: Parent node ≥ both children (largest element at root)

### Key Properties
1. **Complete Binary Tree**: All levels filled except possibly the last
2. **Heap Property**: Parent-child ordering constraint
3. **Efficient Operations**: Insert/Delete in O(log n)
4. **Array Representation**: No pointers needed

### When to Use Heaps
- Finding top-k elements efficiently
- Maintaining dynamic min/max
- Priority-based processing
- Scheduling algorithms
- Graph algorithms (Dijkstra, Prim)
</details>

## Python heapq Module
<details>
<summary>Click to expand</summary>

### Core Functions
```python
import heapq

# Creating a heap
heap = []  # Empty heap
heapq.heapify(nums)  # Convert list to heap in-place

# Basic operations
heapq.heappush(heap, item)    # Insert item: O(log n)
min_item = heapq.heappop(heap)  # Remove and return smallest: O(log n)
min_item = heap[0]            # Peek at smallest: O(1)

# Advanced operations
heapq.heappushpop(heap, item)  # Push then pop: O(log n)
heapq.heapreplace(heap, item)  # Pop then push: O(log n)
```

### Python Heap Quirks
**Important**: Python's `heapq` is a **MIN-HEAP only**!

#### Max-Heap Simulation
```python
# Method 1: Negate values
max_heap = []
heapq.heappush(max_heap, -value)
max_value = -heapq.heappop(max_heap)

# Method 2: Custom comparison (for objects)
import heapq
from dataclasses import dataclass, field

@dataclass
class MaxHeapItem:
    priority: int
    item: any = field(compare=False)
    
    def __lt__(self, other):
        return self.priority > other.priority  # Reverse for max-heap
```

#### Heap with Custom Objects
```python
# For list of lists: heap compares element [0] by default
heap = [[priority, value] for priority, value in items]
heapq.heapify(heap)

# For tuples: comparison by first element, then second, etc.
heap = [(priority, unique_id, data) for priority, data in items]
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Top-K Problems
```python
def find_k_largest(nums, k):
    # Use min-heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

def find_k_smallest(nums, k):
    # Use max-heap of size k (negate values)
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap]
```

### 2. Streaming Data
```python
class StreamProcessor:
    def __init__(self, k):
        self.k = k
        self.heap = []
    
    def add_value(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  # kth largest
```

### 3. Merge K Sorted Arrays
```python
def merge_k_sorted(arrays):
    heap = []
    result = []
    
    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    while heap:
        val, array_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same array
        if elem_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, array_idx, elem_idx + 1))
    
    return result
```

### 4. Frequency-Based Problems
```python
def top_k_frequent(nums, k):
    # Count frequencies
    from collections import Counter
    count = Counter(nums)
    
    # Use heap with frequency as priority
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Two-Heap Pattern (Median)
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (use negative values)
        self.large = []  # min-heap
    
    def add_num(self, num):
        # Add to appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
```

### 2. Lazy Deletion Pattern
```python
class LazyHeap:
    def __init__(self):
        self.heap = []
        self.deleted = set()
    
    def push(self, val):
        heapq.heappush(self.heap, val)
    
    def pop(self):
        while self.heap and self.heap[0] in self.deleted:
            heapq.heappop(self.heap)
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def delete(self, val):
        self.deleted.add(val)
```

### 3. Heap with Unique Elements
```python
class UniqueHeap:
    def __init__(self):
        self.heap = []
        self.seen = set()
    
    def push(self, val):
        if val not in self.seen:
            heapq.heappush(self.heap, val)
            self.seen.add(val)
    
    def pop(self):
        if self.heap:
            val = heapq.heappop(self.heap)
            self.seen.remove(val)
            return val
        return None
```
</details>

## Problem-Solving Framework
<details>
<summary>Click to expand</summary>

### 1. Identify Heap Usage
**Use heaps when you need:**
- Top-k elements
- Dynamic min/max queries
- Priority-based processing
- Efficient access to extremes

### 2. Choose Heap Type
- **Min-Heap**: Finding smallest, kth largest
- **Max-Heap**: Finding largest, kth smallest
- **Two Heaps**: Finding median, range queries

### 3. Handle Edge Cases
- Empty heap operations
- Heap size constraints
- Duplicate elements
- Custom comparison requirements

### 4. Optimization Strategies
- Use `heapify` for bulk initialization
- Consider `heappushpop` for combined operations
- Implement lazy deletion for removals
- Use counter + heap for frequency problems
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [703. Kth Largest Element in a Stream](../703/README.md)
- [1046. Last Stone Weight](../1046/README.md)

### Medium
- [215. Kth Largest Element in an Array](../215/README.md)
- [347. Top K Frequent Elements](../347/README.md)
- [621. Task Scheduler](../621/README.md)
- [973. K Closest Points to Origin](../973/README.md)

### Hard
- [295. Find Median from Data Stream](#) *(if available)*
- [23. Merge k Sorted Lists](#) *(if available)*
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Heap Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| heappush | O(log n) | O(1) |
| heappop | O(log n) | O(1) |
| heappushpop | O(log n) | O(1) |
| heapify | O(n) | O(1) |
| peek (heap[0]) | O(1) | O(1) |

### Common Problem Complexities
- **Top-K**: O(n log k) time, O(k) space
- **Heap Sort**: O(n log n) time, O(1) space
- **Merge K Arrays**: O(n log k) time, O(k) space
- **Stream Processing**: O(log k) per operation, O(k) space
</details>

## Common Pitfalls & Best Practices
<details>
<summary>Click to expand</summary>

### ❌ Common Mistakes
1. **Forgetting Min-Heap Default**
   ```python
   # Wrong: Assuming max-heap
   heapq.heappush(heap, val)
   max_val = heapq.heappop(heap)  # Actually gives min!
   ```

2. **Index Errors**
   ```python
   # Wrong: Not checking if heap is empty
   min_val = heap[0]  # IndexError if heap is empty
   ```

3. **Incorrect Max-Heap Implementation**
   ```python
   # Wrong: Negating after popping
   heapq.heappush(max_heap, -val)
   max_val = heapq.heappop(max_heap)  # Still negative!
   ```

### ✅ Best Practices
1. **Always Check Empty Heap**
   ```python
   if heap:
       min_val = heap[0]
   ```

2. **Consistent Max-Heap Pattern**
   ```python
   # Push: negate
   heapq.heappush(max_heap, -val)
   # Pop: negate again
   max_val = -heapq.heappop(max_heap)
   ```

3. **Use heapify for Initial Setup**
   ```python
   # Efficient: O(n)
   heapq.heapify(nums)
   # Inefficient: O(n log n)
   for num in nums:
       heapq.heappush(heap, num)
   ```
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Python heapq Documentation](https://docs.python.org/3/library/heapq.html)
2. [Heap Data Structure Visualization](https://www.cs.usfca.edu/~galles/visualization/Heap.html)
3. [Priority Queue Applications](https://en.wikipedia.org/wiki/Priority_queue)
</details>

---

*Remember: Heaps are perfect for maintaining access to extremes (min/max) in dynamic datasets. Master the top-k pattern and max-heap simulation for most interview problems.* 