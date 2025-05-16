from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #lenght of the nums array
        n = len(nums)

        #nested function
        def binarySearch(): 
            
            #start with the middle of the array and the left and right pointers
            left = 0
            right = n - 1
            mid = 0
            
            #start at middle and compare the elements with left and right elements for finding the peak lofPeak and rofPeak if left is greater then mid then move to the left side of the array else move to the right side of the array
            while left < right:
                
                mid = (left + right) // 2
                
                # if mid is greater than both left and right elements then return mid
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid
                
                #if right is greater than mid then move to the right side of the array
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                    
                #if left is greater than mid then move to the left side of the array
                else:
                    right = mid - 1
                    
            #if left and right are equal then return left
            return left
        
        #call the binarySearch function and return the result
        return binarySearch()
            

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.findPeakElement(nums))  # Output: 2 (index of peak element)
    
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(sol.findPeakElement(nums))  # Output: 5 (index of peak element)
    nums = [1, 2, 3, 4, 5]
    print(sol.findPeakElement(nums))  # Output: 4 (index of peak element)
    nums = [5, 4, 3, 2, 1]
    print(sol.findPeakElement(nums))  # Output: 0 (index of peak element)