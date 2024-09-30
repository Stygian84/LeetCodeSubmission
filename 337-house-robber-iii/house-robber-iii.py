# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0) 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            robbed = node.val + left[1] + right[1]
            # If we do not rob this node, we take the max of either robbing or not robbing its children
            not_robbed = max(left) + max(right)
            
            return (robbed, not_robbed)
        
        return max(dfs(root))