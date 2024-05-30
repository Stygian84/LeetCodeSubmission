class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=""
        for idx in range(0,len(s),2*k):

            res+=s[idx:idx+k][::-1]
            res+=s[idx+k:idx+2*k]
        return res