class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x == y : 
                continue
            else: 
                res = y-x
                heapq.heappush(stones, res)
                print(f"res: {x}-{y} = {-res}, list: {[-stone for stone in stones]}")
            
        return -stones[0] if stones else 0
            