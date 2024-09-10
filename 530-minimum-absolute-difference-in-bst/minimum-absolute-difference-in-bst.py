# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp = []

        def traverse(node):
            nonlocal temp
            if node:
                traverse(node.left)
                temp.append(node.val)
                traverse(node.right)
        
        traverse(root)
        res = math.inf

        for i in range(len(temp)-1):
            res = min(res, abs(temp[i+1]-temp[i]))
        
        return res