from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        o, c = 1, 0
        l = 1
        permutation = []
        s = "("

        #start with the string lenght of the string and count of open and closed and the actual string
        def recur(length, o , c, s): 

            #if the length is 2n and the o = c then return 1 else if c > o return 0
            if length == 2*n and o == c: 
                return s
            elif c > o or o > n or c > n : 
                return None
            elif length == 2*n and o > c:
                return None
            else : 
                #add the count by incrementing o once and c once
                result1 = recur(length+1, o+1, c, s + "(") 
                result2 = recur(length+1, o, c+1, s+")")
                if result1: 
                    permutation.append(result1)
                if result2: 
                    permutation.append(result2)
            
        
        #call the function
        recur(l, o, c, s)
        return permutation

if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(f"Parentheses for {n} is: {sol.generateParenthesis(n)}") 