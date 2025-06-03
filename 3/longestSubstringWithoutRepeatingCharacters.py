class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        #keep track of left index
        l, r = 0, 0
        longest = 0
        
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1
            
            longest = max(longest, r - l)
        return longest

# Example usage and testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),          # Empty string
        ("a", 1),         # Single character
        ("dvdf", 3)       # "vdf"
    ]
    
    print("Testing Longest Substring Without Repeating Characters:")
    for i, (test_input, expected) in enumerate(test_cases):
        result = solution.lengthOfLongestSubstring(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: '{test_input}' → {result} (expected: {expected})")