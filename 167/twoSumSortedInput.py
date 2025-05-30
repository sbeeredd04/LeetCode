class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #start from left and right
        left, right = 0, len(numbers)-1

        while left < right: 
            #sum
            total = numbers[left] + numbers[right]

            #if the sum is greater than target then right -1 
            if total == target: 
                break

            elif total < target : 
                left += 1

            elif total > target : 
                right -= 1
        
        return left+1, right+1
        