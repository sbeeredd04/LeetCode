
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        d = 0

        def maxDiameter(node): 
            nonlocal d
            if not node : 
                return 0
            left_height = maxDiameter(node.left)
            right_height = maxDiameter(node.right)
            d = max(left_height+right_height, d)
            return 1+max(left_height, right_height)
        
        maxDiameter(root)
        return d