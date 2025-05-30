class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #sort both strings and compare them by popping characters
        if len(s) != len(t):
            return False
        
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        
        if ''.join(s_list) != ''.join(t_list):
            return False

        return True
    
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))  # Output: True

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))  # Output: False
    s = "a"
    t = "ab"
    print(solution.isAnagram(s, t))  # Output: False
    s = "a"
    t = "a"
    print(solution.isAnagram(s, t))  # Output: True
    s = "aa"
    t = "aa"
    print(solution.isAnagram(s, t))  # Output: True
    s = "aab"
    t = "baa"
    print(solution.isAnagram(s, t))  # Output: True
    s = "aabb"
    t = "abab"
    print(solution.isAnagram(s, t))  # Output: True