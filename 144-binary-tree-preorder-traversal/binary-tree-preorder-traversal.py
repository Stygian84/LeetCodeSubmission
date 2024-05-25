# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(root,result):
            if root:
                result.append(root.val)
                traverse(root.left,result)
                traverse(root.right,result)
        traverse(root,result)
        return result
        
        