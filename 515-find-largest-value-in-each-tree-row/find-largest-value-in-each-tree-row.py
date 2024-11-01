# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        rows = defaultdict(list)

        def traverse(node,height):
            if node:
                rows[height].append(node.val)
                traverse(node.left,height+1)
                traverse(node.right,height+1)
        
        traverse(root,0)
        #print(rows)
        res = []
        for v in rows.values():
            res.append(max(v))
        return res