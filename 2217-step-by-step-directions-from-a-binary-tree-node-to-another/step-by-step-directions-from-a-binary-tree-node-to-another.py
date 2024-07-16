# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(root, p, q):
            if not root:
                return None
            if root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, value, path):
                return True
            path.pop()
            return False
        
        lca = findLCA(root, startValue, destValue)
        
        pathToStart = []
        findPath(lca, startValue, pathToStart)
        pathToDest = []
        findPath(lca, destValue, pathToDest)
        
        directions = ['U'] * len(pathToStart) + pathToDest
        
        return ''.join(directions)