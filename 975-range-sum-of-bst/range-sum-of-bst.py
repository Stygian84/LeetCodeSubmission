# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result=[]
        def traverse(root,result):
            if root:
                traverse(root.left,result)
                if high>=root.val>=low:
                    result+=[root.val]
                traverse(root.right,result)
        traverse(root,result)
        return sum(result)