class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)  
        total_length = sum(matchsticks)
        
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        n = len(matchsticks)

        if matchsticks[0] > side_length:
            return False
        
        def backtrack(start,a,b,c,d):
            if start == n:
                return a==b==c==d
            
            item = matchsticks[start]
            if a + item <= side_length and backtrack(start + 1, a + item, b, c, d):
                return True
            if b + item <= side_length and backtrack(start + 1, a, b + item, c, d):
                return True
            if c + item <= side_length and backtrack(start + 1, a, b, c + item, d):
                return True
            if d + item <= side_length and backtrack(start + 1, a, b, c, d + item):
                return True
            return False

        return backtrack(0, 0, 0, 0, 0)
        '''dp = defaultdict(int)

        n = len(matchsticks)
        for i in range(n):
            length = matchsticks[i]
            dp[length]+=1
            if length*dp[length]!=length:
                dp[length*dp[length]]+=1

        print(dp)
        for value in dp.values():
            if value ==4:
                return True
        return False wrong'''