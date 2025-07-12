# 215. Kth Largest Element in an Array - Self-Reflection & Learning Notes

## Problem Recap
Given an unsorted array, I needed to find the kth largest element. This is a classic selection problem that can be solved efficiently with a heap.

## My Approach & Intuition

### 1. Recognizing the Heap Pattern
I immediately recognized that the fastest way to get the kth largest element is to use a **min-heap** of size k. This way, the heap always contains the k largest elements seen so far, and the smallest of these (the root) is the kth largest overall.

### 2. Using Python's `heapq`
I used Python's `heapq` library, which is a min-heap by default. For each number in the array, I pushed it onto the heap. If the heap grew larger than k, I popped the smallest element. At the end, the root of the heap is the answer.

### 3. Why Not Sort?
Sorting the array and picking the kth largest is easy, but it's O(n log n). The heap approach is O(n log k), which is much faster for large n and small k.

## Code Pattern
```python
import heapq

def findKthLargest(nums, k):
    minheap = []
    for num in nums:
        heapq.heappush(minheap, num)
        if len(minheap) > k:
            heapq.heappop(minheap)
    return minheap[0]
```

## What I Learned
- **Heaps are perfect for top-k problems**: They keep only what you need.
- **`heapq` is always a min-heap**: For max-heap, push negatives.
- **Space/time tradeoff**: Heap is O(k) space, O(n log k) time.
- **Sorting is simple but not optimal for this problem.**

## Self-Reflection
- I’m getting faster at spotting heap problems and using the right data structure.
- I’m comfortable with the `heapq` API and its quirks (min-heap only).
- I know when to use a heap vs. sort vs. quickselect.
- I’m building intuition for time/space tradeoffs in selection problems.

## Next Steps
- Try the quickselect (partition) approach for O(n) average time.
- Practice using heaps for streaming data and top-k queries.

---

**This problem reinforced my confidence with heaps and the Python `heapq` library!**
