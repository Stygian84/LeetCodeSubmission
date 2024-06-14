# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(node):
            curr=node
            while curr.left:
                curr=curr.left
            return curr
        if not root:
            return root
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else: #val == key
            #for only 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            #for 2
            sucessor=minValueNode(root.right)
            root.val=sucessor.val
            root.right=self.deleteNode(root.right,sucessor.val)
        return root