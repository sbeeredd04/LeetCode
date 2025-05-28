class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #total product
        total_product = 1
        count0 = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                count0 += 1
        if count0 > 1:
            return [0] * len(nums)
        
        for num in range(len(nums)):
            if count0 == 1:
                if nums[num] == 0:
                    nums[num] = total_product
                else:
                    nums[num] = 0
            else:
                nums[num] = total_product // nums[num]
        return nums