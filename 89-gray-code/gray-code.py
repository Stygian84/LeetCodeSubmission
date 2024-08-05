class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = []
        for i in range(2 ** n):
            res.append(i ^ (i >> 1))
        return res
        '''if n == 1:
            return [0,1]

        def differs(x,y):
            xor_result = x ^ y
            return xor_result != 0 and (xor_result & (xor_result - 1)) == 0


        res = []
        def backtrack(path,seen):
            nonlocal res
            if len(path[:])==2**n and differs(path[-1], path[0]):
                res = path[:]
                return
            if res:
                return
            prev = path[-1]
            seen.add(prev)
            for i in range(2**n):
                if i not in seen and differs(prev,i):
                    seen.add(i)
                    path.append(i)
                    backtrack(path,seen)
                    path.pop()
                    seen.remove(i)
                

        seen = set()
        backtrack([0],seen)
        return res'''