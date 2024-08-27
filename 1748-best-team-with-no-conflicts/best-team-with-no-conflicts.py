class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  
            for j in range(i):
                if players[j][1] <= players[i][1]:  
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)
        '''ls = []
        for s,a in zip(scores,ages):
            ls.append((s,a))

        ls.sort(reverse = True)

        n = len(ages)
        dp = [[0,0] for _ in range(n)]


        prev = None
        for i in range(n):
            s,a = ls[i]
            if prev and a>prev:
                dp[i]=[s,a]
            else:
                dp[i]=[dp[i-1][0]+s,a]
            prev = a

        res = 0
        for s,a in dp:
            if s > res:
                res=s
        return res'''