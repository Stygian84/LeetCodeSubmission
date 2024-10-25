# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = None
        def traverse(node):
            nonlocal res
            if res:
                return
            if node:
                if node.val == target.val:
                    res = node
                    return
                traverse(node.left)
                traverse(node.right)

        traverse(cloned)  
        return res