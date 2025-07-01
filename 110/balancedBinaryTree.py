# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def DFS(root): 
            if not root: 
                return [0, True]
            left_height, right_height = DFS(root.left), DFS(root.right)
            balanced = left_height[1] and right_height[1] and abs(left_height[0] - right_height[0]) <= 1
            return [1 + max(left_height[0], right_height[0]), balanced]
        
        return DFS(root)[1]
    
