# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base cases: root is None or we found the value
        if not root or root.val == val:
            return root
            
        # If val is less than current node, search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is greater than current node, search right subtree
        return self.searchBST(root.right, val)