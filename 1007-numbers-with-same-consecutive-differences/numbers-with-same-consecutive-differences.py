class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtrack(path):
            nonlocal res
            if len(path)==n:
                res.append( int("".join(path)) )
                return
            
            for i in range(10):
                if not path and i!=0:
                    path.append(str(i))
                    backtrack(path)
                    path.pop()
                if path:
                    if abs(i-int(path[-1]))==k:
                        path.append(str(i))
                        backtrack(path)
                        path.pop()


        backtrack([])
        return res