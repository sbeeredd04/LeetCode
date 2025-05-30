class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #first length of the cost
        n = len(cost)

        #if there is only 1
        if n == 1: 
            return cost[0]

        prev1 = cost[0]
        prev2 = cost[1]

        #for loop to get the cost
        for i in range(2, n): 
            result = cost[i] + min(prev1, prev2)
            prev1 = prev2
            prev2 = result

        return min(prev1, prev2)

if __name__ == "__main__":
    
    sol = Solution()
    cost = [10, 15, 20]
    print(f"Minimum cost to reach the top: {sol.minCostClimbingStairs(cost)}")  # Output: 15
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"Minimum cost to reach the top: {sol.minCostClimbingStairs(cost)}")  # Output: 6