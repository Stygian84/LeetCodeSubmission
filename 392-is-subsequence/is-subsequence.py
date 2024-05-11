class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx=0
        if s=="":
            return True
        for letter in t:
            if idx>len(s)-1:
                break
            if s[idx]==letter:
                idx+=1
                continue
        if (idx)!=len(s):
            return False
        else:
            return True