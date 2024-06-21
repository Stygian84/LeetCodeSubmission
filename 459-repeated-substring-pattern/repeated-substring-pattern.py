class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        if n==1:
            return False
        for i in range(1,n//2+1):
            temp_str=s[:i]
            if temp_str*(n//len(temp_str))==s:
                return True
        return False