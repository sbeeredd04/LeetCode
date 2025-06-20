from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new = []
        #join the list [[1,3,5,7],[10,11,16,20],[23,30,34,60]] -> [1,3,5,7,10,11,16,20,23,30,34,60]
        for lst in matrix: 

            #join the list
            new += lst
        
        print(new)

        # do binary search on list 
        low, hi, mid = 0, len(new) - 1, 0

        #while loop
        while low <= hi : 
            mid = (low + hi) // 2

            if new[mid] < target : 
                low = mid + 1       #target in right half
            elif new[mid] > target :  
                hi = mid - 1        #target in left half
            else : 
                return True         #target found
    
        #if reached here target not found
        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    sol = Solution()
    print(sol.searchMatrix(matrix, target))  # Output: True
    target = 13
    print(sol.searchMatrix(matrix, target))  # Output: False
    target = 60
    print(sol.searchMatrix(matrix, target))  # Output: True