class Solution:
    def numTilings(self, n: int) -> int:
        #modulus
        MOD = 1000000007
        dp = [[None] * 4 for _ in range(n + 1)]

        def makeState(t1, t2): 
            if (not t1 and  not t2): 
                return 0
            if (t1 and  not t2): 
                return 1
            if (not t1 and  t2): 
                return 2
            return 3

        #recursive funciton
        def recur(i , t1, t2): 

            #if at the last tile
            if i == n: 
                #only 1 way to put the domino
                return 1

            state = makeState(t1, t2)
            if dp[i][state] != None: 
                return dp[i][state]

            #t3 and t4 conditions to make sure not to go outside the range
            t3, t4 = i+1 < n, i+1 < n
            
            count = 0

            #conditions
            if (t1 and  t2 and  t3) : 
                count += recur(i+1, False, True)
            if (t1 and  t2 and  t4) : 
                count += recur(i+1, True, False)
            if (t1 and  not t2 and  t3 and  t4): 
                count += recur(i+1, False, False)
            if (not t1 and  t2 and  t3 and  t4): 
                count += recur(i+1, False, False)
            if (t1 and  t2): 
                count += recur(i+1, True, True)
            if (t1 and  t2 and  t3 and  t4):
                count += recur(i+1, False, False)
            if (t1 and  not t2 and  t3): 
                count += recur(i+1, False, True)
            if (not t1 and  t2 and  t4): 
                count += recur(i+1, True, False)
            if (not t1 and  not t2): 
                count += recur(i+1, True, True)
            
            dp[i][state] = count % MOD

            return dp[i][state]

        #run the recusion
        return recur(0, True, True)
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(f"Number of ways to tile a {n} x 2 board: {sol.numTilings(n)}")  # Output: 5
    n = 4
    print(f"Number of ways to tile a {n} x 2 board: {sol.numTilings(n)}")  # Output: 11