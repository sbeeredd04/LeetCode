from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If we've seen the complement before, we found our answer
            if complement in seen:
                return [seen[complement], i]
            
            # Add current number to the dictionary
            seen[num] = i
        
        # No solution found (though problem states one solution exists)
        return None

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Output: [0, 1]

    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))  # Output: [1, 2]

    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))  # Output: [0, 1]