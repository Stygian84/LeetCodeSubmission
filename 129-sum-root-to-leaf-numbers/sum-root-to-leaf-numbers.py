# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def traverse(node,current):
            nonlocal total
            if node:
                if not node.left and not node.right: #leaf
                    total += current*10+node.val
                traverse(node.left, current*10+node.val)
                traverse(node.right, current*10+node.val)

        traverse(root,0)
        
        return total
