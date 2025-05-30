# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def longestZigZag(self, root: Optional[TreeNode]) -> int:
    def dfs(node, going_left, count):
        if not node:
            return 0
        
        # Update maximum seen so far
        self.max_length = max(self.max_length, count)
        
        if going_left:
            # Continue zigzag to right
            dfs(node.right, False, count + 1)
            # Start new zigzag from left
            dfs(node.left, True, 1)
        else:
            # Continue zigzag to left
            dfs(node.left, True, count + 1)
            # Start new zigzag from right
            dfs(node.right, False, 1)
    
    if not root:
        return 0
        
    self.max_length = 0
    # Start paths from both directions
    dfs(root, True, 0)
    dfs(root, False, 0)
    return self.max_length