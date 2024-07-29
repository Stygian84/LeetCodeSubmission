# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node,current_sum,prefix):
            if not node:
                return 0

            current_sum+=node.val
            paths = prefix[current_sum-targetSum]

            prefix[current_sum]+=1

            paths += dfs(node.left,current_sum,prefix)
            paths += dfs(node.right,current_sum,prefix)

            prefix[current_sum]-=1

            
            return paths

        prefix_sum_count=defaultdict(int)
        prefix_sum_count[0]=1
        return dfs(root,0,prefix_sum_count)