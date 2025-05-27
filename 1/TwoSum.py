class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #convert nums into dict
        d = {value: index for index, value in enumerate(nums)}

        #try to find difference number for each number in nums
        for i in range(0, len(nums)): 

            if target-nums[i] in d: 
                if d[target-nums[i]] == i: 
                    continue
                return i, d[target-nums[i]]
        
        return None