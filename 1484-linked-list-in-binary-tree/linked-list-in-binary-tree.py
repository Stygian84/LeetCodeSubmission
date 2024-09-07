# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        ls = []

        while head:
            ls.append(head.val)
            head = head.next
        
        n = len(ls)

        def dfs(node,i):
            if not node: return False

            if node.val != ls[i]: return False

            if i==n-1: return True

            return dfs(node.left,i+1) or dfs(node.right,i+1)
        
        def traverse(node):
            if not node: return False
            
            return dfs(node,0) or traverse(node.left) or traverse(node.right)

        return traverse(root)
        