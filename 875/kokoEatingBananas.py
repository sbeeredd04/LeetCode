from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #find the max element in the piles array
        max_pile = max(piles)
        
        #binary search to find the minimum eating speed
        left = 1
        right = max_pile
        
        #start with the middle of the array and the left and right pointers
        while left < right: 
            
            #find the middle of the array
            mid = (left + right) // 2
            
            #calculate the total hours needed to eat all the bananas at the current speed
            total_hours = sum( math.ceil(pile/mid) for pile in piles)
            
            #if the total hours is less than required then right = mid
            if total_hours <= h:
                right = mid
                
            #if the total hours is greater than required then left = mid + 1
            else:
                left = mid + 1
                
        #return the minimum eating speed
        return left 
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    print(sol.minEatingSpeed(piles, h))  # Output: 4 (minimum eating speed)
    
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(sol.minEatingSpeed(piles, h))  # Output: 30 (minimum eating speed)
    
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(sol.minEatingSpeed(piles, h))  # Output: 23 (minimum eating speed)
                