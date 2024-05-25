# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(root,result):
            if root:
                traverse(root.left,result)
                traverse(root.right,result)
                result.append(root.val)
        traverse(root,result)
        return result
        