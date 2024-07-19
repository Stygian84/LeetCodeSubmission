class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s==s[::-1]:
            return 1
        return len(set(s))
        
        
        