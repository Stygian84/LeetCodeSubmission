# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def traverse(node):
            if node:
                traverse(node.left)
                res.append(node)
                traverse(node.right)
        traverse(root)

        x = y = None
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val:
                y = res[i + 1]
                if x is None:
                    x = res[i]
                else:
                    break
        
        if x and y:
            x.val, y.val = y.val, x.val