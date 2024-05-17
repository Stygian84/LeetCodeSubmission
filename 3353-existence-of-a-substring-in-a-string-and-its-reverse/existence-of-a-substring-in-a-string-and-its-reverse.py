class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for idx in range(len(s)-1):
            if s[idx]+s[idx+1] in s[::-1]:
                return True
        return False
        