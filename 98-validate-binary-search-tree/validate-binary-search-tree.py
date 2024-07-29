# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, low, high):
            if not node:
                return True
            
            val = node.val
            if val <= low or val >= high:
                return False
            
            if not traverse(node.right, val, high):
                return False
            if not traverse(node.left, low, val):
                return False
            
            return True
        
        return traverse(root, -math.inf, math.inf)
           