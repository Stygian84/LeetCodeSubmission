# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        res = []

        offset = ord('a')

        def traverse(node,current):
            nonlocal res
            if node.left or node.right:
                if node.left:
                    traverse(node.left, current+chr(node.val + offset))
                if node.right:
                    traverse(node.right, current+chr(node.val + offset))
            else:
                res.append( (current + chr(node.val + offset))[::-1])
                return

        traverse(root,"")    
        #print(res)
        res.sort()
        
        return res[0]