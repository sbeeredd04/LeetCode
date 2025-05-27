class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        svals = {}
        tvals = {}

        for sval in s: 

            #if sval already in s increment the count
            if sval in svals: 
                svals[sval] += 1

            #else add the new value
            else : 
                svals[sval] = 1

        for tval in t: 

            #if tval already in s increment the count
            if tval in tvals: 
                tvals[tval] += 1

            #else add the new value
            else : 
                tvals[tval] = 1

        if len(svals) != len(tvals) : 
            return False

        else : 
            for val in svals: 
                if val in tvals : 
                    if svals[val] == tvals[val]:
                        # all values match dont need to check further
                        continue
                    else : 
                        return False
                else: 
                    return False

        # Return the final boolean result
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