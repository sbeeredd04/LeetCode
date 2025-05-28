# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        # Search for node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: Leaf node
            if not root.left and not root.right:
                return None
                
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
                
            # Case 3: Two children
            # Find successor (minimum value in right subtree)
            temp = self.findMin(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
            
        return root
        
    def findMin(self, root):
        current = root
        while current.left:
            current = current.left
        return current