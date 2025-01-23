# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSequence(root, leaves):
            if not root:
                return
            # If leaf node (no children)
            if not root.left and not root.right:
                leaves.append(root.val)
            # Traverse left and right
            getLeafSequence(root.left, leaves)
            getLeafSequence(root.right, leaves)

        leaves1, leaves2 = [], []
        getLeafSequence(root1, leaves1)
        getLeafSequence(root2, leaves2)
        
        return leaves1 == leaves2
        