# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        parent1 = defaultdict(set)
        parent2 = defaultdict(set)

        def traverse(node,parent):
            if node:
                parent[None].add(node.val)
                if node.left:
                    parent[node.val].add(node.left.val)
                if node.right:
                    parent[node.val].add(node.right.val)
                traverse(node.left,parent)
                traverse(node.right,parent)
        
        traverse(root1,parent1)
        traverse(root2,parent2)
        
        return parent1==parent2