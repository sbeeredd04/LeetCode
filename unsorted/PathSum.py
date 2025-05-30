# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum, cache):
            if not node:
                return 0
            
            curr_sum += node.val
            # Get number of paths that sum to target ending at current node
            count = cache.get(curr_sum - targetSum, 0)
            
            # Add current sum to prefix sums map
            cache[curr_sum] = cache.get(curr_sum, 0) + 1
            
            # Recursively count paths in left and right subtrees
            total = count + dfs(node.left, curr_sum, cache) + dfs(node.right, curr_sum, cache)
            
            # Backtrack: remove current sum from map
            cache[curr_sum] -= 1
            
            return total
        
        # Initialize prefix sum map with 0 sum having frequency 1
        prefix_sums = {0: 1}
        return dfs(root, 0, prefix_sums)
            