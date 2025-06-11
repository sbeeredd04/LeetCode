class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        s2dict = {}
        left = 0
        maxs = len(s1)

        if maxs > len(s2): 
            return False

        for char in s1: 
            if char in s1dict: 
                s1dict[char] += 1
            else : 
                s1dict[char] = 1
                
        print(f"s1dict: {s1dict}")
        
        for r in range(0, len(s1)-1) : 
            
            #add the current char to s2 
            if s2[r] in s2dict : 
                s2dict[s2[r]] += 1
            else : 
                s2dict[s2[r]] = 1
                
        print(f"Initial s2dict: {s2dict}")
        print("\n\n")
        #start sliding the window

        for r in range(len(s1)-1, len(s2)) : 
            
            print(f"Window: {s2[left:r+1]}")
            #first
            if s2[r] in s2dict : 
                s2dict[s2[r]] += 1
            else : 
                s2dict[s2[r]] = 1

            print(f"Updated s2dict: {s2dict}")

            print(f"Comparing s1dict: {s1dict} with s2dict: {s2dict}")
            if s1dict == s2dict : 
                return True
            
            else : 
                #remove the char count from the dict
                if s2dict[s2[left]] > 1 : 
                    s2dict[s2[left]] -= 1
                else : 
                    del s2dict[s2[left]]

                print(f"After removing {s2[left]} from s2dict: {s2dict}")
                
                left += 1
            
            print("\n\n")
        print("No permutation found.")
        return False


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    print(solution.checkInclusion(s1, s2))  # Output: True
    print("-----"* 20)
    print("\n\n")
    s1 = "ab"
    s2 = "eidboaoo"
    print(solution.checkInclusion(s1, s2))  # Output: False