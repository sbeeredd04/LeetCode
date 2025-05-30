class Solution:
    def isPalindromeAlt(self, s: str) -> bool:
        """
        Alternative approach using string preprocessing.
        Time: O(n), Space: O(n)
        """
        # Clean string: keep only alphanumeric and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if cleaned string equals its reverse
        return cleaned == cleaned[::-1]