class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        
        dc = defaultdict(dict)

        for x,y in pick:
            dc[x][y]=dc[x].get(y,0)+1

        count = 0
        for i in range(n):
            for v in dc[i].values():
                if v>=i+1:
                    count+=1
                    break
        
        return count