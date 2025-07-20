from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
    
    def partition(self, s: str) -> List[List[str]]:

        palindromes = []

        def backtrack(string, currList=[]): 
 
            for index in range(0, len(string)):
                part1 = string[:index + 1]
                part2 = string[index + 1:]
                
                # Check if the first part is a palindrome
                if self.isPalindrome(part1):
                    currList.append(part1)
                    
                    # If the second part is empty, we have a valid partition
                    if not part2:
                        palindromes.append(currList.copy())
                    else:
                        # Recur for the second part
                        backtrack(part2, currList)
                    
                    # Backtrack by removing the last added palindrome
                    currList.pop()
                    
        backtrack(s)
        return palindromes



if __name__ == "__main__":
    sol = Solution()
    out = sol.partition("aaa")
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    print(f"Output: {out}, Expected: {expected}")
    assert out == expected, f"Test failed: {out} != {expected}"
    print("Test passed!")
    out = sol.partition("aab")
    expected = [["a", "a", "b"], ["aa", "b"]]
    print(f"Output: {out}, Expected: {expected}")
    assert out == expected, f"Test failed: {out} != {expected}"
    print("Test passed!")