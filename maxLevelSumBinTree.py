# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque([root])
        max_sum = float('-inf')
        result_level = 1
        current_level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            # Process current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update max sum and result level
            if level_sum > max_sum:
                max_sum = level_sum
                result_level = current_level
                
            current_level += 1
        
        return result_level