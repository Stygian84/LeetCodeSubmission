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

            for i in range(start,n):
                str_num = s[start:i+1]
                if not str_num:
                    continue
                number = int(str_num)
                if int(path[-1])-number==1:
                    path.append(str_num)
                    backtrack(i+1,path)
                    path.pop()
        
        for i in range(n):
            str_num = s[:i+1]
            backtrack(i+1,[str_num])

        if res:
            return True
        return False