class Solution:
    def splitString(self, s: str) -> bool:
        res = []
        
        n = len(s)

        def backtrack(start,path):
            nonlocal res
            if start == n and len(path)>1:
                res.append(path[:])
                return
            if res:
                return

            for i in range(start,n+1):
                str_num = s[start:i+1]
                if not str_num:
                    continue
                if not path:
                    path.append(str_num)
                    backtrack(i+1,path)
                    path.pop()
                    continue
                number = int(str_num)
                if int(path[-1])-number==1:
                    path.append(str_num)
                    backtrack(i+1,path)
                    path.pop()



        backtrack(0,[])
        if res:
            return True
        return False