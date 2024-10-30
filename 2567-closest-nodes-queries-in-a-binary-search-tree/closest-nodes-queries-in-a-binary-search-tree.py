# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        ls = []
        def traverse(node):
            nonlocal ls
            if node:
                traverse(node.left)
                ls.append(node.val)
                traverse(node.right)
        traverse(root)
        
        ans = []
        for q in queries:
            pos = bisect_left(ls,q)
            if 0<=pos<len(ls) and ls[pos]==q:
                ans.append([q,q])
            elif pos>=len(ls):
                ans.append([ls[-1],-1])
            elif pos<=0:
                ans.append([-1,ls[0]])
            else:
                ans.append([ls[pos-1],ls[pos]])
        return ans