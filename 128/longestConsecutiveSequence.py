from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest_streak = 0
        
        for num in seen:
            
            #if a number has a left neighbor, it is not the start of a sequence else it is a start
            if num - 1 not in seen:
                current_num = num
                current_streak = 1
                
                #count the length of the sequence starting from this number
                while current_num + 1 in seen:
                    current_num += 1
                    current_streak += 1
                
                #update the longest streak found so far
                longest_streak = max(longest_streak, current_streak)
        


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, -1, 4, 6]))  # Output: 9
    print(solution.longestConsecutive([]))  # Output: 0
    print(solution.longestConsecutive([1]))  # Output: 1
    print(solution.longestConsecutive([1, 2, 3, 4, 5]))  # Output: 5
            