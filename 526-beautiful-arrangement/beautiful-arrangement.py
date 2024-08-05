class Solution:
    def countArrangement(self, n: int) -> int:
        res=0

        def backtrack(path):
            nonlocal res
            if len(path)==n:
                res+=1
                return

            for j in range(1,n+1):
                m = len(path)+1
                if j not in path and (j%m==0 or m%j==0):
                    path.append(j)
                    backtrack(path)
                    path.pop()

        backtrack([])

        return res