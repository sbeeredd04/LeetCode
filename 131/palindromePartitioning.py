from typing import List

class Solution:
    def isPalindrome(self, s: str, left, right) -> bool:
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
        res = []
        part = []
        def dfs(i):
            print(f"dfs({i}), part: {part}")  # Debugging
            if i >= len(s):
                print(f"  End reached, append: {part}")
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    print(f"  Palindrome found: {s[i:j+1]}")
                    part.append(s[i:j+1])
                    dfs(j+1)
                    print(f"  Backtrack, pop: {part[-1]}")
                    part.pop()
        dfs(0)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("abccba"))  # Example usage