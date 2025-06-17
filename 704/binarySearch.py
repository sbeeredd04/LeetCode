class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right : 

            #the mid number
            mid = (left + right) // 2

            if nums[mid] > target : 
                right = mid - 1 
            elif nums[mid] < target: 
                left = mid + 1
            else : 
                #found the target 
                return mid
            
        #return -1 if the target not found
        return -1