from typing import List
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    stream=sys.stdout
)
logger = logging.getLogger("CombinationSum3")

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        logger.info(f"\n{'='*50}\nPROBLEM: Find all combinations of {k} numbers that sum to {n}\n{'='*50}")
        
        # Early validation 
        if k <= 0 or n <= 0:
            logger.info(f"Early validation failed: k={k}, n={n}")
            return []
        
        # Create the list to store the combinations
        combinations = []
        recursion_depth = 0  # Track recursion depth for indentation
        
        # Backtracking function
        def backtrack(start: int, current_combination: list, remaining: int): 
            nonlocal recursion_depth
            
            # Create indentation based on recursion depth for better visualization
            indent = "  " * recursion_depth
            
            logger.debug(f"{indent}ENTER Recursion Level {recursion_depth}:")
            logger.debug(f"{indent}│ Current: {current_combination}, Remaining: {remaining}, Start: {start}")
            
            # Base cases
            if len(current_combination) == k:
                if remaining == 0:
                    logger.debug(f"{indent}│ ✓ FOUND VALID COMBINATION: {current_combination}")
                    combinations.append(current_combination.copy())  # Make a copy
                else:
                    logger.debug(f"{indent}│ ✗ COMBINATION of length k but sum != n: {current_combination}")
                logger.debug(f"{indent}EXIT Recursion Level {recursion_depth}\n")
                return
            
            # Early pruning
            if remaining <= 0:
                logger.debug(f"{indent}│ ✗ PRUNE: remaining={remaining} <= 0")
                logger.debug(f"{indent}EXIT Recursion Level {recursion_depth}\n")
                return
            
            if len(current_combination) > k:
                logger.debug(f"{indent}│ ✗ PRUNE: combination length={len(current_combination)} > k={k}")
                logger.debug(f"{indent}EXIT Recursion Level {recursion_depth}\n")
                return
            
            # Try each valid digit
            possible_digits = list(range(start, 10))
            logger.debug(f"{indent}│ Considering digits: {possible_digits}")
            
            for digit in possible_digits:
                # Skip if adding this digit would exceed the target
                if digit > remaining:
                    logger.debug(f"{indent}│ ✗ SKIP digit {digit}: exceeds remaining={remaining}")
                    break
                
                # Choose
                current_combination.append(digit)
                logger.debug(f"{indent}│ CHOOSE digit {digit} -> Current: {current_combination}")
                
                # Explore (only use digits greater than the current one)
                recursion_depth += 1
                backtrack(digit + 1, current_combination, remaining - digit)
                recursion_depth -= 1
                
                # Unchoose (backtrack)
                removed = current_combination.pop()
                logger.debug(f"{indent}│ BACKTRACK: Remove {removed} -> Current: {current_combination}")
            
            logger.debug(f"{indent}EXIT Recursion Level {recursion_depth} (no more digits to try)\n")

        # Call the backtracking with starting digit 1
        logger.info(f"Starting backtracking with k={k}, n={n}")
        backtrack(1, [], n)
        
        logger.info(f"\nFinal Result: Found {len(combinations)} combinations")
        for i, combo in enumerate(combinations):
            logger.info(f"Combination {i+1}: {combo} (sum={sum(combo)})")
        
        logger.info(f"{'='*50}\n")
        return combinations
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    k = 3
    n = 7
    print(sol.combinationSum3(k, n))  # Output: [[1, 2, 4]]

    k = 3
    n = 9
    print(sol.combinationSum3(k, n))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    
    k = 4
    n = 1
    print(sol.combinationSum3(k, n))  # Output: []

