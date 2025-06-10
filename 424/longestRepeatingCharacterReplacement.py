class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        words = {}

        #edge cases 
        if n == 0 or k < 0:
            return 0
        if n == 1:
            return 1
        if k >= n:
            return n
        
        #left and right pointers
        left, right = 0, 1
        
        #current window size and max window size
        w, maxw = 0 , 0
        words[s[left]] = 1

        while right < n:
            w = right - left + 1
            print(f"Current window: {s[left:right+1]}, left: {left}, right: {right}, w: {w}, maxw: {maxw}")
            if s[right] in words:
                print(f"Incrementing count of {s[right]}")
                words[s[right]] += 1
            else: 
                print(f"Adding {s[right]} to words")
                words[s[right]] = 1

            #get the current max frequency of a character in the window
            topf = max(words.values())
            print(f"Current character counts: {words}")
            print(f"Current window size: {w}, top frequency: {topf}, k: {k}")

            if w - topf <= k : 
                print(f"Window size {w} is valid, moving right pointer")
                right += 1
                maxw = max(maxw, w)
            else : 
                print(f"Window size {w} is invalid, moving left pointer and decrementing count of {s[left]} from words {words[s[left]]}") 
                #decrement the count of the character at the left pointer
                words[s[left]] -= 1
                left += 1
                right += 1
                maxw = max(maxw, w - 1)

            print(f"Updated max window size: {maxw}")
            print(f"\n\n")
        return maxw
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    result = sol.characterReplacement("ABAB", 0)
    print(f"Result: {result}")  # Expected output: 4