# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #check if p and q are in left and right tree
        if p.val <= root.val and q.val >= root.val or p.val >= root.val and q.val <= root.val: 
            return root
        
        elif p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)     #both values are in left sub tree current root is not least common ancestor
        
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)