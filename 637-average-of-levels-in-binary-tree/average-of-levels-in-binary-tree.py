# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])

        while queue:
            total = 0
            count = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                total += node.val
                count += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(total / count)

        return result
        