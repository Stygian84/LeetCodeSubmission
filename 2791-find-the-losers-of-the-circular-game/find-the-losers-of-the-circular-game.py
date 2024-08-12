class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = [False]*n

        i=0
        step = 0
        while players[i]!=True:
            players[i] = True
            
            step += 1
            i = i+k*step
            i %= n

        res = []

        for i in range(n):
            if not players[i]:
                res.append(i+1)
        return res
        