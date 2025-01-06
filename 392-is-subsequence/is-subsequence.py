class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t:
            return True
        i = 0
        j = 0
        n = len(s)
        m = len(t)

        if m<n:
            return False
        if n==0:
            return True

        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        
        return i==n