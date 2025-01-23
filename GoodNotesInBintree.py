# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
                
            # Count current node if it's >= max seen so far
            count = 1 if node.val >= max_so_far else 0
            
            # Update max value for path
            current_max = max(max_so_far, node.val)
            
            # Recursively count good nodes in left and right subtrees
            count += dfs(node.left, current_max)
            count += dfs(node.right, current_max)
            
            return count
        
        return dfs(root, float('-inf'))
            