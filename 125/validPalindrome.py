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


# Example usage and testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("a", True),
        ("Madam", True),
        ("No 'x' in Nixon", True),
        ("Mr. Owl ate my metal worm", True),
        ("Was it a car or a cat I saw?", True),
        ("hello", False)
    ]
    
    print("Testing Two-Pointer Approach:")
    for i, (test_input, expected) in enumerate(test_cases):
        result = solution.isPalindrome(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: '{test_input}' → {result} (expected: {expected})")