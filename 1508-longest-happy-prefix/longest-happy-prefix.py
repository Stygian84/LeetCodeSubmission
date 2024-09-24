class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        i=0
        j=n-1
        res = ""
        while i<n and j>0:
            if s[:i+1]==s[j:]:
                res=s[j:]
            i+=1
            j-=1
        return res
        '''p = set()
        
        for i in range(len(s)-1):
            p.add(s[:i+1])
        
        res = ""
        for j in range(len(s)-1,0,-1):
            if s[j:] in p:
               res = s[j:]
            
        return res '''