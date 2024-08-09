class Solution:
    def printVertically(self, s: str) -> List[str]:
        ls = s.split()
        n = 1
        for item in ls:
            n = max(len(item),n)

        res = [""]*n


        for item in ls:
            m = len(item)
            last_idx = -1
            for i in range(n):
                if i>=m:
                    res[i] = res[i]+" "       
                else:
                    res[i] = res[i]+item[i]
                if res[i].isalpha():
                    last_idx=i
        
        for i in range(len(res)):
            res[i]=res[i].rstrip()
            
        return res