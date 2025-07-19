class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        n = len(nums)

        def dfs(curr, available): 

            if len(curr) == n or not available: 
                res.append(curr.copy())
                return

            for num in available: 
                curr.append(num)
                copy = available.copy()
                copy.remove(num)
                dfs(curr, copy)
                curr.pop()
            
            return

        dfs([], set(nums))
        return res