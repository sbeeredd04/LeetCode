# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float('-inf')

        def trackNodes(node, maxVal): 
            if not node : 
                return 0

            count = 1 if node.val >= maxVal else 0

            count += trackNodes(node.left, max(maxVal, node.val))
            count += trackNodes(node.right, max(maxVal, node.val))
            
            return count

        count = trackNodes(root, maxVal)
        return count