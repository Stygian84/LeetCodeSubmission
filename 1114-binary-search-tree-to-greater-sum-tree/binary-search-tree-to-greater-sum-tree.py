# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_traversal(node,acc_sum):
            if not node:
                return acc_sum
            
            acc_sum=reverse_traversal(node.right,acc_sum)
            node.val+=acc_sum
            acc_sum=node.val

            return reverse_traversal(node.left,acc_sum)
        
        reverse_traversal(root,0)
        return root