from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total_cost = 0
        
        # Initialize two heaps for first and last candidates
        first_heap = [(costs[i], i) for i in range(min(candidates, n))]
        last_heap = [(costs[i], i) for i in range(max(n - candidates, candidates), n)]
        heapq.heapify(first_heap)
        heapq.heapify(last_heap)
        
        # Pointers for next workers to consider
        next_first = candidates
        next_last = n - candidates - 1
        
        # Hire k workers
        for _ in range(k):
            if not last_heap or (first_heap and first_heap[0] <= last_heap[0]):
                cost, index = heapq.heappop(first_heap)
                total_cost += cost
                if next_first <= next_last:
                    heapq.heappush(first_heap, (costs[next_first], next_first))
                    next_first += 1
            else:
                cost, index = heapq.heappop(last_heap)
                total_cost += cost
                if next_first <= next_last:
                    heapq.heappush(last_heap, (costs[next_last], next_last))
                    next_last -= 1
                    
        return total_cost
