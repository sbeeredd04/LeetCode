from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #make a hash set to store the unique numbers
        seen = set()

        for num in nums: 
            
            #first check if num is in seen
            if num in seen : 
                return True
            
            else : 

                #if number not in seen then add num to seen
                seen.add(num)
            
        return False
            
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.containsDuplicate(nums))  # Output: True

    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums))  # Output: False