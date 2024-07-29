# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,path,target):
            if node:
                path.append(node.val)
                target-=node.val
                if target==0 and not node.left and not node.right:
                    res.append(path[:])
                else:
                    if node.left:
                        dfs(node.left,path,target)
                    if node.right:
                        dfs(node.right,path,target)
                path.pop()


        dfs(root,[],targetSum)
        
        return res