# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # parent, child, isleft
        dc= {}
        children = set()
        for parent,child,isLeft in descriptions:
            if parent not in dc:
                dc[parent]= TreeNode(parent)
            
            if child not in dc:
                dc[child] = TreeNode(child)
            
            if isLeft:
                dc[parent].left=dc[child]
            else:
                dc[parent].right=dc[child]
            children.add(child)
            
        for parent, _ , _ in descriptions:
            if parent not in children:
                return dc[parent]