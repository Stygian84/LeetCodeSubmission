# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dc = defaultdict(list)
        max_height = 0
        def traverse(node,height):
            nonlocal max_height
            if node:
                max_height = max(max_height,height)
                traverse(node.left,height+1)
                dc[height].append(node.val)
                traverse(node.right,height+1)
        traverse(root,0)
        print(dc)
        return dc[max_height][0]