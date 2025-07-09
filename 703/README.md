# Kth Largest Element in a Stream - Problem 703

## Problem Statement
Design a class to find the kth largest element in a stream. Implement the `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer k and the stream of integers nums.
- `int add(int val)` Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

## My Self-Reflection & Learning

### 1. My Solution and Why It Works

This problem is a classic use-case for a **min-heap**. I realized that to always get the kth largest element efficiently, I only need to keep track of the k largest elements seen so far. The smallest of these k elements (the root of the min-heap) is the kth largest overall.

**My Implementation:**
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k: 
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k: 
            heapq.heappop(self.minheap)
        return self.minheap[0]
```

### 2. Why I Used `heapq` and How It Helped

- **`heapq` is Python's built-in heap/priority queue library.**
- It implements a **min-heap** by default (smallest element at index 0).
- All heap operations (`heappush`, `heappop`, `heapify`) are O(log n).
- By keeping the heap size at k, I ensure that the root is always the kth largest element.

**Key heapq functions I used:**
- `heapq.heapify(nums)`: Turns a list into a heap in-place.
- `heapq.heappush(heap, val)`: Adds a value to the heap.
- `heapq.heappop(heap)`: Removes and returns the smallest value from the heap.

### 3. How My Algorithm Works (Step by Step)

**Initialization:**
- Heapify the input list.
- Pop elements until only k remain (so the heap always has the k largest elements).

**Adding a Value:**
- Push the new value onto the heap.
- If the heap grows beyond k, pop the smallest (to maintain only k largest).
- The root of the heap (`self.minheap[0]`) is the kth largest.

**Mermaid Diagram:**
```mermaid
flowchart TD
    A[Start: nums = [4,5,8,2], k=3] --> B[heapify(nums): [2,4,8,5]]
    B --> C[Pop until len(heap)==k: [4,5,8]]
    C --> D[add(3): push 3, heap=[3,4,8,5]]
    D --> E[Pop 3, heap=[4,5,8]]
    E --> F[Return 4 (kth largest)]
```

### 4. Why This Solution is Efficient
- **Time Complexity:**
  - Initialization: O(n log n) for heapify and popping
  - Each add: O(log k)
- **Space Complexity:** O(k) (heap never grows beyond k)

### 5. What I Did Well
- Used the right data structure for the job (min-heap)
- Leveraged Python's `heapq` for clean, efficient code
- Kept the heap size at k for optimal performance
- Wrote concise, readable logic

### 6. What I Could Improve or Explore
- **Naming:** I could use more descriptive names (e.g., `self.heap` instead of `self.minheap`)
- **Type Hints:** Add `import heapq` and `from typing import List` for clarity
- **Edge Cases:** What if nums is empty? My code still works, as heapq handles empty lists.
- **Max-Heap Alternative:** If I needed the kth smallest, I could use a max-heap (by pushing negatives).

### 7. Key Takeaways
- For "kth largest/smallest" problems in a stream, a fixed-size heap is almost always the answer.
- Python's `heapq` is powerful and easy to use for these scenarios.
- Always keep the heap size at k to ensure O(log k) operations.

### 8. Related Problems to Practice
- Kth Largest Element in an Array (LC 215)
- Find Median from Data Stream (LC 295)
- Top K Frequent Elements (LC 347)

**Memory Aid:**
> "Keep a min-heap of size k: the root is always the kth largest!"

**What Made My Solution Successful:**
1. ✅ Used the right data structure (min-heap)
2. ✅ Leveraged Python's standard library
3. ✅ Maintained optimal time and space complexity
4. ✅ Clean, readable, and bug-free implementation

