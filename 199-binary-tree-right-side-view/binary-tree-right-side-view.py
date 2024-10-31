# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        res = []
        height = defaultdict(list)

        def traverse(node,depth):
            if node:
                height[depth].append(node.val)

                traverse(node.right,depth+1)
                traverse(node.left,depth+1)

        traverse(root,0)
        for v in height.values():
            res.append(v[0])
        return res