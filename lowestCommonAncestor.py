# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(node, target, path):
            if not node:
                return False
                
            path.append(node)
            
            if node == target:
                return True
                
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
                
            path.pop()
            return False
        
        path_p = []
        path_q = []
        
        findPath(root, p, path_p)
        findPath(root, q, path_q)
        
        # Find last common node in both paths
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
        
        return path_p[i-1]        