class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #try insert 3 dots
        res = []
        n = len(s)

        def isValid(x):
            ls = x.split(".")
            for item in ls:
                if item and 0<=int(item)<=255:
                    if len(item)>1 and item[0]=="0":
                        return False
                else:
                    return False
            return True


        def insertDots(x,i,j,k):
            x = x[:k] + '.' + x[k:]
            x = x[:j] + '.' + x[j:]
            x = x[:i] + '.' + x[i:]
            return x
        
        def backtrack(start,path):
            if len(path)==3:
                a,b,c = path
                x=insertDots(s,a,b,c)
                if isValid(x):
                    res.append(x)
                return

            prev = path[-1]
            for i in range(start,n):
                if i-prev<=3:
                    path.append(i+1)
                    backtrack(i+1,path)
                    path.pop()
                if i-prev==3:
                    break

        for i in range(1,4):
            backtrack(i,[i])
        return res