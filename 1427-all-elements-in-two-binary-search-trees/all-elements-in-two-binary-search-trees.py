# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ls=[]
        ls2=[]
        def traverse(node,ls):
            if node:
                traverse(node.left,ls)
                ls.append(node.val)
                traverse(node.right,ls)
            return ls
        traverse(root1,ls)
        traverse(root2,ls)


        res=ls
        res.extend(ls2)
        res.sort()
        return res