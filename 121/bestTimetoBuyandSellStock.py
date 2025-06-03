from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_min = prices[0] if prices else 0
        max_profit = 0
        
        for price in prices:   
            
            # Update the minimum price seen so far
            left_min = min(left_min, price)
            
            # Calculate profit if we sell at the current price
            profit = price - left_min
            
            # Update the maximum profit if this profit is greater
            max_profit = max(max_profit, profit)
        return max_profit if max_profit > 0 else 0


# Example usage and testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2], 1)
    ]
    
    print("Testing Max Profit Calculation:")
    for i, (test_input, expected) in enumerate(test_cases):
        result = solution.maxProfit(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Test {i+1}: {test_input} → {result} (expected: {expected})")