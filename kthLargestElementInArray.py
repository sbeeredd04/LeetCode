from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert nums to a min-heap
        heapq.heapify(nums)
        
        # Pop the smallest elements until we have the k largest elements in the heap
        while len(nums) > k:
            heapq.heappop(nums)
        
        # The root of the heap is the kth largest element
        return heapq.heappop(nums)
