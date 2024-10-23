# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def traverse(node):
            nonlocal ls
            if node:
                traverse(node.left)
                ls.append(node.val)
                traverse(node.right)
        traverse(root)
        ls.sort()
        return ls[k-1]