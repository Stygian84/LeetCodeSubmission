class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def dfs(node,seen):
            
            if node<0 or node>=n:
                return False
            if node in seen:
                return False

            seen.add(node)
            value = arr[node]
            
            if value==0:
                return True

            return dfs(node+value,seen) or dfs(node-value,seen)

        return dfs(start,set())