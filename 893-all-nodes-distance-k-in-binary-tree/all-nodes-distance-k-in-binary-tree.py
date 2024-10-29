# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(set)

        def traverse(node,parent):

            if node:
                
                graph[parent].add(node.val)
                graph[node.val].add(parent)
                
                traverse(node.left,node.val)
                traverse(node.right,node.val)
        
        traverse(root,root.val)

        #print(graph)

        res = []
        def dfs(current,seen,count):
            nonlocal res
            seen.add(current)

            if count==k:
                res.append(current)
                return

            for neighbours in graph[current]:
                if neighbours not in seen:
                    dfs(neighbours,seen,count+1)

        dfs(target.val,set(),0)

        return res