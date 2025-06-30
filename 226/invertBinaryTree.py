# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recur(node): 

            if node.left and node.right : 
                node.left, node.right = node.right, node.left

            if node.left: 
                recur(node.left)
            if node.right: 
                recur(node.right)

            if not node.left or node.right : 
                pass

        #start the recursion from root node
        recur(root) if root else None
        return root 


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    solution = Solution()
    inverted_root = solution.invertTree(root)