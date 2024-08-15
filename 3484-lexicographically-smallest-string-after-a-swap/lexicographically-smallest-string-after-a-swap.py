class Solution:
    def getSmallestString(self, s: str) -> str:
        
        n = len(s)
        res = list(s)
        for i in range(1,n):
            if s[i]<s[i-1]:
                #check same parity
                if int(s[i])%2==int(s[i-1])%2:
                    #swap
                    res[i],res[i-1] = res[i-1], res[i]
                    break 

        return "".join(res)