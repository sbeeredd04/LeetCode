from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #need to the find the point where nums[mid-1] > nums[mid]
        lo, hi = 0, len(nums) -1 

        while lo <= hi: 

            #mid
            mid = (lo + hi) // 2

            if nums[mid] < nums[hi] and nums[mid-1] < nums[mid] : 
                hi = mid - 1            #the deflection number is in the left half
            elif nums[mid] > nums[hi] and nums[mid-1] < nums[mid]: 
                lo = mid + 1            #the deflection number is in the right half
            elif nums[mid-1] > nums[mid]: 
                return nums[mid]
            else : 
                break
        #if reached here, it means the while loop has ended at the point where lo > hi and the mid is the smallest element
        return nums[mid]
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    print(sol.findMin(nums))  # Output: 1

    nums = [4, 5, 6, 7, 0, 1, 2]
    print(sol.findMin(nums))  # Output: 0

    nums = [11, 13, 15, 17]
    print(sol.findMin(nums))  # Output: 11
    
    nums = [1, 2, 3, 4, 5]
    print(sol.findMin(nums))  # Output: 1