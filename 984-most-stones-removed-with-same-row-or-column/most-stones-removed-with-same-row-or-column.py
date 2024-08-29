class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        seen = set()

        def dfs(x,y):
            seen.add((x,y))
            for a,b in stones:
                if (a,b) not in seen:
                    if a==x or b==y:
                        dfs(a,b)

        count = 0
        for a,b in stones:
            if (a,b) not in seen:
                dfs(a,b)
                count+=1
        return len(stones)-count
            