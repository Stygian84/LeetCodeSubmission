# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dc_sum = defaultdict(int)

        def traverse(node,level):
            if node:
                traverse(node.left,level+1)
                dc_sum[level] += node.val
                traverse(node.right,level+1)

        traverse(root,0)
        res = []
        for v in dc_sum.values():
            res.append(v)

        if k>len(res):
            return -1

        res.sort()
        
        return res[-k]