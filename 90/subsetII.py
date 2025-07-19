class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def backtrack(i, curr):
            if i >= len(nums) : 
                res.add(tuple(curr))
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])

        #conver the result into list and sort
        res = list(res)
        res.sort()
        
        return res