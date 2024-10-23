# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #cousin if same depth diff parents
        
        depth = defaultdict(int)
        def traverse(node,height):
            if node:
                depth[height] += node.val
                traverse(node.left,height+1)
                traverse(node.right,height+1)
                
        traverse(root,0)

        def replace(node,height,parent_val,siblings):
            if node:
                sibling_val = 0
                if node.left and node.right:
                    sibling_val += node.left.val + node.right.val
                elif node.left:
                    sibling_val = node.left.val
                elif node.right:
                    sibling_val = node.right.val
                
                replace(node.left,height+1,node.val,sibling_val)
                replace(node.right,height+1,node.val,sibling_val)

                if height==0 or height==1:
                    node.val = 0
                else:
                    node.val = depth[height]-siblings
        
        replace(root,0,0,0)
        
        return root