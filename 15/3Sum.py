from typing import List

class Solution: 
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        
        #first sort the array
        nums.sort()
        result = []
        
        k = len(nums) - 1
        
        while k >= 2: 
            
            i, j = 0, k - 1

            while i < j: 
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0: 
                    result.append([nums[i], nums[j], nums[k]])
                    
                    #skip duplicates
                    while i < j and nums[i] == nums[i+1]: 
                        i += 1
                    while i < j and nums[j] == nums[j-1]: 
                        j -= 1
                    
                    i += 1
                    j -= 1
                
                elif total < 0: 
                    i += 1
                
                else: 
                    j -= 1
            k -= 1

        #remove duplicates
        result = [list(x) for x in set(tuple(x) for x in result)]
        return result
    
# Example usage and testing 
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([0, 0, 0], [[0, 0, 0]])
    ]
    
    print("Testing Three Sum:")
    for i, (test_input, expected) in enumerate(test_cases):
        result = solution.threeSum(test_input)
        status = "✓" if sorted(result) == sorted(expected) else "✗"
        print(f"{status} Test {i+1}: {test_input} → {result} (expected: {expected})")