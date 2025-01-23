# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # Process current level
            for i in range(level_size):
                node = queue.popleft()
                
                # Add left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                # Add rightmost node value of current level
                if i == level_size - 1:
                    result.append(node.val)
        
        return result        