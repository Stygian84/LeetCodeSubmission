# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        total=0
        def dfs(node):
            nonlocal total
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left_d = dfs(node.left)
            right_d = dfs(node.right) 
            for l in left_d:
                for r in right_d:
                    if l + r <= distance:
                        total += 1      
                        
            return [d + 1 for d in left_d + right_d]
                

        dfs(root)
    
        return total