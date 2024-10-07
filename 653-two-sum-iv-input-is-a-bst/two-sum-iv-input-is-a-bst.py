# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dc = defaultdict(int)
        
        def traverse(root):
            nonlocal dc
            if root:
                traverse(root.left)
                dc[root.val]+=1
                traverse(root.right)
        traverse(root)
        #print(dc)
        for key in dc.keys():
            if k-key in dc:
                if k-key==key:
                    if dc[key]>1:
                        return True
                    continue
                return True
        return False