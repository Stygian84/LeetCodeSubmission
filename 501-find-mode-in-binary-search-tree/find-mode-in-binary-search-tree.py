# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dc={}
        def traverse(x):
            if x:
                dc[x.val]=dc.get(x.val,0)+1
                traverse(x.left)
                traverse(x.right)
        traverse(root)
        mode=max(dc.values())
        res=[]
        for key,values in dc.items():
            if values==mode:
                res.append(key)
        return res