class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        count = [[] for i in range(len(nums) + 1)]
        
        for num in nums: 
            
            if num in d: 
                d[num] += 1
            else:
                d[num] = 1
                
        for num, freq in d.items():
            
            count[freq].append(num)
        
        result = []
        # for i in range(len(count) - 1, 0, -1):
        #     if count[i]:
        #         result.extend(count[i])
        #         if len(result) >= k:
        #             return result[:k]
        
        #OR using whjile loop
        while k > 0:
            
            i = len(count) - 1
            while i > 0 and not count[i]:
                i -= 1
            if i == 0:
                break
            
            result.append(count[i].pop())
            k -= 1
            
        return result