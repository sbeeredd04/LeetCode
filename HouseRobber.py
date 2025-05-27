from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        
        if n == 0 : 
            return 0
        if n == 1 : 
            return nums[0]

        n1 = 0
        n2 = nums[0]

        for i in range(1, n): 

            result = max((n1+nums[i]), n2)
            n1 = n2
            n2 = result
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2, 7, 9, 3, 1]))  # Example test case