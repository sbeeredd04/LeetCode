# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, res) : 

            if not root : 
                return 
            
            inOrder(root.left, res) 
            
            res.append(root.val)  
            
            inOrder(root.right, res)

            return res
        
        return inOrder(root, [])[k-1]