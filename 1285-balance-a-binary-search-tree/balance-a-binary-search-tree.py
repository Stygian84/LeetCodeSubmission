# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        result=[]
        def traverse(root,result):
            if root:
                traverse(root.left,result)
                result.append(root.val)
                traverse(root.right,result)
        traverse(root,result)

        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sorted_array_to_bst(nums[:mid])
            node.right = sorted_array_to_bst(nums[mid+1:])
            return node
        
        return sorted_array_to_bst(result)