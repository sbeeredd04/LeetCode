# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #list to hold the result of level order traversal
        res = []

        # Helper function to perform level order traversal recursively
        def level_order_rec(root, level, res):
            # Base case: If node is null, return
            if root is None:
                return

            # Add a new level to the result if needed
            if len(res) <= level:
                res.append([])

            # Add current node's data to its corresponding level
            res[level].append(root.val)

            # Recur for left and right children
            level_order_rec(root.left, level + 1, res)
            level_order_rec(root.right, level + 1, res)
        
        # Start the recursive traversal from the root at level 0
        level_order_rec(root, 0, res)
        return res