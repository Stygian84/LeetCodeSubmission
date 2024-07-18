# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a=[]
        b=[]
        def traverse(root,result):
            if root:
                if not root.left:
                    result.append(None)
                if not root.right:
                    result.append(None)
                traverse(root.left,result)
                result.append(root.val)
                traverse(root.right,result)
        traverse(p,a)
        traverse(q,b)
        return a==b