class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #10 000 000
        while n>0:
            if n%3==2:
                return False
            n//=3
        return True
        '''three = []
        for i in range(14):
            three.append(3**i)
        res = False

        def dfs(current,total,seen):
            seen.add(current)
            nonlocal res
            if total == n:
                res = True
            if res:
                return

            for item in three:
                if (item not in seen) and item+total<=n:
                    dfs(item,item+total,seen)
        
        for item in three:
            dfs(item,item,set())
        return res'''