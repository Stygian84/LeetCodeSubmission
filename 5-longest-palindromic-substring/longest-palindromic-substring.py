class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = s[0]
        n = len(s)
        for i in range(len(s)):
            j = 1
            while (i-j>=0 and j+i<n):
                if s[i-j]==s[i+j]:
                    if len(res)<2*j+1:
                        res = s[i-j:j+i+1]
                    j+=1
                else:
                    break
            
            #for even
            if i+1<n and (s[i]==s[i+1]):
                if 2>len(res):
                    res = s[i]+s[i+1]
                j=1
                while (i-j>=0 and j+i+1<n):
                    if s[i-j]==s[i+j+1]:
                        if len(res)<2*j+2:
                            res = s[i-j:j+i+2]
                        j+=1
                    else:
                        break
        return res