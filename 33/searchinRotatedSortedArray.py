from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1

        while lo <= hi: 

            #mid
            mid = (lo + hi) // 2

            if nums[mid] < nums[hi] and nums[mid-1] < nums[mid] : 
                hi = mid - 1            #the deflection number is in the left half
            elif nums[mid] > nums[hi] and nums[mid-1] < nums[mid]: 
                lo = mid + 1            #the deflection number is in the right half
            elif nums[mid-1] > nums[mid]: 
                break
            else : 
                break

        if nums[mid] == target : 
            return mid
        elif nums[mid] != target and mid == 0 : 
            return self.binSearch(nums, target, mid, len(nums))
        elif nums[mid] != target and mid == len(nums)-1 : 
            return self.binSearch(nums, target, 0, mid)
        else :
            pass

        #binary search on both list
        result1, result2  = self.binSearch(nums, target, 0, mid), self.binSearch(nums, target, mid, len(nums))

        #return the number if any of numbers are not -1 then return the result
        if result1 != -1 or result2 != -1 : 
            return result1 + result2 + 1
        
        return -1

    def binSearch(self, nums: List[int], target: int, start: int, end: int) -> int: 

        lo, hi = start, end-1

        while lo <= hi : 

            mid = (lo + hi) // 2 

            if nums[mid] < target : 
                lo = mid + 1                #target is in right half
            elif nums[mid] > target :
                hi = mid - 1                #target is in left half
            else: 
                return mid
        
        #if target not found return -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    # Test cases
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(f"Search for {target} in {nums}: {sol.search(nums, target)}")  # Should return 4
    
    target = 3
    print(f"Search for {target} in {nums}: {sol.search(nums, target)}")  # Should return -1
    
    nums = [1]
    target = 1
    print(f"Search for {target} in {nums}: {sol.search(nums, target)}")  # Should return 0
