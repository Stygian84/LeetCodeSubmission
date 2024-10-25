# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def traverse(node,current):
            nonlocal total
            if node:
                if node.val == 0:
                    current = current << 1
                elif node.val == 1:
                    current = current << 1 | 1
                traverse(node.left,current)
                traverse(node.right,current)
                if not node.left and not node.right: # leaf
                    total +=current

        traverse(root,0)
        return total
        